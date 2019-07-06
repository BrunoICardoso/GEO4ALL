from googlemaps.client import Client
from googlemaps.geocoding import reverse_geocode

# Essa classe tem a função de refletir a resposta do corpo da pagina do google maps API
class BodyMaps:

    def __init__(self):
        self._number = None
        self._street = None
        self._postalcode = None
        self._city = None
        self._statelong = None
        self._stateshort = None
        self._countrylong = None
        self._countryshort = None

    @property
    def Number(self) -> int:
        return self._number

    @Number.setter
    def Number(self, number: int):
        self._number = number

    @property
    def Street(self) -> str:
        return self._street

    @Street.setter
    def Street(self, street: str):
        self._street = street

    @property
    def PostalCode(self) -> str:
        return self._postalcode

    @PostalCode.setter
    def PostalCode(self, postalcode: str):
        self._postalcode = postalcode

    @property
    def District(self) -> str:
        return self._district

    @District.setter
    def District(self, district: str):
        self._district = district

    @property
    def City(self) -> str:
        return self._city

    @City.setter
    def City(self, city: str):
        self._city = city

    @property
    def StateLong(self) -> str:
        return self._statelong

    @StateLong.setter
    def StateLong(self, statelong: str):
        self._statelong = statelong

    @property
    def StateShort(self) -> str:
        return self._stateshort

    @StateShort.setter
    def StateShort(self, stateshort: str):
        self._stateshort = stateshort

    @property
    def CountryLong(self) -> str:
        return self._countrylong

    @CountryLong.setter
    def CountryLong(self, countrylong: str):
        self._countrylong = countrylong

    @property
    def CountryShort(self) -> str:
        return self._countryshort

    @CountryShort.setter
    def CountryShort(self, countryshort: str):
        self._countryshort = countryshort

# Essa classe tem a função de fazer a conexão com a API GOOGLE MAPS onde é usado a bibliote googlemaps
class GoogleMaps(BodyMaps):

    def __init__(self, ApiKey, language):
        self._client = Client(ApiKey)
        self._language = language
        BodyMaps.__init__(self)

    @property
    def ClientMap(self):
        return self._client

    @ClientMap.setter
    def ClientMap(self, client):
        self._client = client

    @property
    def Language(self):
        return self._language

    @Language.setter
    def Language(self, language):
        self._language = language

    def SearchGeoCode(self, coordinates:tuple):
        #Coordinates -> São as cordenadas da Latitude e Longitude que passado por uma Tupla
        # Essa função tem a resposabilidade de refletir o corpo da pagina do googlemaps api apenas o componentes de endereço

        result = reverse_geocode(client=self.ClientMap, latlng=coordinates, language=self.Language)

        if len(result) > 0:
            for components in result[0]['address_components']:

                if any(elem in components['types'] for elem in ['street_number']):
                    self.Number = components['long_name']

                elif any(elem in components['types'] for elem in ['route']):
                    self.Street = components['long_name']

                elif any(elem in components['types'] for elem in ['postal_code']):
                    self.PostalCode = components['long_name']

                elif any(elem in components['types'] for elem in ['sublocality', 'sublocality_level_1']):
                    self.District = components['long_name']

                elif any(elem in components['types'] for elem in ['administrative_area_level_2']):
                    self.City = components['long_name']

                elif any(elem in components['types'] for elem in ['administrative_area_level_1']):
                    self.StateLong = components['long_name']
                    self.StateShort = components['short_name']

                elif any(elem in components['types'] for elem in ['country']):
                    self.CountryLong = components['long_name']
                    self.CountryShort = components['short_name']
