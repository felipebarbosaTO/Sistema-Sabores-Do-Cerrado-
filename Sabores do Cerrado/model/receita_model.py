from model.conexao_model import Database

class ReceitaModel:
    def cadastrar(id_usuario, nome, ingredientes, modo, categoria, dificuldade, link_imagem=None, link_video=None):
        db = Database()
        conn = db.get_connection()
        if not conn:
            print("[ERRO] Falha ao conectar ao banco para cadastrar receita.")
            return

        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO receita (
                    id_usuario, nome, ingredientes, modo_preparo, 
                    categoria, dificuldade, link_imagem, link_video
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (id_usuario, nome, ingredientes, modo, categoria, dificuldade, link_imagem, link_video))
            
            conn.commit()
            print(f"[OK] Receita '{nome}' cadastrada com sucesso.")
        except Exception as e:
            print(f"[ERRO SQL] Falha ao cadastrar receita: {e}")
        finally:
            cursor.close()
            conn.close()

    def listar():
        db = Database()
        conn = db.get_connection()
        if not conn:
            print("[ERRO] Falha ao conectar ao banco para listar receitas.")
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT id_receita, nome FROM receita ORDER BY id_receita DESC")
        receitas = cursor.fetchall()
        cursor.close()
        conn.close()
        return receitas

    def buscar_por_id(id_receita):
        db = Database()
        conn = db.get_connection()
        if not conn:
            print("[ERRO] Falha ao conectar ao banco para buscar receita.")
            return None

        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                id_receita, nome, ingredientes, modo_preparo, 
                categoria, dificuldade, link_imagem, link_video
            FROM receita
            WHERE id_receita = %s
        """, (id_receita,))
        dados = cursor.fetchone()
        cursor.close()
        conn.close()
        return dados
