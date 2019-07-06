import logging
import pyodbc
from urllib import parse


# Classe criada para toda conficuração da DataBase e manipulação do Banco de Dados
class DataBase:

    def __init__(self):

        self._server = 'DESKTOP-2S1L854\SQLEXPRESS'
        self._database = 'Geo'
        self._username = 'root'
        self._password = 'root'

        try:

            self._conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self._server + ';DATABASE=' + self._database + ';UID=' + self._username + ';PWD=' + self._password)
            self._cur = self._conn.cursor()

        except pyodbc.Error as excpt:
            logging.critical('%s', excpt)

    @property
    def SERVER(self):
        return self._server

    @property
    def DATABASE(self):
        return self._database

    @property
    def USERNAME(self):
        return self._username

    @property
    def PASSWORD(self):
        return self._password

    @property
    def CONN(self):
        return self._conn

    @CONN.deleter
    def CONN(self):
        self._conn.close()

    @property
    def CUR(self):
        return self._cur

    def Query(self, query, params=None, fetchall=False):
        # Query -> parametro tem a função de trazer comando da SQL
        # Param -> param é oocional mas se quiser atribuir para query ele funciona de forma que alimente os paramtro da query
        # ferchall quando é FALSE serve para trazer um registro ou True para varios registros

        try:
            if fetchall:
                if params:
                    return self.CUR.execute(query, params).fetchall()

                return self.CUR.execute(query).fetchall()

            else:
                if params:
                    return self.CUR.execute(query, params).fetchone()

                return self.CUR.execute(query).fetchone()

        except Exception as e:
            logging.critical("Erro na Query: %s", e)
            logging.critical("Query: %s", query)
            logging.critical("param: %s", params)

    def Insert(self, query, params=None, getID=False):
        # Query-> parametro tem a função de trazer comando da SQL
        # params -> param é oocional mas se quiser atribuir para query ele funciona de forma que alimente os paramtro da query
        # GetID -> Serve para trazer ID quando salva um registro Mas essa condição so vai funcionar se a Query estiver com sintaxe INSERT TABELA(COLUNAS) OUTPUT inserted.COLUNA Values()

        global id
        try:
            if params:
                self.CUR.execute(query, params)

                if getID:
                    id = self.CUR.fetchval()

            else:
                self.CUR.execute(query)

                if getID:
                    id = self.CUR.fetchval()

        except Exception as e:
            logging.critical("erro inserção do banco: %s", e)
            self.CONN.rollback()

        else:
            self.CONN.commit()
            if getID:
                return id

    def Update(self, query, params, getID=False):
        # Query-> parametro tem a função de trazer comando da SQL
        # params -> param é oocional mas se quiser atribuir para query ele funciona de forma que alimente os paramtro da query
        # GetID -> Serve para trazer ID quando salva um registro Mas essa condição so vai funcionar se a Query estiver com sintaxe Update TABELA(COLUNAS) OUTPUT inserted.COLUNA Values()

        global id
        try:
            if params:
                self.CUR.execute(query, params)

                if getID:
                    id = self.CUR.fetchval()
            else:
                self.CUR.execute(query)

                if getID:
                    id = self.CUR.fetchval()

        except Exception as e:
            logging.critical("erro na atualização no banco: %s", e)
            self.CONN.rollback()

        else:
            self.CONN.commit()

            if getID:
                return id
