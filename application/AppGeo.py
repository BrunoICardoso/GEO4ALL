import pandas as pd
import numpy as np
import logging
import time
from datetime import datetime
from Download.PathFolderDownload import PathDownload
from Useful.File import Files
from Useful.GoogleMaps import GoogleMaps
from RN.ETLDataPoints import ExtracDataPoint
from Repository.FileManagement import FileManagement
from Repository.Cidade import Cidade
from Repository.Estado import Estado
from Repository.IdentificationPoint import IdentificationPoint
from Repository.Logradouro import Logradouro
from Repository.Pais import Pais
from Repository.Points import Points

#Apenas executar esse arquivo, já está tudo configurado para extrair os arquivos e coletar.
def ExtractGeo():
    # Essa Função tem objecto da extração da aplicação em volta do projeto
    # Onde tem toda a validação de não repetir valores e salvar os valores no banco de dados
    # Configurações de parametro de Banco ficam no arquivo /DAO/DataBase
    # CHave GoogleMaps continuara Ativa até 01/08/2019

    path = PathDownload()
    file = Files(directory=path)
    maps = GoogleMaps(ApiKey='AIzaSyBOfvtPquH05kbxAlnSo4eJoLdHGuP3lZk', language='pt-BR')

    fileManagement = FileManagement()
    points = Points()
    pais = Pais()
    estado = Estado()
    cidade = Cidade()
    logradouro = Logradouro()
    identificationPoint = IdentificationPoint()

    ListFile = file.ReturnExtractTazGz(url='https://s3.amazonaws.com/dev.etl.python/datasets/data_points.tar.gz')

    for filedatapoints in ListFile:

        if not fileManagement.CheckExistingFile(filedatapoints):
            IDFile = fileManagement.Save(NomeArquivo=filedatapoints, CreateFile=datetime.now(), id=True)

            for datapoint in ExtracDataPoint(filedatapoints):

                if datapoint['Latitude'] != None and datapoint['Longitude'] != None:

                    if not points.CheckExistingPoint(datapoint['Latitude'], datapoint['Longitude']):
                        IDPoint = points.Save(Latitude=datapoint['Latitude'], Logintude=datapoint['Longitude'],
                                              Distance=datapoint['Distance'], Bearing=datapoint['Bearing'],
                                              IDFile=IDFile,
                                              id=True)

                        coordenadas = (datapoint['Latitude'], datapoint['Longitude'])
                        maps.SearchGeoCode(coordenadas)

                        IDPais = pais.CheckExistingPais(maps.CountryLong)
                        if not IDPais:
                            IDPais = pais.Save(Nome=maps.CountryLong, Sigla=maps.CountryShort, id=True)

                        IDEstado = estado.CheckExistingPais(maps.StateLong)
                        if not IDEstado:
                            IDEstado = estado.Save(Nome=maps.StateLong, Sigla=maps.StateShort, IDPais=IDPais, id=True)

                        IDCidade = cidade.CheckExistingCidade(maps.City)
                        if not IDCidade:
                            IDCidade = cidade.Save(Nome=maps.City, IDEstado=IDEstado, id=True)

                        IDlogradouro = logradouro.CheckExistingLogradouro(maps.Street, maps.Number, maps.District,
                                                                          maps.PostalCode)
                        if not IDlogradouro:
                            IDlogradouro = logradouro.Save(Rua=maps.Street, Numero=maps.Number, bairro=maps.District,
                                                           CEP=maps.PostalCode, IDCidade=IDCidade, id=True)

                        IDGeo = identificationPoint.CheckExistingLogradouro(IDPoint, IDPais, IDEstado, IDCidade,
                                                                            IDlogradouro)
                        if not IDGeo:
                            identificationPoint.Save(IDPoint, IDPais, IDEstado, IDCidade, IDlogradouro)

                        logging.info("%s %s - %s - %s %s - %s %s - %s ", maps.Street, maps.Number, maps.District,
                                     maps.StateLong, maps.StateShort, maps.CountryLong, maps.CountryShort,
                                     maps.PostalCode)


    result = identificationPoint.VisualizacaoFINAL()
    logging.info("%s",result)

    # df = pd.DataFrame(data=np.asarray(result),
    #                   columns=['Latitude', 'Logintude', 'Rua', 'Numero', 'bairro', 'Cidade', 'CEP', 'Estado', 'Pais'])
    # print(df.head())


if __name__ == '__main__':
    start_time = time.time()
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

    ExtractGeo()

    logging.info("Tempo de execução do script: %s segundos" % (time.time() - start_time))
    logging.info("Script executado com sucesso!")
