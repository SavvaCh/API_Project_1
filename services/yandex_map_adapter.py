import requests

from services.i_map__service import IMapService


class YandexMapAdapter(IMapService):
    map_request = "http://static-maps.yandex.ru/1.x/"

    def get_map(self, longitude, latitude, zoom):
        return requests.get(self.map_request, params={"ll": str(longitude) + "," + str(latitude),
                                                      "z": zoom,
                                                      "l": "map"}).content
