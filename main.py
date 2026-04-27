import customtkinter as ctk
import threading
from downloader import baixar_video, baixar_audio, obter_info

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("pyMusic Downloader")
app.geometry("500x400")

# Título
titulo = ctk.CTkLabel(app, text="Downloader", font=("Arial", 18))
titulo.pack(pady=10)

# Entrada URL
entry = ctk.CTkEntry(app, width=400, placeholder_text="Cole a URL")
entry.pack(pady=10)

# Preview título
preview_label = ctk.CTkLabel(app, text="Título aparecerá aqui")
preview_label.pack(pady=5)

# Barra de progresso
progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(pady=10)

# Status
status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=5)


# 🔹 Atualizar preview automaticamente
def atualizar_preview(event=None):
    url = entry.get()
    if not url:
        return

    preview_label.configure(text="Carregando título...")
    app.update()

    def task():
        titulo = obter_info(url)
        preview_label.configure(text=titulo)

    threading.Thread(target=task).start()


entry.bind("<FocusOut>", atualizar_preview)


# 🔹 Atualizar barra
def atualizar_progresso(valor):
    progress_bar.set(valor)
    app.update()


# 🔹 Download vídeo
def baixar_video_click():
    url = entry.get()
    if not url:
        status_label.configure(text="Digite uma URL")
        return

    progress_bar.set(0)
    status_label.configure(text="Baixando vídeo...")

    def task():
        resultado = baixar_video(url, atualizar_progresso)
        status_label.configure(text=resultado)

    threading.Thread(target=task).start()


# 🔹 Download áudio
def baixar_audio_click():
    url = entry.get()
    if not url:
        status_label.configure(text="Digite uma URL")
        return

    progress_bar.set(0)
    status_label.configure(text="Baixando áudio...")

    def task():
        resultado = baixar_audio(url, atualizar_progresso)
        status_label.configure(text=resultado)

    threading.Thread(target=task).start()


# Botões
btn_video = ctk.CTkButton(app, text="Baixar Vídeo", command=baixar_video_click)
btn_video.pack(pady=10)

btn_audio = ctk.CTkButton(app, text="Baixar Áudio", command=baixar_audio_click)
btn_audio.pack(pady=10)

app.mainloop()