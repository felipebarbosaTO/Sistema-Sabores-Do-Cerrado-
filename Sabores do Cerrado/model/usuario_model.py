from model.conexao_model import Database
import bcrypt

class UsuarioModel:
    def autenticar(email, senha):
        db = Database()
        conn = db.get_connection()
        if not conn:
            print("[ERRO] Falha na conexão ao autenticar usuário.")
            return None

        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id_usuario, nome, senha, tipo_usuario FROM usuario WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user:
            return None  

        senha_hash = user["senha"].encode("utf-8")
        if bcrypt.checkpw(senha.encode("utf-8"), senha_hash):
            return {
                "id_usuario": user["id_usuario"],
                "nome": user["nome"],
                "tipo_usuario": user["tipo_usuario"]
            }
        else:
            return None

    def cadastrar(nome, email, senha, tipo_usuario="usuario"):
        db = Database()
        conn = db.get_connection()
        if not conn:
            print("[ERRO] Falha na conexão ao cadastrar usuário.")
            return False

        cursor = conn.cursor()

        try:
            senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt(rounds=12))

            cursor.execute("""
                INSERT INTO usuario (nome, email, senha, tipo_usuario)
                VALUES (%s, %s, %s, %s)
            """, (nome, email, senha_hash, tipo_usuario))
            conn.commit()
            print(f"[OK] Usuário '{nome}' cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"[ERRO SQL] Falha ao cadastrar usuário: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
