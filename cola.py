import customtkinter as ctk

# =========================
# CONFIGURAÇÃO GLOBAL
# =========================
ctk.set_appearance_mode("dark")  # tema
ctk.set_default_color_theme("blue")


# =========================
# CLASSE PRINCIPAL (APP)
# =========================
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema exemplo")
        self.geometry("500x400")

        # Container principal (onde as telas ficam)
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Dicionário para armazenar telas
        self.frames = {}

        # Criando telas
        for Tela in (LoginScreen, MenuScreen, CadastroScreen):
            frame = Tela(self.container, self)
            self.frames[Tela] = frame

            # coloca todas no mesmo lugar
            frame.grid(row=0, column=0, sticky="nsew")

        # mostra tela inicial
        self.show_frame(LoginScreen)

    # função de navegação
    def show_frame(self, tela):
        frame = self.frames[tela]
        frame.tkraise()  # traz a tela para frente


# =========================
# TELA 1 - LOGIN
# =========================
class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller  # referência ao App

        # título
        titulo = ctk.CTkLabel(self, text="Login", font=("Arial", 20))
        titulo.pack(pady=20)

        # campo usuário
        self.user = ctk.CTkEntry(self, placeholder_text="Usuário")
        self.user.pack(pady=10)

        # campo senha
        self.senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.senha.pack(pady=10)

        # botão login
        botao = ctk.CTkButton(self, text="Entrar", command=self.login)
        botao.pack(pady=20)

        self.msg = ctk.CTkLabel(self, text="")
        self.msg.pack()

    def login(self):
        # pega valores digitados
        user = self.user.get()
        senha = self.senha.get()

        # validação simples
        if user == "admin" and senha == "123":
            self.msg.configure(text="Login OK")
            self.controller.show_frame(MenuScreen)  # troca tela
        else:
            self.msg.configure(text="Erro no login")


# =========================
# TELA 2 - MENU
# =========================
class MenuScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        titulo = ctk.CTkLabel(self, text="Menu", font=("Arial", 20))
        titulo.pack(pady=20)

        # botão para cadastro
        btn_cadastro = ctk.CTkButton(
            self,
            text="Ir para Cadastro",
            command=lambda: controller.show_frame(CadastroScreen)
        )
        btn_cadastro.pack(pady=10)

        # botão logout
        btn_logout = ctk.CTkButton(
            self,
            text="Sair",
            command=lambda: controller.show_frame(LoginScreen)
        )
        btn_logout.pack(pady=10)


# =========================
# TELA 3 - CADASTRO
# =========================
class CadastroScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        titulo = ctk.CTkLabel(self, text="Cadastro", font=("Arial", 20))
        titulo.pack(pady=20)

        # nome
        self.nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.nome.pack(pady=10)

        # idade
        self.idade = ctk.CTkEntry(self, placeholder_text="Idade")
        self.idade.pack(pady=10)

        # checkbox
        self.termos = ctk.CTkCheckBox(self, text="Aceito os termos")
        self.termos.pack(pady=10)

        # slider
        self.slider = ctk.CTkSlider(self, from_=0, to=10)
        self.slider.pack(pady=10)

        # botão salvar
        btn_salvar = ctk.CTkButton(self, text="Salvar", command=self.salvar)
        btn_salvar.pack(pady=10)

        # botão voltar
        btn_voltar = ctk.CTkButton(
            self,
            text="Voltar",
            command=lambda: controller.show_frame(MenuScreen)
        )
        btn_voltar.pack(pady=10)

        self.msg = ctk.CTkLabel(self, text="")
        self.msg.pack()

    def salvar(self):
        nome = self.nome.get()
        idade = self.idade.get()
        termos = self.termos.get()
        nivel = self.slider.get()

        self.msg.configure(
            text=f"{nome}, {idade} anos | termos: {termos} | nivel: {nivel:.1f}"
        )


# =========================
# EXECUÇÃO
# =========================
app = App()
app.mainloop()