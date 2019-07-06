from DAO.DataBase import DataBase
from datetime import datetime

# Esse Repositorio da tabela Estado tem a função de ter todo qualquer comando que tem como função direta da tabela
class Estado(DataBase):

    def __init__(self):
        DataBase.__init__(self)

    def CheckExistingPais(self, Nome) -> None or int:
        # Essa função faz a verificação se o registgro exsite no banco dados se existe ele retorna o ID
        IDEstado = self.Query("SELECT IDEstado FROM Estados WHERE Nome = ?", Nome)
        if not IDEstado:
            return None

        return IDEstado[0]

    def Save(self, Nome, Sigla, IDPais, id=False) -> int:
        # id => Tem a resposabilidade de retornar o ID quando é TRUE ou apenas salva o registro

        if id:
            IDEstado = self.Insert("INSERT INTO Estados (Nome,Sigla,IDPais) OUTPUT inserted.IDEstado VALUES(?,?,?)",
                                   (Nome, Sigla, IDPais),
                                   getID=True)

            return IDEstado

        else:
            self.Insert("INSERT INTO Estados (Nome,Sigla,IDPais)VALUES(?,?,?)", (Nome, Sigla, IDPais))
