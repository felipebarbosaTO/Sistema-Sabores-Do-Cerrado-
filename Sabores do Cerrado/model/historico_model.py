from model.conexao_model import Database
from datetime import datetime

class HistoricoModel:
    def registrar(id_usuario, id_receita):
        db = Database()
        conn = db.get_connection()
        if not conn:
            print("[ERRO] Falha ao conectar ao banco de dados para registrar histórico.")
            return

        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO historico (id_usuario, id_receita, data_visualizacao)
                VALUES (%s, %s, %s)
            """, (id_usuario, id_receita, datetime.now()))

            conn.commit()
            print(f"[OK] Histórico registrado para o usuário {id_usuario} e receita {id_receita}.")

        except Exception as e:
            print(f"[ERRO SQL] Falha ao registrar histórico: {e}")

        finally:
            cursor.close()
            conn.close()
