from model.conexao_model import connection

class FavoritosModel:
    def adicionar(id_usuario, id_receita):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM receitas_favoritas WHERE id_usuario=%s AND id_receita=%s", (id_usuario, id_receita))
        if cursor.fetchone():
            conn.close()
            return False
        cursor.execute("INSERT INTO receitas_favoritas (id_usuario, id_receita) VALUES (%s, %s)", (id_usuario, id_receita))
        conn.commit()
        conn.close()
        return True