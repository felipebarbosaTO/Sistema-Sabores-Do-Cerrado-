import tkinter as tk
from tkinter import messagebox
import webbrowser
from controller.receita_controller import ReceitaController


class AvaliacaoView:
    def __init__(self, id_usuario, id_receita, dados):
        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.id_receita = id_receita
        self.dados = dados

        self.janela = tk.Toplevel()
        self.janela.title(f"🍽️ Detalhes da Receita - {dados.get('nome', 'Sem Nome')}")
        self.janela.geometry("650x600")
        self.janela.configure(bg="white")

        frame = tk.Frame(self.janela, bg="white", bd=3, relief="ridge")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(frame, text=dados.get("nome", "Receita sem nome"), 
                 font=("Arial", 18, "bold"), bg="white").pack(pady=10)

        tk.Label(frame, text=f"Categoria: {dados.get('categoria', 'Não informada')}", 
                 font=("Arial", 12), bg="white").pack(pady=2)

        tk.Label(frame, text=f"Dificuldade: {dados.get('dificuldade', 'Não informada')}", 
                 font=("Arial", 12), bg="white").pack(pady=2)

        tk.Label(frame, text="Ingredientes:", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
        tk.Message(frame, text=dados.get("ingredientes", "Sem ingredientes cadastrados."),
                   width=500, bg="white", font=("Arial", 11)).pack(pady=3)

        tk.Label(frame, text="Modo de Preparo:", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
        tk.Message(frame, text=dados.get("modo_preparo", "Sem modo de preparo."),
                   width=500, bg="white", font=("Arial", 11)).pack(pady=3)

        if dados.get("link_imagem"):
            link_imagem = tk.Label(frame, text="📷 Ver Imagem", fg="blue", bg="white", cursor="hand2", font=("Arial", 11, "underline"))
            link_imagem.pack(pady=5)
            link_imagem.bind("<Button-1>", lambda e: webbrowser.open(dados["link_imagem"]))

        if dados.get("link_video"):
            link_video = tk.Label(frame, text="🎬 Ver Vídeo", fg="blue", bg="white", cursor="hand2", font=("Arial", 11, "underline"))
            link_video.pack(pady=5)
            link_video.bind("<Button-1>", lambda e: webbrowser.open(dados["link_video"]))

        tk.Label(frame, text="Avalie esta receita:", font=("Arial", 13, "bold"), bg="white").pack(pady=10)
        self.nota = tk.StringVar(value="5")
        notas = [("⭐ 1", "1"), ("⭐⭐ 2", "2"), ("⭐⭐⭐ 3", "3"), ("⭐⭐⭐⭐ 4", "4"), ("⭐⭐⭐⭐⭐ 5", "5")]
        for texto, valor in notas:
            tk.Radiobutton(frame, text=texto, variable=self.nota, value=valor, bg="white").pack(anchor="w")

        tk.Label(frame, text="Comentário:", font=("Arial", 12), bg="white").pack(pady=5)
        self.comentario = tk.Text(frame, height=4, width=60)
        self.comentario.pack(pady=5)

        tk.Button(frame, text="Enviar Avaliação", bg="#4CAF50", fg="white",
                  command=self.enviar_avaliacao).pack(pady=10)

    def enviar_avaliacao(self):
        """Envia avaliação do usuário"""
        nota = int(self.nota.get())
        comentario = self.comentario.get("1.0", "end-1c").strip()

        if not comentario:
            messagebox.showwarning("Aviso", "Por favor, insira um comentário sobre a receita.")
            return

        try:
            self.controller.avaliar(self.id_usuario, self.id_receita, nota, comentario)
            messagebox.showinfo("Sucesso", "Avaliação registrada com sucesso!")
            self.janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar avaliação: {e}")