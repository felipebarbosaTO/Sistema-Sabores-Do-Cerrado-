import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = "localhost"
        self.database = "Lista_receitas"
        self.user = "root"
        self.password = "turma@283"

    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                return connection
            print("[ERRO] Conexão não estabelecida.")
            return None
        except Error as e:
            print(f"[ERRO] Falha ao conectar ao MySQL: {e}")
            return None

    def execute_query(self, query, params=None):
        connection = self.get_connection()
        if not connection:
            print("[ERRO] Sem conexão ativa com o banco de dados.")
            return None

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params or ())

            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
            else:
                connection.commit()
                result = cursor.lastrowid

            cursor.close()
            connection.close()
            return result

        except Error as e:
            print(f"[ERRO SQL] {e}")
            return None
