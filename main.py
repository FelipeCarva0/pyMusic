# Importamos a classe principal do Kivy que cria aplicações
from kivy.app import App

# BoxLayout é um tipo de layout que organiza elementos em linha ou coluna
from kivy.uix.boxlayout import BoxLayout

# Campo de texto onde o usuário digita ou cola algo
from kivy.uix.textinput import TextInput

# Botão clicável
from kivy.uix.button import Button


# Importamos as funções que criamos no arquivo downloader.py
from downloader import baixar_video, baixar_audio


# Criamos uma classe chamada Interface
# Ela herda de BoxLayout (herdar significa aproveitar funcionalidades da classe)
class Interface(BoxLayout):


    # O método __init__ é executado quando a classe é criada
    # Ele funciona como um "construtor"
    def __init__(self, **kwargs):

        # Chamamos o construtor da classe pai (BoxLayout)
        super().__init__(orientation="vertical", **kwargs)

        # Criamos um campo de texto
        # hint_text é o texto que aparece como dica
        self.url = TextInput(
            hint_text="Cole a URL do YouTube aqui",
            size_hint=(1, 0.2)
        )

        # Adiciona o campo de texto à interface
        self.add_widget(self.url)


        # Criamos um botão para baixar vídeo
        btn_video = Button(text="Baixar Vídeo")

        # bind conecta o clique do botão a uma função
        btn_video.bind(on_press=self.download_video)

        # adiciona o botão à interface
        self.add_widget(btn_video)


        # Criamos outro botão para baixar áudio
        btn_audio = Button(text="Baixar Áudio")

        # Quando clicado, chama a função download_audio
        btn_audio.bind(on_press=self.download_audio)

        # adiciona o botão na interface
        self.add_widget(btn_audio)


    # Função chamada quando o botão "Baixar Vídeo" é pressionado
    def download_video(self, instance):

        # Pegamos o texto digitado no campo
        url = self.url.text

        # Chamamos a função do downloader
        baixar_video(url)


    # Função chamada quando o botão "Baixar Áudio" é pressionado
    def download_audio(self, instance):

        # Pegamos o link digitado
        url = self.url.text

        # Chamamos a função que baixa áudio
        baixar_audio(url)



# Criamos a classe principal da aplicação
class PyMusicApp(App):

    # Esse método define qual será a interface inicial
    def build(self):

        # Retorna nossa interface personalizada
        return Interface()



# Executa a aplicação
PyMusicApp().run()