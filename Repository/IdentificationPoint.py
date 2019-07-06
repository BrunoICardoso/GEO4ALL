from DAO.DataBase import DataBase
from datetime import datetime


# Esse Repositorio da tabela IdentificationPoint tem a função de ter todo qualquer comando que tem como função direta da tabela
class IdentificationPoint(DataBase):

    def __init__(self):
        DataBase.__init__(self)

    def CheckExistingLogradouro(self, IDPoints, IDPais, IDEstado, IDCidades, IDLogradouro) -> None or int:
        # Essa função faz a verificação se o registgro exsite no banco dados se existe ele retorna o ID

        IDGeo = self.Query(
            "SELECT IDGeo FROM IdentificationPoint WHERE IDPoints = ? AND IDPais = ? AND IDEstado = ? AND IDCidades = ? AND IDLogradouro = ?",
            (IDPoints, IDPais, IDEstado, IDCidades, IDLogradouro))

        if not IDGeo:
            return None

        return IDGeo[0]

    def Save(self, IDPoints, IDPais, IDEstado, IDCidades, IDLogradouro, id=False) -> int:
        # id => Tem a resposabilidade de retornar o ID quando é TRUE ou apenas salva o registro

        if id:
            IDGeo = self.Insert(
                "INSERT INTO IdentificationPoint (IDPoints,IDPais,IDEstado,IDCidades,IDLogradouro) OUTPUT inserted.IDGeo VALUES(?,?,?,?,?)",
                (IDPoints, IDPais, IDEstado, IDCidades, IDLogradouro), getID=True)

            return IDGeo

        else:
            self.Insert(
                "INSERT INTO IdentificationPoint (IDPoints,IDPais,IDEstado,IDCidades,IDLogradouro)VALUES(?,?,?,?,?)",
                (IDPoints, IDPais, IDEstado, IDCidades, IDLogradouro))

    def VisualizacaoFINAL(self):
        return self.Query(
            """SELECT po.Latitude, 
           po.Logintude, 
           lo.Rua, 
           lo.Numero, 
           lo.bairro,
           ci.Nome, 
           lo.CEP, 
           es.Nome as Estado, 
           pa.Nome as Pais 
    FROM IdentificationPoint ident
    INNER JOIN Points po  on po.IDPoints = ident.IDPoints
    INNER JOIN Paises pa  on pa.IDPais = ident.IDPais
    INNER JOIN Estados es on es.IDEstado = ident.IDEstado
    INNER JOIN Cidades ci on ci.IDCidade = ident.IDCidades
    INNER JOIN Logradouros lo on lo.IDLogradouro = ident.IDLogradouro""", fetchall=True)
