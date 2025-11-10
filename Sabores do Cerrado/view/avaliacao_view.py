import tkinter as tk
from tkinter import messagebox
import webbrowser
from controller.receita_controller import ReceitaController

class AvaliacaoView:
    janela_aberta = None  # Impede abrir mais de uma janela

    def __init__(self, id_usuario, id_receita, dados):
        if AvaliacaoView.janela_aberta:
            messagebox.showinfo("Aviso", "Feche a receita atual antes de abrir outra.")
            return

        self.controller = ReceitaController()
        self.id_usuario = id_usuario
        self.id_receita = id_receita
        self.dados = dados

        self.janela = tk.Toplevel()
        AvaliacaoView.janela_aberta = self.janela
        self.janela.title(f"🍽️ Receita - {dados['nome']}")
        self.janela.geometry("750x650")
        self.janela.resizable(False, False)

        # Criar canvas para gradiente
        self.canvas = tk.Canvas(self.janela, width=750, height=650, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.criar_gradiente(self.canvas, "#FFA726", "#FFF8E1") 

        frame = tk.Frame(self.canvas, bg="white", bd=2, relief="solid")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=680, height=580)

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_janela)

        tk.Label(frame, text=dados["nome"], font=("Arial", 18, "bold"), bg="white", fg="#333",).pack(pady=(15, 10))
        tk.Label(frame, text=f"Categoria: {dados['categoria']}", font=("Arial", 12), bg="white").pack(pady=3)
        tk.Label(frame, text=f"Dificuldade: {dados['dificuldade']}", font=("Arial", 12), bg="white").pack(pady=3)

        tk.Label(frame, text="🧂 Ingredientes", font=("Arial", 14, "bold"), bg="white", fg="#4CAF50").pack(pady=(15, 3))
        self.texto(frame, dados["ingredientes"])

        tk.Label(frame, text="👨‍🍳 Modo de Preparo", font=("Arial", 14, "bold"), bg="white", fg="#FF7043").pack(pady=(15, 3))
        self.texto(frame, dados["modo_preparo"])

        links_frame = tk.Frame(frame, bg="white")
        links_frame.pack(pady=10)

        if dados["link_imagem"]:
            btn_imagem = tk.Button(links_frame, text=f"📷 Abrir Imagem", fg="blue", bg="white", cursor="hand2", font=("Arial", 10, "underline"), relief="flat", borderwidth=0, activebackground="white", activeforeground="darkblue", command=lambda url=dados["link_imagem"]: self.abrir_link(url))
            btn_imagem.pack(side="left", padx=10) 

        if dados["link_video"]:
            btn_video = tk.Button(links_frame, text=f"🎬 Abrir Vídeo",  fg="blue", bg="white", cursor="hand2", font=("Arial", 10, "underline"), relief="flat", borderwidth=0, activebackground="white", activeforeground="darkblue", command=lambda url=dados["link_video"]: self.abrir_link(url))
            btn_video.pack(side="left", padx=10)  

        avaliacao_frame = tk.Frame(frame, bg="white")
        avaliacao_frame.pack(pady=15, fill="x")

        tk.Label(avaliacao_frame, text="Avalie esta receita:", font=("Arial", 13, "bold"), bg="white").pack(pady=5)
        self.nota = tk.StringVar(value="5")

        estrelas = [("⭐ 1", "1"), ("⭐⭐ 2", "2"), ("⭐⭐⭐ 3", "3"), ("⭐⭐⭐⭐ 4", "4"), ("⭐⭐⭐⭐⭐ 5", "5")]
        estrelas_frame = tk.Frame(avaliacao_frame, bg="white")
        estrelas_frame.pack(pady=5)
        
        for texto, valor in estrelas:
            tk.Radiobutton(estrelas_frame, text=texto, variable=self.nota, value=valor, 
                          bg="white", font=("Arial", 10)).pack(side="left", padx=5)

        tk.Label(avaliacao_frame, text="Comentário:", font=("Arial", 12), bg="white").pack(pady=5)
        self.comentario = tk.Text(avaliacao_frame, height=4, width=65, font=("Arial", 10))
        self.comentario.pack(pady=(0, 10))

        btn_enviar = tk.Button(avaliacao_frame, text="Enviar Avaliação", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), relief="flat", bd=0, activebackground="#45a049", padx=20, pady=8, command=self.enviar_avaliacao)
        btn_enviar.pack(pady=10) 

    def abrir_link(self, url):
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            webbrowser.open_new_tab(url)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o link: {e}")

    def criar_gradiente(self, canvas, cor1, cor2):
        largura = 750
        altura = 650
        steps = 100
        r1, g1, b1 = canvas.winfo_rgb(cor1)
        r2, g2, b2 = canvas.winfo_rgb(cor2)
        r_ratio = (r2 - r1) / steps
        g_ratio = (g2 - g1) / steps
        b_ratio = (b2 - b1) / steps

        for i in range(steps):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            cor = f'#{nr >> 8:02x}{ng >> 8:02x}{nb >> 8:02x}'
            y1 = int(i * altura / steps)
            y2 = int((i + 1) * altura / steps)
            canvas.create_rectangle(0, y1, largura, y2, outline="", fill=cor)

    def texto(self, frame, conteudo):
        caixa = tk.Text(frame, height=4, width=65, wrap="word", font=("Arial", 10), bg="#fafafa", relief="flat")
        caixa.insert("1.0", conteudo)
        caixa.configure(state="disabled")
        caixa.pack(pady=3)

    def enviar_avaliacao(self):
        nota = int(self.nota.get())
        comentario = self.comentario.get("1.0", "end-1c").strip()

        if not comentario:
            messagebox.showwarning("Aviso", "Por favor, insira um comentário antes de enviar.")
            return

        try:
            self.controller.avaliar(self.id_usuario, self.id_receita, nota, comentario)
            messagebox.showinfo("Sucesso", "Avaliação registrada com sucesso!")
            self.fechar_janela()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar avaliação: {e}")

    def fechar_janela(self):
        if AvaliacaoView.janela_aberta == self.janela:
            AvaliacaoView.janela_aberta = None
        self.janela.destroy()