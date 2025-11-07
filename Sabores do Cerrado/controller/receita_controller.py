from model.receita_model import ReceitaModel
from model.historico_model import HistoricoModel
from model.favoritos_model import FavoritosModel
from model.avaliacao_model import AvaliacaoModel
from model.cardapio_model import CardapioModel
from model.conexao_model import Database


class ReceitaController:
    def autenticar_usuario(self, nome, senha):
        db = Database()
        query = """
            SELECT id_usuario, nome, tipo_usuario
            FROM usuario
            WHERE nome = %s AND senha = %s
        """
        try:
            resultado = db.execute_query(query, (nome, senha))
            if resultado and len(resultado) > 0:
                return resultado[0]
            return None
        except Exception as e:
            print(f"Erro ao autenticar usuário: {e}")
            return None

    def cadastrar(
        self,
        id_usuario,
        nome,
        ingredientes,
        modo,
        categoria,
        dificuldade,
        link_imagem=None,
        link_video=None
    ):
     
        try:
            ReceitaModel.cadastrar(
                id_usuario, nome, ingredientes, modo,
                categoria, dificuldade, link_imagem, link_video
            )
        except Exception as e:
            print(f"Erro ao cadastrar receita: {e}")

    def listar(self):
        try:
            return ReceitaModel.listar()
        except Exception as e:
            print(f"Erro ao listar receitas: {e}")
            return []

    def detalhes(self, id_usuario, id_receita):
        try:
            HistoricoModel.registrar(id_usuario, id_receita)
            return ReceitaModel.buscar_por_id(id_receita)
        except Exception as e:
            print(f"Erro ao buscar detalhes da receita: {e}")
            return None

    def avaliar(self, id_usuario, id_receita, nota, comentario):
        try:
            AvaliacaoModel.registrar(id_usuario, id_receita, nota, comentario)
            FavoritosModel.adicionar(id_usuario, id_receita)
        except Exception as e:
            print(f"Erro ao registrar avaliação: {e}")

    def gerar_cardapio(self):
        try:
            return CardapioModel.gerar()
        except Exception as e:
            print(f"Erro ao gerar cardápio: {e}")
            return []
