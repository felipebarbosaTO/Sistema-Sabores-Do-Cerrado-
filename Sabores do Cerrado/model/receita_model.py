from model.conexao_model import connection

class ReceitaModel:
    def cadastrar(id_usuario, nome, tempo, ingredientes, modo):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO receitas (id_usuario, nome, tempo_preparo, ingredientes, modo_preparo)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_usuario, nome, tempo, ingredientes, modo))
        conn.commit()
        conn.close()

    def listar():
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_receita, nome FROM receitas")
        receitas = cursor.fetchall()
        conn.close()
        return receitas

    def buscar_por_id(id_receita):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, tempo_preparo, ingredientes, modo_preparo FROM receitas WHERE id_receita=%s", (id_receita,))
        dados = cursor.fetchone()
        conn.close()
        return dados
    
    def cadastrar(id_usuario, nome, tempo, ingredientes, modo, categoria, dificuldade, link_imagem=None, link_video=None):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO receitas (id_usuario, nome, tempo_preparo, ingredientes, modo_preparo, categoria, dificuldade, link_imagem, link_video)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (id_usuario, nome, tempo, ingredientes, modo, categoria, dificuldade, link_imagem, link_video))
        conn.commit()
        conn.close()

    def buscar_por_id(id_receita):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT nome, tempo_preparo, ingredientes, modo_preparo, categoria, dificuldade, link_imagem, link_video
            FROM receitas WHERE id_receita=%s
        """, (id_receita,))
        dados = cursor.fetchone()
        conn.close()
        return dados