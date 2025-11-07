from model.conexao_model import Database

class FavoritosModel:
    def adicionar(id_usuario, id_receita):
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM favorito WHERE id_usuario=%s AND id_receita=%s", (id_usuario, id_receita))
        if cursor.fetchone():
            conn.close()
            return False
        cursor.execute("INSERT INTO favorito (id_usuario, id_receita) VALUES (%s, %s)", (id_usuario, id_receita))
        conn.commit()
        conn.close()
        return True