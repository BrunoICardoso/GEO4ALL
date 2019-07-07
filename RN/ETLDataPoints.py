import codecs
from decimal import *


# Essa Classes Guarda toda a regra de extração dos arquivos "data_points_"
# Conforme o algoritmo tem a função de guardar os valores como objeto como Latitude,Longitude,Distance,Bearing
# Tambem se percebe que faltava valores como por exemplo Latidade onde o algorismo faz dele um valor NULO
# Solução para problema dos valores restantes é quando um valor voltasse a repetir é nesse caso se salvaria aquele valor.

class DataPoint:

    def __init__(self, latitude: Decimal = None, longitude: Decimal = None, distance: str = None, bearing: str = None):
        self._latitude = latitude
        self._longitude = longitude
        self._distance = distance
        self._bearing = bearing

    @property
    def Latitude(self):
        return self._latitude

    @Latitude.setter
    def Latitude(self, latitude):
        self._latitude = latitude

    @property
    def Longitude(self):
        return self._longitude

    @Longitude.setter
    def Longitude(self, longitude):
        self._longitude = longitude

    @property
    def Distance(self):
        return self._distance

    @Distance.setter
    def Distance(self, distance):
        self._distance = distance

    @property
    def Bearing(self):
        return self._bearing

    @Bearing.setter
    def Bearing(self, bearing):
        self._bearing = bearing


class ValidateDataPoint:

    def __init__(self, latitude: bool = False, longitude: bool = False, distance: bool = False, bearing: bool = False):
        self._latitude = latitude
        self._longitude = longitude
        self._distance = distance
        self._bearing = bearing

    @property
    def Latitude(self):
        return self._latitude

    @Latitude.setter
    def Latitude(self, latitude):
        self._latitude = latitude

    @property
    def Longitude(self):
        return self._longitude

    @Longitude.setter
    def Longitude(self, longitude):
        self._longitude = longitude

    @property
    def Distance(self):
        return self._distance

    @Distance.setter
    def Distance(self, distance):
        self._distance = distance

    @property
    def Bearing(self):
        return self._bearing

    @Bearing.setter
    def Bearing(self, bearing):
        self._bearing = bearing


class ETL:

    def ExtracDataPoint(self,file) -> list:

        dataPoint = DataPoint()
        validateDataPoint = ValidateDataPoint()
        ListSave = []

        with codecs.open(file, "r", "utf-8") as readFileDataPoints:

            ListDataPoints = [line.replace("\n", "").replace("Bearing", "\nBearing") for line in readFileDataPoints]

            for line in ListDataPoints:
                linha = line.split("\n")

                for valor in linha:
                    lista = valor.split(":")

                    if lista[0] == "Latitude":

                        if not validateDataPoint.Latitude:
                            dataPoint.Latitude = Decimal(lista[1].replace("  ", "").lstrip().split()[1])
                            validateDataPoint.Latitude = True

                        elif dataPoint.Latitude != None:

                            ListSave.append(dataPoint)
                            Latitude = Decimal(lista[1].replace("  ", "").lstrip().split()[1])

                            dataPoint = DataPoint(latitude=Latitude)
                            validateDataPoint = ValidateDataPoint(latitude=True)

                        continue

                    elif not validateDataPoint.Latitude:
                        validateDataPoint.Latitude = True

                    if lista[0] == "Longitude":

                        if not validateDataPoint.Longitude:
                            dataPoint.Longitude = Decimal(lista[1].replace("  ", "").lstrip().split()[1])
                            validateDataPoint.Longitude = True

                        elif dataPoint.Longitude != None:

                            ListSave.append(dataPoint)
                            Longitude = Decimal(lista[1].replace("  ", "").lstrip().split()[1])

                            dataPoint = DataPoint(longitude=Longitude)
                            validateDataPoint = ValidateDataPoint(longitude=True)

                        continue

                    elif not validateDataPoint.Longitude:
                        validateDataPoint.Longitude = True

                    if lista[0] == "Distance":

                        if not validateDataPoint.Distance:
                            dataPoint.Distance = lista[1].replace("  ", "").lstrip()
                            validateDataPoint.Distance = True

                        elif dataPoint.Distance != None:

                            ListSave.append(dataPoint)
                            Distance = lista[1].replace("  ", "").lstrip()

                            dataPoint = DataPoint(distance=Distance)
                            validateDataPoint = ValidateDataPoint(distance=True)

                        continue

                    elif not validateDataPoint.Distance:
                        validateDataPoint.Distance = True

                    if lista[0] == "Bearing":

                        if not validateDataPoint.Bearing:
                            dataPoint.Bearing = lista[1].replace("  ", "").lstrip()
                            validateDataPoint.Bearing = True

                        elif dataPoint.Bearing != None:
                            ListSave.append(dataPoint)
                            Bearing = lista[1].replace("  ", "").lstrip()

                            dataPoint = DataPoint(bearing=Bearing)
                            validateDataPoint = ValidateDataPoint(bearing=True)

                        continue

                    elif not validateDataPoint.Bearing:
                        validateDataPoint.Bearing = True

                if validateDataPoint.Latitude and validateDataPoint.Longitude and validateDataPoint.Distance and validateDataPoint.Bearing:
                    ListSave.append(dataPoint)
                    dataPoint = DataPoint()
                    validateDataPoint = ValidateDataPoint()

        return ListSave
