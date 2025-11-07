from model.conexao_model import Database
from datetime import date
import random


class CardapioModel:
    def gerar():
        try:
            db = Database()
            conn = db.get_connection()
            if conn is None:
                return ["❌ Erro: Não foi possível conectar ao banco de dados."]

            cursor = conn.cursor()

            cursor.execute("DELETE FROM cardapio WHERE data_cardapio = %s", (date.today(),))

            cursor.execute("SELECT id_receita FROM receita")
            todas = [row[0] for row in cursor.fetchall()]

            if not todas:
                cursor.close()
                conn.close()
                return ["⚠️ Nenhuma receita cadastrada para gerar o cardápio."]

            escolhidas = random.sample(todas, min(3, len(todas)))
            tipos = ["Café da Manhã", "Almoço", "Jantar"]

            for i, id_receita in enumerate(escolhidas):
                tipo = tipos[i % len(tipos)]
                cursor.execute("""
                    INSERT INTO cardapio (id_receita, data_cardapio, tipo_refeicao)
                    VALUES (%s, %s, %s)
                """, (id_receita, date.today(), tipo))

            conn.commit()

            cursor.execute("""
                SELECT receita.nome, cardapio.tipo_refeicao
                FROM cardapio
                JOIN receita ON receita.id_receita = cardapio.id_receita
                WHERE cardapio.data_cardapio = %s
            """, (date.today(),))

            lista = [f"{row[1]} → {row[0]}" for row in cursor.fetchall()]

            cursor.close()
            conn.close()
            print(f"[OK] Cardápio gerado com {len(lista)} receitas.")
            return lista or ["⚠️ Nenhuma receita encontrada."]
        except Exception as e:
            print(f"[ERRO] Falha ao gerar cardápio: {e}")
            return [f"Erro ao gerar cardápio: {e}"]
