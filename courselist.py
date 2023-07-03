from course import *
from professor import *
from classroom import *

class CourseList:

    def __init__(self) -> None:
        self.__list = []
        self.__count = 0
    
    @property
    def count(self) -> int:
        return self.__count
    
    def show(self) -> None:
        print("\n\n=== List of courses ===")
        for itm in self.__list:
            print(f"{itm}")
    
    def add(self, course: Course) -> bool:
        is_found = False
        for itm in self.__list:
            if itm.code == course.code:
                is_found = True
                break
        
        if is_found:
            print("Course already exists")
            return False

        self.__list.append(course)
        self.__count += 1
        return True

    def remove(self, code: str) -> bool:
        is_found = False
        index = -1

        print("Searching for course...")
        for idx, itm in enumerate(self.__list):
            if itm.code == code:
                is_found = True
                index = int(idx)
                break
        
        if not is_found:
            print(f"Course Code {code} NOT found")
            return False
        
        print(f"Removing item: {index}...")

        del self.__list[index]
        self.__count -= 1
        return True
