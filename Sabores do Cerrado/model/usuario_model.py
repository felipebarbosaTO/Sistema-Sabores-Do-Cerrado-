from model.conexao_model import Database
import bcrypt

class UsuarioModel:
    def autenticar(email, senha):
        salt = bcrypt.gensalt(rounds=12) 
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        db = Database
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, nome, tipo_usuario FROM usuarios WHERE email=%s AND senha=%s", (email, senha_hash))
        user = cursor.fetchone()
        conn.close()
        return user

    def cadastrar(nome, email, senha, tipo_usuario="Usuário"):
        db = Database
        conn = db.get_connection()
        cursor = conn.cursor()
        salt = bcrypt.gensalt(rounds=12) 
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        try:
            cursor.execute("""
                INSERT INTO usuarios (nome, email, senha, tipo_usuario)
                VALUES (%s, %s, %s, %s)
            """, (nome, email, senha_hash, tipo_usuario))
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()