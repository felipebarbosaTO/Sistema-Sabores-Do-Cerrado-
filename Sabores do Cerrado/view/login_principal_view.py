import tkinter as tk
from tkinter import messagebox
from controller.receita_controller import ReceitaController
from view.principal_view import PrincipalView
from view.login_view import LoginView


class Application:
    def __init__(self, master=None):
        self.master = master
        self.controller = ReceitaController()
        self.master.title("🍽️ Login - Sistema Sabores do Cerrado")
        # Tela cheia configurável
        self.fullscreen = True
        self.master.attributes("-fullscreen", self.fullscreen)
        self.master.bind("<Escape>", self.toggle_fullscreen)

        #  self.master.geometry("400x320")
        self.master.configure(bg="#FAFAFA")
        self.master.resizable(False, False)

        frame = tk.Frame(self.master, bg="white", bd=3, relief="ridge")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="Acesso ao Sistema",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#333"
        ).pack(pady=(10, 20))

        tk.Label(frame, text="Usuário:", font=("Arial", 11), bg="white").pack(anchor="w", padx=15)
        self.nome = tk.Entry(frame, width=35, font=("Arial", 10))
        self.nome.pack(padx=15, pady=5)

        tk.Label(frame, text="Senha:", font=("Arial", 11), bg="white").pack(anchor="w", padx=15)
        self.senha = tk.Entry(frame, width=35, font=("Arial", 10), show="•")
        self.senha.pack(padx=15, pady=5)

        tk.Button(
            frame,
            text="Entrar",
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.verificaSenha
        ).pack(pady=15)

        self.mensagem = tk.Label(frame, text="", bg="white", font=("Arial", 10))
        self.mensagem.pack(pady=5)

        master.bind('<Return>', lambda event: self.verificaSenha())

        tk.Label(
            self.master,
            text="Sabores do Cerrado © 2025",
            font=("Arial", 8),
            bg="#FAFAFA",
            fg="#777"
        ).pack(side="bottom", pady=5)

    def verificaSenha(self):
        usuario = self.nome.get().strip()
        senha = self.senha.get().strip()

        if not usuario or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        dados = self.controller.autenticar_usuario(usuario, senha)

        if dados:
            tipo = dados["tipo_usuario"]
            id_usuario = dados["id_usuario"]
            nome = dados["nome"]

            self.mensagem.config(fg="green", text=f"Acesso permitido ({tipo})")
            messagebox.showinfo("Bem-vindo", f"Olá {nome}, você está logado como {tipo.upper()}!")

            self.master.withdraw()  

            if tipo.lower() == "admin":
                PrincipalView(id_usuario, nome)
            else:
                LoginView(id_usuario, nome)

            self.master.withdraw()

        else:
            self.mensagem.config(fg="red", text="Usuário ou senha inválidos!")
            messagebox.showerror("Erro", "Credenciais incorretas!")

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.master.attributes("-fullscreen", True)
        else:
            self.master.attributes("-fullscreen", False)
            self.master.geometry("400x320")
            self.master.update_idletasks()



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
