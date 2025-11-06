from model.conexao_model import Database
from datetime import datetime

class HistoricoModel:
    def registrar(id_usuario, id_receita):
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO historico (id_usuario, id_receita, data_visualizacao) VALUES (%s, %s, %s)", (id_usuario, id_receita, datetime.now()))
        conn.commit()
        cursor.close()
        conn.close()