from model.conexao_model import Database

class ReceitaModel:
    def cadastrar(id_usuario, nome, ingredientes, modo, categoria, dificuldade, link_imagem=None, link_video=None):
        db = Database()  
        conn = db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO receita (
                id_usuario, nome, ingredientes, modo_preparo, categoria, dificuldade, link_imagem, link_video
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (id_usuario, nome, ingredientes, modo, categoria, dificuldade, link_imagem, link_video))

        conn.commit()
        cursor.close()
        conn.close()

    def listar():
        db = Database()  
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_receita, nome FROM receita order by id_receita DESC")
        receitas = cursor.fetchall()
        cursor.close()
        conn.close()
        return receitas

    def buscar_por_id(id_receita):
        db = Database()  
        conn = db.get_connection()
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