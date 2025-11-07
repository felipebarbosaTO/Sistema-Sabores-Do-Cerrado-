import tkinter as tk
from tkinter import messagebox
import webbrowser
from controller.receita_controller import ReceitaController


class AvaliacaoView:
    def __init__(self, id_usuario, id_receita, dados):
        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.id_receita = id_receita
        self.dados = dados or {}

        self.janela = tk.Toplevel()
        self.janela.title(f"🍽️ Detalhes da Receita - {self.dados.get('nome', 'Sem Nome')}")
        self.janela.geometry("700x650")
        self.janela.configure(bg="#FAFAFA")

        frame = tk.Frame(self.janela, bg="white", bd=3, relief="ridge", padx=15, pady=15)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(frame, text=self.dados.get("nome", "Receita sem nome"),
                 font=("Arial", 20, "bold"), bg="white", fg="#333").pack(pady=(5, 10))

        tk.Label(frame, text=f"Categoria: {self.dados.get('categoria', 'Não informada')}",
                 font=("Arial", 12), bg="white").pack(pady=2)
        tk.Label(frame, text=f"Dificuldade: {self.dados.get('dificuldade', 'Não informada')}",
                 font=("Arial", 12), bg="white").pack(pady=2)

        tk.Label(frame, text="🧂 Ingredientes:", font=("Arial", 14, "bold"),
                 bg="white", fg="#555").pack(pady=(15, 5))
        tk.Message(frame, text=self.dados.get("ingredientes", "Sem ingredientes cadastrados."),
                   width=600, bg="#FFF", font=("Arial", 11), relief="sunken", bd=1, padx=8, pady=5).pack(pady=3)

        tk.Label(frame, text="🍳 Modo de Preparo:", font=("Arial", 14, "bold"),
                 bg="white", fg="#555").pack(pady=(15, 5))
        tk.Message(frame, text=self.dados.get("modo_preparo", "Sem modo de preparo cadastrado."),
                   width=600, bg="#FFF", font=("Arial", 11), relief="sunken", bd=1, padx=8, pady=5).pack(pady=3)

        if self.dados.get("link_imagem"):
            link_imagem = tk.Label(frame, text="📷 Ver Imagem", fg="blue", bg="white",
                                   cursor="hand2", font=("Arial", 11, "underline"))
            link_imagem.pack(pady=5)
            link_imagem.bind("<Button-1>", lambda e: webbrowser.open(self.dados["link_imagem"]))

        if self.dados.get("link_video"):
            link_video = tk.Label(frame, text="🎬 Ver Vídeo", fg="blue", bg="white",
                                  cursor="hand2", font=("Arial", 11, "underline"))
            link_video.pack(pady=5)
            link_video.bind("<Button-1>", lambda e: webbrowser.open(self.dados["link_video"]))

        tk.Label(frame, text="⭐ Avalie esta receita:", font=("Arial", 14, "bold"), bg="white").pack(pady=(15, 10))
        self.nota = tk.StringVar(value="5")

        notas = [("⭐ 1", "1"), ("⭐⭐ 2", "2"), ("⭐⭐⭐ 3", "3"), ("⭐⭐⭐⭐ 4", "4"), ("⭐⭐⭐⭐⭐ 5", "5")]
        stars_frame = tk.Frame(frame, bg="white")
        stars_frame.pack()
        for texto, valor in notas:
            tk.Radiobutton(stars_frame, text=texto, variable=self.nota, value=valor, bg="white",
                           activebackground="white").pack(side="left", padx=5)

        tk.Label(frame, text="📝 Comentário:", font=("Arial", 13), bg="white").pack(pady=(15, 5))
        self.comentario = tk.Text(frame, height=5, width=70, relief="sunken", bd=1)
        self.comentario.pack(pady=5)

        tk.Button(frame, text="Enviar Avaliação ✅", bg="#4CAF50", fg="white",
                  font=("Arial", 11, "bold"), relief="raised",
                  command=self.enviar_avaliacao).pack(pady=15)

    def enviar_avaliacao(self):
        nota = int(self.nota.get())
        comentario = self.comentario.get("1.0", "end-1c").strip()

        if not comentario:
            messagebox.showwarning("Aviso", "Por favor, insira um comentário sobre a receita.")
            return

        try:
            self.controller.avaliar(self.id_usuario, self.id_receita, nota, comentario)
            messagebox.showinfo("Sucesso", "✅ Avaliação registrada com sucesso!")
            self.janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar avaliação:\n{e}")
