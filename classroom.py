class Classroom:

    def __init__(self, location: str, building: str) -> None:
        self.__location = location
        self.__building = building
    
    def __str__(self) -> str:
        return f"{self.__location} [{self.__building}]"

    @property
    def location(self) -> str:
        return self.__location
    
    @location.setter
    def location(self, value: str) -> None:
        self.__location = value
    
    @property
    def building(self) -> str:
        return self.__building
    
    @building.setter
    def building(self, value: str) -> None:
        self.__building = value
