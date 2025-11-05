from model.receita_model import ReceitaModel
from model.historico_model import HistoricoModel
from model.favoritos_model import FavoritosModel
from model.avaliacao_model import AvaliacaoModel
from model.cardapio_model import CardapioModel
from model.conexao_model import Database

class ReceitaController:

    def autenticar_usuario(self, nome, senha):
        db=Database()
        query = ""
        resultado = db.execute_query(query, (nome, senha))
        if resultado:
            return resultado[0]
        return None

    def cadastrar(self, id_usuario, nome, tempo, ingredientes, modo):
        ReceitaModel.cadastrar(id_usuario, nome, tempo, ingredientes, modo)

    def listar(self):
        return ReceitaModel.listar()

    def detalhes(self, id_usuario, id_receita):
        HistoricoModel.registrar(id_usuario, id_receita)
        return ReceitaModel.buscar_por_id(id_receita)

    def avaliar(self, id_usuario, id_receita, nota, comentario):
        AvaliacaoModel.registrar(id_usuario, id_receita, nota, comentario)
        FavoritosModel.adicionar(id_usuario, id_receita)

    def gerar_cardapio(self):
        return CardapioModel.gerar()