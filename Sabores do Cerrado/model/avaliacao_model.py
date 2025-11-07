from model.conexao_model import Database

class AvaliacaoModel:
    def registrar(id_usuario, id_receita, nota, comentario):
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO avaliacao (id_receita, id_usuario, nota, comentario)
            VALUES (%s, %s, %s, %s)
        """, (id_receita, id_usuario, nota, comentario))
        conn.commit()
        conn.close()