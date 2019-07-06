import codecs
from decimal import *

# Essa Função Guarda toda a regra de extração dos arquivos data_points_20180101
# Conforme o algoritmo tem a função de guardar os valores como objeto como Latitude,Longitude,Distance,Bearing
# Tambem se percebe que faltava valores como por exemplo Latidade onde o algorismo faz dele um valor NULO
# Solução para problema dos valores restantes é quando um valor voltasse a repetir é nesse caso se salvaria aquele valor.
def ExtracDataPoint(file) -> list:
    DataCamp = {'Latitude': None, 'Longitude': None, 'Distance': None, 'Bearing': None}
    Campadd = {'Latitude': False, 'Longitude': False, 'Distance': False, 'Bearing': False}
    ListSave = []

    with codecs.open(file, "r", "utf-8") as readFileDataPoints:

        ListDataPoints = [line.replace("\n", "").replace("Bearing", "\nBearing") for line in readFileDataPoints]

        for line in ListDataPoints:
            linha = line.split("\n")

            for valor in linha:
                lista = valor.split(":")

                if lista[0] == "Latitude":

                    if not Campadd['Latitude']:
                        DataCamp['Latitude'] = Decimal(lista[1].replace("  ", "").lstrip().split()[1])
                        Campadd['Latitude'] = True

                    elif DataCamp['Latitude'] != None:
                        ListSave.append(DataCamp)
                        Latitude = Decimal(lista[1].replace("  ", "").lstrip().split()[1])
                        DataCamp = {'Latitude': Latitude, 'Longitude': None, 'Distance': None, 'Bearing': None}
                        Campadd = {'Latitude': True, 'Longitude': False, 'Distance': False, 'Bearing': False}

                    continue

                elif not Campadd['Latitude']:
                    Campadd['Latitude'] = True

                if lista[0] == "Longitude":
                    if not Campadd['Longitude'] or Campadd['Longitude'] == None:
                        DataCamp['Longitude'] = Decimal(lista[1].replace("  ", "").lstrip().split()[1])
                        Campadd['Longitude'] = True

                    elif DataCamp['Longitude'] != None:
                        ListSave.append(DataCamp)
                        Longitude = Decimal(lista[1].replace("  ", "").lstrip().split()[1])
                        DataCamp = {'Latitude': None, 'Longitude': Longitude, 'Distance': None, 'Bearing': None}
                        Campadd = {'Latitude': False, 'Longitude': True, 'Distance': False, 'Bearing': False}

                    continue

                elif not Campadd['Longitude']:
                    Campadd['Longitude'] = True

                if lista[0] == "Distance":

                    if not Campadd['Distance']:
                        DataCamp['Distance'] = lista[1].replace("  ", "").lstrip()
                        Campadd['Distance'] = True

                    elif DataCamp['Distance'] != None:
                        ListSave.append(DataCamp)
                        Distance = lista[1].replace("  ", "").lstrip()
                        DataCamp = {'Latitude': None, 'Longitude': None, 'Distance': Distance, 'Bearing': None}
                        Campadd = {'Latitude': False, 'Longitude': False, 'Distance': True, 'Bearing': False}

                    continue

                elif not Campadd['Distance']:
                    Campadd['Distance'] = True

                if lista[0] == "Bearing":
                    if not Campadd['Bearing'] or Campadd['Bearing'] == None:
                        DataCamp['Bearing'] = lista[1].replace("  ", "").lstrip()
                        Campadd['Bearing'] = True

                    elif DataCamp['Bearing'] != None:
                        ListSave.append(DataCamp)
                        Bearing = lista[1].replace("  ", "").lstrip()
                        DataCamp = {'Latitude': None, 'Longitude': None, 'Distance': None, 'Bearing': Bearing}
                        Campadd = {'Latitude': False, 'Longitude': False, 'Distance': False, 'Bearing': True}

                    continue

                elif not Campadd['Bearing']:
                    Campadd['Bearing'] = True

            if Campadd['Latitude'] and Campadd['Longitude'] and Campadd['Distance'] and Campadd['Bearing']:
                ListSave.append(DataCamp)
                DataCamp = {'Latitude': None, 'Longitude': None, 'Distance': None, 'Bearing': None}
                Campadd = {'Latitude': False, 'Longitude': False, 'Distance': False, 'Bearing': False}

    return ListSave
