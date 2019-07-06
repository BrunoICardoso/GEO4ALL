from DAO.DataBase import DataBase
from datetime import datetime

# Esse Repositorio da tabela Pais tem a função de ter todo qualquer comando que tem como função direta da tabela
class Pais(DataBase):

    def __init__(self):
        DataBase.__init__(self)

    def CheckExistingPais(self, Nome) -> None or int:
        # Essa função faz a verificação se o registgro exsite no banco dados se existe ele retorna o ID

        IDPais = self.Query("SELECT IDPais FROM Paises WHERE Nome = ?", Nome)
        if not IDPais:
            return None

        return IDPais[0]

    def Save(self, Nome, Sigla, id=False) -> int:
        # id => Tem a resposabilidade de retornar o ID quando é TRUE ou apenas salva o registro

        if id:
            IDPais = self.Insert("INSERT INTO Paises (Nome,Sigla) OUTPUT inserted.IDPais VALUES(?,?)", (Nome, Sigla),
                                 getID=True)
            return IDPais

        else:
            self.Insert("INSERT INTO Paises (Nome,Sigla)VALUES(?,?)", (Nome, Sigla))
