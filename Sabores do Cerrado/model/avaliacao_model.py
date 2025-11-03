from model.conexao_model import connection

class AvaliacaoModel:
    def registrar(id_usuario, id_receita, nota, comentario):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO avaliacoes (id_receita, id_usuario, nota, comentario)
            VALUES (%s, %s, %s, %s)
        """, (id_receita, id_usuario, nota, comentario))
        conn.commit()
        conn.close()