import tkinter as tk
from tkinter import messagebox
from controller.receita_controller import ReceitaController
from view.avaliacao_view import AvaliacaoView

class LoginView:
    def __init__(self, id_usuario, nome):
        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.nome = nome

        self.janela = tk.Toplevel()
        self.janela.title("🍽️ Sabores do Cerrado - Usuário")
        self.janela.geometry("800x600")
        self.janela.configure(bg="#FAFAFA")

        container = tk.Frame(self.janela, bg="white", bd=2, relief="ridge", padx=12, pady=12)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text=f"Bem-vindo, {self.nome}!", font=("Arial", 16, "bold"), bg="white", fg="#333").grid(row=0, column=0, columnspan=3, pady=(0,10))

        tk.Label(container, text="Receitas disponíveis:", bg="white", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
        self.lista = tk.Listbox(container, width=45, height=12, bd=1, relief="sunken")
        self.lista.grid(row=2, column=0, rowspan=6, padx=(0,12), pady=5)

        btn_frame = tk.Frame(container, bg="white")
        btn_frame.grid(row=2, column=1, sticky="n")

        tk.Button(btn_frame, text="Ver Receita", bg="#2196F3", fg="white", width=18,
                  command=self.ver_receita).pack(pady=6)
        tk.Button(btn_frame, text="Gerar Cardápio", bg="#9C27B0", fg="white", width=18,
                  command=self.cardapio).pack(pady=6)
        tk.Button(btn_frame, text="Atualizar Lista", bg="#607D8B", fg="white", width=18,
                  command=self.atualizar_lista).pack(pady=6)
        tk.Button(btn_frame, text="Fechar", bg="#B00020", fg="white", width=18,
                  command=self.janela.destroy).pack(pady=6)

        self.status = tk.Label(container, text="", bg="white", font=("Arial", 10))
        self.status.grid(row=8, column=0, columnspan=2, pady=(10,0))

        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        try:
            receitas = self.controller.listar() or []
            for r in receitas:
                if isinstance(r, (list, tuple)) and len(r) >= 2:
                    self.lista.insert(tk.END, f"{r[0]} - {r[1]}")
            self.status.config(text=f"Receitas carregadas: {self.lista.size()}", fg="#333")
        except Exception as e:
            self.status.config(text=f"Erro ao listar receitas: {e}", fg="red")

    def ver_receita(self):
        selecao = self.lista.curselection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma receita antes de visualizar.")
            return

        try:
            id_receita = int(self.lista.get(selecao[0]).split(" - ")[0])
        except Exception:
            messagebox.showerror("Erro", "Seleção inválida.")
            return

        dados = self.controller.detalhes(self.id_usuario, id_receita)
        if not dados:
            messagebox.showerror("Erro", "Não foi possível carregar os detalhes da receita.")
            return

        AvaliacaoView(self.id_usuario, id_receita, dados)

    def cardapio(self):
        try:
            lista = self.controller.gerar_cardapio()
            if not lista:
                messagebox.showinfo("Cardápio do Dia", "Nenhum item encontrado para o cardápio.")
                return
            messagebox.showinfo("Cardápio do Dia", "\n".join(lista))
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao gerar cardápio: {e}")
