import tkinter as tk
from tkinter import messagebox, ttk
from controller.receita_controller import ReceitaController
from view.avaliacao_view import AvaliacaoView

class PrincipalView:
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

        tk.Label(frame, text="Nome da Receita:", bg="white").grid(row=1, column=0)
        self.nome_r = tk.Entry(frame, width=35)
        self.nome_r.grid(row=1, column=1)

        tk.Label(frame, text="Tempo de Preparo:", bg="white").grid(row=2, column=0)
        self.tempo_r = tk.Entry(frame, width=35)
        self.tempo_r.grid(row=2, column=1)

        tk.Label(frame, text="Ingredientes:", bg="white").grid(row=3, column=0)
        self.ingr_r = tk.Text(frame, width=30, height=5)
        self.ingr_r.grid(row=3, column=1)

        tk.Label(frame, text="Modo de Preparo:", bg="white").grid(row=4, column=0)
        self.modo_r = tk.Text(frame, width=30, height=5)
        self.modo_r.grid(row=4, column=1)

        tk.Label(frame, text="Categoria:", bg="white").grid(row=5, column=0)
        self.categoria = tk.Entry(frame, width=35)
        self.categoria.grid(row=5, column=1)

        tk.Label(frame, text="Dificuldade:", bg="white").grid(row=6, column=0)
        self.combo_dificuldade = ttk.Combobox(frame, values=["Fácil", "Médio", "Difícil"], state="readonly", width=10)
        self.combo_dificuldade.grid(row=6, column=1)

        tk.Label(frame, text="Link da Imagem:", bg="white").grid(row=7, column=0)
        self.link_imagem = tk.Entry(frame, width=35)
        self.link_imagem.grid(row=7, column=1)

        tk.Label(frame, text="Link do Vídeo:", bg="white").grid(row=8, column=0)
        self.link_video = tk.Entry(frame, width=35)
        self.link_video.grid(row=8, column=1)

        self.lista = tk.Listbox(frame, width=40, height=8)
        self.lista.grid(row=5, column=1, pady=10)

        tk.Button(frame, text="Cadastrar Receita", bg="#4CAF50", fg="white", command=self.cadastrar).grid(row=10, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Ver Receita", bg="#2196F3", fg="white", command=self.ver_receita).grid(row=11, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Gerar Cardápio", bg="#9C27B0", fg="white", command=self.cardapio).grid(row=12, column=0, columnspan=2, pady=5)

        self.atualizar_lista()
        self.janela.mainloop()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for r in self.controller.listar():
            self.lista.insert(tk.END, f"{r[0]} - {r[1]}")

        self.controller.cadastrar(
            self.id_usuario,
            self.nome_r.get(),
            self.tempo_r.get(),
            self.ingr_r.get("1.0", "end-1c"),
            self.modo_r.get("1.0", "end-1c"),
            self.categoria.get(),
            self.combo_dificuldade.get(),
            self.link_imagem.get(),
            self.link_video.get()
)
        messagebox.showinfo("Sucesso", "Receita cadastrada!")
        self.atualizar_lista()

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