from DAO.DataBase import DataBase
from datetime import datetime

# Esse Repositorio da tabela Logradouro tem a função de ter todo qualquer comando que tem como função direta da tabela
class Logradouro(DataBase):

    def __init__(self):
        DataBase.__init__(self)

    def CheckExistingLogradouro(self, Rua, Numero, bairro, CEP) -> None or int:
        # Essa função faz a verificação se o registgro exsite no banco dados se existe ele retorna o ID

        IDLogradouro = self.Query(
            "SELECT IDLogradouro FROM Logradouros WHERE Rua = ? AND Numero = ? AND bairro = ? AND CEP = ?",
            (Rua, Numero, bairro, CEP))

        if not IDLogradouro:
            return None

        return IDLogradouro[0]

    def Save(self, Rua, Numero, bairro, CEP, IDCidade, id=False) -> int:
        # id => Tem a resposabilidade de retornar o ID quando é TRUE ou apenas salva o registro

        if id:
            IDLogradouro = self.Insert(
                "INSERT INTO Logradouros (Rua,Numero,bairro,CEP,IDCidade) OUTPUT inserted.IDLogradouro VALUES(?,?,?,?,?)",
                (Rua, Numero, bairro, CEP, IDCidade), getID=True)

            return IDLogradouro
        else:
            self.Insert("INSERT INTO Logradouros (Rua,Numero,bairro,CEP,IDCidade)VALUES(?,?,?,?,?)",
                        (Rua, Numero, bairro, CEP, IDCidade))
