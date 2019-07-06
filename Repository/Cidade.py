from DAO.DataBase import DataBase
from datetime import datetime

# Esse Repositorio da tabela CIDADE tem a função de ter todo qualquer comando que tem como função direta da tabela
class Cidade(DataBase):

    def __init__(self):
        DataBase.__init__(self)

    def CheckExistingCidade(self, Nome) -> None or int:
        # Essa função faz a verificação se o registgro exsite no banco dados se existe ele retorna o ID

        IDCidade = self.Query("SELECT IDCidade FROM Cidades WHERE Nome = ?", Nome)
        if not IDCidade:
            return None

        return IDCidade[0]

    def Save(self, Nome, IDEstado, id=False) -> int:
        #id => Tem a resposabilidade de retornar o ID quando é TRUE ou apenas salva o registro

        if id:
            IDCidade = self.Insert("INSERT INTO Cidades (Nome,IDEstado) OUTPUT inserted.IDCidade VALUES(?,?)",
                                   (Nome, IDEstado), getID=True)
            return IDCidade

        else:
            self.Insert("INSERT INTO Cidades (Nome,IDEstado)VALUES(?,?)", (Nome, IDEstado))
