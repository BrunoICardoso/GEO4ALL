from DAO.DataBase import DataBase
from datetime import datetime

# Esse Repositorio da tabela Points tem a função de ter todo qualquer comando que tem como função direta da tabela
class Points(DataBase):

    def __init__(self):
        DataBase.__init__(self)

    def CheckExistingPoint(self, latitude, longitude) -> None or int:
        # Essa função faz a verificação se o registgro exsite no banco dados se existe ele retorna o ID

        IDPoints = self.Query("SELECT IDPoints FROM Points WHERE Latitude = ? AND Logintude = ?", (latitude, longitude))
        if not IDPoints:
            return None

        return IDPoints[0]

    def Save(self, Latitude, Logintude, Distance, Bearing, IDFile, id=False) -> int:
        # id => Tem a resposabilidade de retornar o ID quando é TRUE ou apenas salva o registro

        if id:
            IDPoints = self.Insert(
                "INSERT INTO Points (Latitude,Logintude,Distance,Bearing,IDFile) OUTPUT inserted.IDPoints VALUES(?,?,?,?,?)",
                (Latitude, Logintude, Distance, Bearing, IDFile), getID=True)
            return IDPoints
        else:
            self.Insert("INSERT INTO Points (Latitude,Logintude,Distance,Bearing,IDFile)VALUES(?,?,?,?,?)",
                        (Latitude, Logintude, Distance, Bearing, IDFile))
