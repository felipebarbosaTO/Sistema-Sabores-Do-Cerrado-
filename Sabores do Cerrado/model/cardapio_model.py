from conexao_model import Database
from datetime import date
import random

class CardapioModel:
    def gerar():
        db = Database
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cardapio WHERE data_cardapio=%s", (date.today(),))
        cursor.execute("SELECT id_receita FROM receitas")
        todas = [r[0] for r in cursor.fetchall()]
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
            SELECT receitas.nome, cardapio.tipo_refeicao 
            FROM cardapio 
            JOIN receitas ON receitas.id_receita = cardapio.id_receita
            WHERE data_cardapio=%s
        """, (date.today(),))
        lista = [f"{r[1]}: {r[0]}" for r in cursor.fetchall()]
        conn.close()
        return lista