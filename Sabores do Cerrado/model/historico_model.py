from model.conexao_model import Database

class HistoricoModel:
    def registrar(id_usuario, id_receita):
        db = Database
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO historico_visualizacoes (id_usuario, id_receita) VALUES (%s, %s)", (id_usuario, id_receita))
        conn.commit()
        conn.close()