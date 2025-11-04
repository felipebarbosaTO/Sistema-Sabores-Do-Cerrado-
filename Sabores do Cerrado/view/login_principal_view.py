import tkinter as tk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from login_principal_view import PrincipalView
from login_view import LoginView


def get_connection():
        try:
            connection = mysql.connector.connect(
                host= 'localhost',
                database= 'Lista_receitas',
                user= 'root',
                password= 'turma@283'
            )
            return connection
        except Error as e:
            print(f"Erro ao connection ao MySQL: {e}")
            return None
        

class Application:
    def __init__(self, master=None):
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
            command=self.verificaSenha
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

        conexao = get_connection()
        if not conexao:
            return

        cursor = conexao.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT nome, tipo_usuario FROM usuario WHERE nome=%s AND senha=%s",
                (usuario, senha)
            )
            dados = cursor.fetchone()

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
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro SQL", f"Erro ao executar consulta: {erro}")
        finally:
            cursor.close()
            conexao.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()