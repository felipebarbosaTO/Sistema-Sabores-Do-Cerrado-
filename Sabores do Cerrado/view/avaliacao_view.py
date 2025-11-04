import tkinter as tk
from tkinter import ttk, messagebox
from controller.receita_controller import ReceitaController

class AvaliacaoView:
    def __init__(self, id_usuario, id_receita, receita_dados):
        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.id_receita = id_receita

        top = tk.Toplevel()
        top.title("Detalhes da Receita")
        tk.Label(top, text=f"🍽️ {receita_dados[0]}", font=("Arial", 14, "bold")).pack(pady=5)
        tk.Label(top, text=f"⏱️ {receita_dados[1]}").pack()
        tk.Label(top, text=f"🧂 Ingredientes:\n{receita_dados[2]}", justify="left").pack(pady=5)
        tk.Label(top, text=f"👨‍🍳 Modo de preparo:\n{receita_dados[3]}", justify="left").pack(pady=5)

        tk.Label(top, text="⭐ Avalie (1 a 5):").pack()
        nota = ttk.Combobox(top, values=[1, 2, 3, 4, 5], state="readonly", width=5)
        nota.pack(pady=5)

        comentario = tk.Text(top, height=3, width=40)
        comentario.pack(pady=5)

        def salvar():
            if not nota.get():
                messagebox.showwarning("Aviso", "Selecione uma nota!")
                return
            self.controller.avaliar(id_usuario, id_receita, int(nota.get()), comentario.get("1.0", "end-1c"))
            messagebox.showinfo("Sucesso", "Avaliação e favorito registrados!")

        tk.Button(top, text="Salvar Avaliação", bg="#4CAF50", fg="white", command=salvar).pack(pady=10)