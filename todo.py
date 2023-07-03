class ToDo:

    PRIORITY_URGENT = 'urgent'
    PRIORITY_INTERMIDIEATE = 'intermediate'
    PRIORITY_OPTIONAL = 'optional'

    CATEGORY_PERSONAL = "Personal"
    CATEGORY_ACADEMIC = "Academic"
    CATEGORY_WORK = "Work"
    CATEGORY_LEISURE = "Leisure"

    def __init__(self, description, due_date, priority) -> None:
        self.__description = description
        self.__due_date = due_date
        self.__priority = priority
    
    def __str__(self) -> str:
        return f"{self.__description} - {self.__due_date} - {self.__priority}"

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, update_description):
        self.__description = update_description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @due_date.setter
    def due_date(self, update_due_date):
        self.__due_date = update_due_date
    
    @property
    def priority(self):
        return self.__priority
    
    @priority.setter
    def priority(self, value):
        self.__priority = value
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, value):
        self.__category = value

