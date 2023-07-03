from professor import *
from classroom import *

class Course:

    def __init__(self, code: str, description: str, start: str, end: str) -> None:
        self.__code = code
        self.__description = description
        self.__start = start
        self.__end = end
        self.__professor = None
        self.__classroom = None
    
    def __str__(self) -> str:
        return f"[{self.__code}] {self.__description} ({self.__start} - {self.__end}) | professor: {self.__professor} | classroom: {self.__classroom}"
    
    '''
    Code is read-only
    '''
    @property
    def code(self) -> str:
        return self.__code
    
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value
    
    @property
    def start(self) -> str:
        return self.__start
    
    @start.setter
    def start(self, value: str) -> None:
        self.__start = value
    
    @property
    def end(self) -> str:
        return self.__end
    
    @end.setter
    def end(self, value: str) -> None:
        self.__end = value
    
    @property
    def professor(self) -> str:
        return f"{self.__professor}"
    
    def update_professor(self, name: str, phone: str, email: str) -> None:
        self.__professor = Professor(name, phone, email)
    
    @property
    def classroom(self) -> str:
        return f"{self.__classroom}"
    
    def update_classroom(self, location: str, building: str) -> None:
        self.__classroom = Classroom(location, building)