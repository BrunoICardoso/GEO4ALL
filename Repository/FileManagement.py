from DAO.DataBase import DataBase
from datetime import datetime

# Esse Repositorio da tabela FileManagement tem a função de ter todo qualquer comando que tem como função direta da tabela
class FileManagement(DataBase):

    def __init__(self):
        DataBase.__init__(self)

    def CheckExistingFile(self, file: str) -> None or int:
        # Essa função faz a verificação se o registgro exsite no banco dados se existe ele retorna o ID

        IDFile = self.Query("SELECT IDFile FROM FileManagement WHERE NomeArquivo = ?", file)
        if not IDFile:
            return None

        return IDFile[0]

    def Save(self, NomeArquivo: str, CreateFile: datetime, id=False) -> int:
        # id => Tem a resposabilidade de retornar o ID quando é TRUE ou apenas salva o registro

        if id:
            IDFile = self.Insert(
                "INSERT INTO FileManagement(NomeArquivo,CreateFile) OUTPUT inserted.IDFile VALUES(?,?)",
                (NomeArquivo, CreateFile), getID=True)
            return IDFile
        else:
            self.Insert("INSERT INTO FileManagement(NomeArquivo,CreateFile) VALUES(?,?)",
                        (NomeArquivo, CreateFile))
