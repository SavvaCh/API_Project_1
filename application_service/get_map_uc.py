from domain.map_params import MapParams
from services.i_map__service import IMapService


class GetMapUseCase:
    def __init__(self, map_service: IMapService):
        self.map_service = map_service

    def execute(self, param: MapParams):
        return self.map_service.get_map(param.get_longitude(), param.get_latitude(),
                                        param.get_zoom())
