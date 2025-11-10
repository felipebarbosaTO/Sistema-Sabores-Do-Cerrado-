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
        self.janela.title("🍽️ Sistema de Receitas - Administrador")

        # Fullscreen
        self.fullscreen = True
        self.janela.attributes("-fullscreen", self.fullscreen)
        self.janela.bind("<Escape>", self.toggle_fullscreen)

        # Fundo com Canvas redimensionável
        self.background = tk.Canvas(self.janela, highlightthickness=0)
        self.background.pack(fill="both", expand=True)
        self.background.bind("<Configure>", self._on_resize)

        frame = tk.Frame(self.background, bg="white", bd=3, relief="ridge", padx=25, pady=25)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text=f"Bem-vindo, {nome} (ADMIN)!", font=("Arial", 18, "bold"), bg="white", fg="#333").grid(row=0, column=0, columnspan=2, pady=10)

        self._criar_entrada(frame, "Nome da Receita:", 1)
        self.nome_r = tk.Entry(frame, width=35, font=("Arial", 10))
        self.nome_r.grid(row=1, column=1, pady=5)

        self._criar_entrada(frame, "Ingredientes:", 2)
        self.ingr_r = tk.Text(frame, width=35, height=4, font=("Arial", 10))
        self.ingr_r.grid(row=2, column=1, pady=5)

        self._criar_entrada(frame, "Modo de Preparo:", 3)
        self.modo_r = tk.Text(frame, width=35, height=4, font=("Arial", 10))
        self.modo_r.grid(row=3, column=1, pady=5)

        self._criar_entrada(frame, "Categoria:", 4)
        self.categoria = tk.Entry(frame, width=35, font=("Arial", 10))
        self.categoria.grid(row=4, column=1, pady=5)

        self._criar_entrada(frame, "Dificuldade:", 5)
        self.combo_dificuldade = ttk.Combobox(frame, values=["Fácil", "Médio", "Difícil"], state="readonly", width=15)
        self.combo_dificuldade.grid(row=5, column=1, pady=5)

        self._criar_entrada(frame, "Link da Imagem:", 6)
        self.link_imagem = tk.Entry(frame, width=35)
        self.link_imagem.grid(row=6, column=1, pady=5)

        self._criar_entrada(frame, "Link do Vídeo:", 7)
        self.link_video = tk.Entry(frame, width=35)
        self.link_video.grid(row=7, column=1, pady=5)

        self.lista = tk.Listbox(frame, width=45, height=8, font=("Arial", 10))
        self.lista.grid(row=8, column=0, columnspan=2, pady=10)

        self._criar_botao(frame, "Cadastrar Receita", "#4CAF50", self.cadastrar, 9)
        self._criar_botao(frame, "Ver Receita", "#2196F3", self.ver_receita, 10)
        self._criar_botao(frame, "Gerar Cardápio", "#9C27B0", self.cardapio, 11)

        self.atualizar_lista()
        self.janela.mainloop()

    def _criar_entrada(self, parent, texto, linha):
        tk.Label(parent, text=texto, bg="white", font=("Arial", 12)).grid(row=linha, column=0, sticky="e", pady=3)

    def _criar_botao(self, parent, texto, cor, comando, linha):
        btn = tk.Button(
            parent, text=texto, bg=cor, fg="white",
            font=("Arial", 11, "bold"), relief="flat",
            command=comando, width=25, height=1
        )
        btn.grid(row=linha, column=0, columnspan=2, pady=6)
        btn.bind("<Enter>", lambda e: btn.config(bg=self._escurecer(cor)))
        btn.bind("<Leave>", lambda e: btn.config(bg=cor))

    def _escurecer(self, cor):
        cor = cor.lstrip("#")
        r, g, b = tuple(int(cor[i:i+2], 16) for i in (0, 2, 4))
        return f"#{max(r-30,0):02x}{max(g-30,0):02x}{max(b-30,0):02x}"

    def _on_resize(self, event):
        w = event.width
        h = event.height
        self.background.delete("__gradient__")
        self._draw_gradient(w, h, "#FFF8E7", "#FFD580")

    def _draw_gradient(self, width, height, color1, color2):
        try:
            r1, g1, b1 = [v >> 8 for v in self.janela.winfo_rgb(color1)]
            r2, g2, b2 = [v >> 8 for v in self.janela.winfo_rgb(color2)]
            for i in range(height):
                ratio = i / max(height - 1, 1)
                r = int(r1 + (r2 - r1) * ratio)
                g = int(g1 + (g2 - g1) * ratio)
                b = int(b1 + (b2 - b1) * ratio)
                color = f"#{r:02x}{g:02x}{b:02x}"
                self.background.create_line(0, i, width, i, fill=color, tags="__gradient__")
        except Exception:
            self.background.create_rectangle(0, 0, width, height, fill=color1, outline="", tags="__gradient__")

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for r in self.controller.listar():
            self.lista.insert(tk.END, f"{r[0]} - {r[1]}")

    def cadastrar(self):
        self.controller.cadastrar(
            self.nome_r.get(),
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
            messagebox.showwarning("Aviso", "Selecione uma receita.")
            return
        id_receita = int(self.lista.get(selecao[0]).split(" - ")[0])
        dados = self.controller.detalhes(self.id_usuario, id_receita)
        AvaliacaoView(self.id_usuario, id_receita, dados)

    def cardapio(self):
        lista = self.controller.gerar_cardapio()
        messagebox.showinfo("Cardápio do Dia", "\n".join(lista))

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.janela.attributes("-fullscreen", True)
        else:
            self.janela.attributes("-fullscreen", False)
            self.janela.geometry("900x650")
            self.janela.update_idletasks()
