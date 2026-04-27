import yt_dlp
import os


def obter_info(url):
    try:
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get("title", "Título não encontrado")
    except Exception:
        return "Erro ao obter informações"


def baixar_video(url, progress_callback=None):
    try:
        os.makedirs("downloads/video", exist_ok=True)

        def hook(d):
            if progress_callback and d["status"] == "downloading":
                total = d.get("total_bytes") or d.get("total_bytes_estimate")
                downloaded = d.get("downloaded_bytes", 0)
                if total:
                    progress_callback(downloaded / total)

        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": "downloads/video/%(title)s.%(ext)s",
            "noplaylist": True,
            "quiet": True,
            "progress_hooks": [hook]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return "Download concluído!"

    except Exception as e:
        return f"Erro: {str(e)}"


def baixar_audio(url, progress_callback=None):
    try:
        os.makedirs("downloads/audio", exist_ok=True)

        def hook(d):
            if progress_callback and d["status"] == "downloading":
                total = d.get("total_bytes") or d.get("total_bytes_estimate")
                downloaded = d.get("downloaded_bytes", 0)
                if total:
                    progress_callback(downloaded / total)

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/audio/%(title)s.%(ext)s",
            "noplaylist": True,
            "quiet": True,
            "progress_hooks": [hook],
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return "Download concluído!"

    except Exception as e:
        return f"Erro: {str(e)}"