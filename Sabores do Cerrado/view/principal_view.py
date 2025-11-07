import tkinter as tk
from tkinter import messagebox, ttk
from controller.receita_controller import ReceitaController
from view.avaliacao_view import AvaliacaoView

class PrincipalView:
    def __init__(self, id_usuario, nome):
        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.nome = nome

        self.janela = tk.Toplevel()
        self.janela.title("🍽️ Sabores do Cerrado - Administrador")
        self.janela.geometry("1000x700")
        self.janela.configure(bg="#FAFAFA")

        main = tk.Frame(self.janela, bg="white", bd=2, relief="ridge", padx=14, pady=14)
        main.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(main, text=f"Painel Admin — {self.nome}", font=("Arial", 18, "bold"), bg="white", fg="#333").grid(row=0, column=0, columnspan=3, pady=(0,12))

        tk.Label(main, text="Nome da Receita:", bg="white").grid(row=1, column=0, sticky="w")
        self.nome_r = tk.Entry(main, width=40)
        self.nome_r.grid(row=2, column=0, pady=4, sticky="w")

        tk.Label(main, text="Ingredientes:", bg="white").grid(row=3, column=0, sticky="w")
        self.ingr_r = tk.Text(main, width=50, height=6, bd=1, relief="sunken")
        self.ingr_r.grid(row=4, column=0, pady=4, sticky="w")

        tk.Label(main, text="Modo de Preparo:", bg="white").grid(row=5, column=0, sticky="w")
        self.modo_r = tk.Text(main, width=50, height=6, bd=1, relief="sunken")
        self.modo_r.grid(row=6, column=0, pady=4, sticky="w")

        tk.Label(main, text="Categoria:", bg="white").grid(row=7, column=0, sticky="w")
        self.categoria = tk.Entry(main, width=25)
        self.categoria.grid(row=8, column=0, pady=4, sticky="w")

        tk.Label(main, text="Dificuldade:", bg="white").grid(row=9, column=0, sticky="w")
        self.combo_dificuldade = ttk.Combobox(main, values=["Fácil", "Médio", "Difícil"], state="readonly", width=12)
        self.combo_dificuldade.grid(row=10, column=0, pady=4, sticky="w")

        tk.Label(main, text="Link da Imagem:", bg="white").grid(row=11, column=0, sticky="w")
        self.link_imagem = tk.Entry(main, width=40)
        self.link_imagem.grid(row=12, column=0, pady=4, sticky="w")

        tk.Label(main, text="Link do Vídeo:", bg="white").grid(row=13, column=0, sticky="w")
        self.link_video = tk.Entry(main, width=40)
        self.link_video.grid(row=14, column=0, pady=4, sticky="w")

        action_frame = tk.Frame(main, bg="white")
        action_frame.grid(row=15, column=0, pady=10, sticky="w")
        tk.Button(action_frame, text="Cadastrar Receita", bg="#4CAF50", fg="white", width=18, command=self.cadastrar).pack(side="left", padx=6)
        tk.Button(action_frame, text="Gerar Cardápio", bg="#9C27B0", fg="white", width=18, command=self.cardapio).pack(side="left", padx=6)

        tk.Label(main, text="Receitas cadastradas:", bg="white").grid(row=1, column=1, sticky="w", padx=(20,0))
        self.lista = tk.Listbox(main, width=40, height=20, bd=1, relief="sunken")
        self.lista.grid(row=2, column=1, rowspan=10, padx=(20,0), pady=4, sticky="n")

        list_btn_frame = tk.Frame(main, bg="white")
        list_btn_frame.grid(row=12, column=1, pady=8)
        tk.Button(list_btn_frame, text="Ver Receita", bg="#2196F3", fg="white", width=16, command=self.ver_receita).pack(side="left", padx=6)
        tk.Button(list_btn_frame, text="Atualizar Lista", bg="#607D8B", fg="white", width=16, command=self.atualizar_lista).pack(side="left", padx=6)
        tk.Button(list_btn_frame, text="Fechar", bg="#B00020", fg="white", width=16, command=self.janela.destroy).pack(side="left", padx=6)

        self.status = tk.Label(main, text="", bg="white", font=("Arial", 10))
        self.status.grid(row=16, column=0, columnspan=2, pady=(8,0))

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

    def cadastrar(self):
        nome = self.nome_r.get().strip()
        ingredientes = self.ingr_r.get("1.0", "end-1c").strip()
        modo = self.modo_r.get("1.0", "end-1c").strip()
        categoria = self.categoria.get().strip()
        dificuldade = self.combo_dificuldade.get().strip()
        link_imagem = self.link_imagem.get().strip() or None
        link_video = self.link_video.get().strip() or None

        if not nome or not ingredientes or not modo:
            messagebox.showwarning("Aviso", "Preencha nome, ingredientes e modo de preparo.")
            return

        try:
            self.controller.cadastrar(
                nome,
                ingredientes,
                modo,
                categoria,
                dificuldade,
                link_imagem,
                link_video
            )
            messagebox.showinfo("Sucesso", "Receita cadastrada com sucesso!")
            self.limpar_campos()
            self.atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar receita: {e}")

    def limpar_campos(self):
        self.nome_r.delete(0, tk.END)
        self.ingr_r.delete("1.0", "end")
        self.modo_r.delete("1.0", "end")
        self.categoria.delete(0, tk.END)
        self.combo_dificuldade.set("")
        self.link_imagem.delete(0, tk.END)
        self.link_video.delete(0, tk.END)

    def ver_receita(self):

        selecao = self.lista.curselection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma receita para visualizar.")
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
