class Professor:

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.__name = name
        self.__phone = phone
        self.__email = email
    
    def __str__(self) -> str:
        return f"{self.__name} [{self.__phone}] ({self.__email})"

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def phone(self) -> str:
        return self.__phone
    
    @phone.setter
    def phone(self, value: str) -> None:
        self.__phone = value
    
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        self.__email = value

