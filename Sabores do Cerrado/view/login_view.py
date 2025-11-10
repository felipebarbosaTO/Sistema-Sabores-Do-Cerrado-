import tkinter as tk
from tkinter import messagebox
from controller.receita_controller import ReceitaController
from view.avaliacao_view import AvaliacaoView

class LoginView:
    def __init__(self, id_usuario, nome):
        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.nome = nome

        self.janela = tk.Tk()
        self.janela.title("🍽️ Sistema de Receitas - Usuário Comum")

        # Ativa fullscreen
        self.fullscreen = True
        self.janela.attributes("-fullscreen", self.fullscreen)
        self.janela.bind("<Escape>", self.toggle_fullscreen)

         # Fundo com Canvas redimensionável
        self.background = tk.Canvas(self.janela, highlightthickness=0)
        self.background.pack(fill="both", expand=True)
        self.background.bind("<Configure>", self._on_resize)

        frame = tk.Frame(self.background, bg="white", bd=3, relief="ridge", padx=25, pady=25)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame, text=f"Bem-vindo, {nome}!", font=("Arial", 18, "bold"),
            bg="white", fg="#333"
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Lista de Receitas:", bg="white", font=("Arial", 12)).grid(row=1, column=0, pady=5)
        self.lista = tk.Listbox(frame, width=45, height=10, font=("Arial", 10))
        self.lista.grid(row=1, column=1, pady=5)

        self._criar_botao(frame, "Ver Receita", "#2196F3", self.ver_receita, 2)
        self._criar_botao(frame, "Gerar Cardápio", "#9C27B0", self.cardapio, 3)

        self.atualizar_lista()
        self.janela.mainloop()

    def _criar_botao(self, parent, texto, cor, comando, linha):
        btn = tk.Button(
            parent, text=texto, bg=cor, fg="white",
            font=("Arial", 11, "bold"), relief="flat",
            command=comando, width=20, height=1
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
        self._draw_gradient(w, h, "#FFFAF0", "#FFE4B5")

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
            self.background.create_line(0, i, 900, i, fill=f"#{r:02x}{g:02x}{b:02x}")

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for r in self.controller.listar():
            self.lista.insert(tk.END, f"{r[0]} - {r[1]}")

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
