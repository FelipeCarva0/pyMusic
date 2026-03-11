import yt_dlp
import sys


def baixar_video(url):

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "noplaylist": True,

        # evita erro de logging no Windows GUI
        "quiet": True,
        "no_warnings": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def baixar_audio(url):

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "noplaylist": True,

        "quiet": True,
        "no_warnings": True,

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])