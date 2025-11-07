from model.conexao_model import Database

class FavoritosModel:
    def adicionar(id_usuario, id_receita):
        db = Database()
        conn = db.get_connection()

        if not conn:
            print("[ERRO] Falha ao conectar ao banco de dados.")
            return False

        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT 1 FROM favorito WHERE id_usuario = %s AND id_receita = %s",
                (id_usuario, id_receita)
            )

            if cursor.fetchone():
                print("[INFO] Receita já está nos favoritos.")
                return False

            cursor.execute(
                "INSERT INTO favorito (id_usuario, id_receita) VALUES (%s, %s)",
                (id_usuario, id_receita)
            )
            conn.commit()
            print("[OK] Receita adicionada aos favoritos.")
            return True

        except Exception as e:
            print(f"[ERRO SQL] Falha ao adicionar favorito: {e}")
            return False

        finally:
            cursor.close()
            conn.close()
