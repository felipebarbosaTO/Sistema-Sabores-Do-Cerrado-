import tkinter as tk
from tkinter import messagebox, ttk
from controller.receita_controller import ReceitaController
from view.avaliacao_view import AvaliacaoView

class LoginView:
    def __init__(self, id_usuario, nome):
        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.nome = nome

        self.janela = tk.Tk()
        self.janela.title("🍽️ Sistema de Receitas")
        self.janela.geometry("900x650")

        frame = tk.Frame(self.janela, bg="white", bd=3, relief="ridge")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text=f"Bem-vindo, {nome}!", font=("Arial", 16, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Lista Receitas:", bg="white").grid(row=1, column=0, pady=5)
        self.lista = tk.Listbox(frame, width=40, height=8)
        self.lista.grid(row=1, column=1, pady=5)

        tk.Button(frame, text="Ver Receita", bg="#2196F3", fg="white", command=self.ver_receita).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Gerar Cardápio", bg="#9C27B0", fg="white", command=self.cardapio).grid(row=3, column=0, columnspan=2, pady=5)

        self.atualizar_lista()
        self.janela.mainloop()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for r in self.controller.listar():
            self.lista.insert(tk.END, f"{r[0]} - {r[1]}")

    def ver_receita(self):
        selecao = self.lista.curselection()
        if not selecao:
            return
        id_receita = int(self.lista.get(selecao[0]).split(" - ")[0])
        dados = self.controller.detalhes(self.id_usuario, id_receita)
        AvaliacaoView(self.id_usuario, id_receita, dados)

    def cardapio(self):
        lista = self.controller.gerar_cardapio()
        messagebox.showinfo("Cardápio do Dia", "\n".join(lista))