import tkinter as tk
from tkinter import messagebox
from controller.receita_controller import ReceitaController
from view.principal_view import PrincipalView
from view.login_view import LoginView

class Application:
    def __init__(self, master=None):
        self.master = master  
        self.controller = ReceitaController()

        self.fontePadrao = ("Arial", 10, "bold")
        master.title("Login - Sistema Sabores do Cerrado")
        master.geometry("360x250")
        master.resizable(False, False)

        tk.Label(master, text="Autenticação de Usuário", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

        tk.Label(master, text="Usuário:", font=self.fontePadrao).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.nome = tk.Entry(master, width=30, font=self.fontePadrao)
        self.nome.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(master, text="Senha:", font=self.fontePadrao).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.senha = tk.Entry(master, width=30, font=self.fontePadrao, show="*")
        self.senha.grid(row=2, column=1, padx=10, pady=10)

        self.botao = tk.Button(
            master,
            text="Autenticar",
            font=("Calibri", 9, "bold"),
            width=12,
            command=self.verificaSenha,
        )
        self.botao.grid(row=3, column=0, columnspan=2, pady=15)

        self.mensagem = tk.Label(master, text="", font=self.fontePadrao)
        self.mensagem.grid(row=4, column=0, columnspan=2)

    def verificaSenha(self):
        usuario = self.nome.get().strip()
        senha = self.senha.get().strip()

        if usuario == "" or senha == "":
            messagebox.showwarning("Aviso", "Preencha todos os campos!")   
            return

        dados = self.controller.autenticar_usuario(usuario, senha)

        if dados:
                tipo = dados["tipo_usuario"]
                id_usuario = dados["id_usuario"]
                nome = dados["nome"]

                self.mensagem["fg"] = "green"
                self.mensagem["text"] = f"Acesso permitido ({tipo})"
                messagebox.showinfo("Bem-vindo", f"Olá {nome}, você está logado como {tipo.upper()}!")

                self.master.destroy()

                if tipo.lower() == "admin":
                    PrincipalView(id_usuario, nome)
                else:
                    LoginView(id_usuario, nome)
        else:
                self.mensagem["fg"] = "red"
                self.mensagem["text"] = "Usuário ou senha inválidos!"
                messagebox.showerror("Erro", "Credenciais incorretas!")
        


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()