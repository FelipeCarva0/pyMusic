import os
import yt_dlp
import sys


def baixar_video(url):

    os.makedirs("downloads/video", exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/video/%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "logger": None,
        "no_warnings": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def baixar_audio(url):

    os.makedirs("downloads/audio", exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/audio/%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "logger": None,
        "no_warnings": True,

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])