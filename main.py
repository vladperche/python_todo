from courselist import *

class Main:

    C_LINE_SIZE = 60
    C_LINE_SINGLE = "-" * C_LINE_SIZE
    C_LINE_DOUBLE = "=" * C_LINE_SIZE

    def __init__(self) -> None:
        self.__courselist = CourseList()
        
    def start(self):
        while True:
            Main.__print_main_menu()

            c = input("choose one option:")
            if(c == "99"):
                break
            elif(c == "1"):
                self.todoMenu()
            elif(c == "2"):
                self.courseMenu()
    
    '''
    TODO OPERATIONS
    '''
    def todoMenu(self) -> None:
        while True:
            Main.__print_todo_menu()
            
            c = input("choose one option:")
            if(c == "99"):
                break
    
    def todoShow() -> None:
        pass
    
    '''
    COUSE OPERATIONS
    '''
    def courseMenu(self) -> None:
        while True:
            Main.__print_course_menu()

            c = input("choose one option:")
            if(c == "99"):
                break
            elif(c == "1"):
                self.courseShow()
            elif(c == "2"):
                self.courseAdd()
            elif(c == "3"):
                self.courseRemove()
    
    def courseShow(self) -> None:
        if(self.__courselist.count == 0):
            print("\n\n*** The list has no elements ***")
        else:
            self.__courselist.show()
            print(f"{Main.C_LINE_SINGLE}\n")
    
    def courseAdd(self) -> None:
        code = input("\nCourse Code:")
        name = input("Course Description:")
        course = Course(code, name, None, None)
        if(not self.__courselist.add(course)):
           return
        
        course.start = input("Course start time:")
        course.end = input("Course end time:")

        p_name = input("Professor name:")
        p_phone = input("Professor Phone:")
        p_email = input("Professor email:")
        course.update_professor(p_name, p_phone, p_email)

        c_name = input("Classroom Location:")
        c_build = input("Classroom Building:")
        course.update_classroom(c_name, c_build)
    
    def courseRemove(self) -> None:
        code = input("\nCourse Code:")
        self.__courselist.remove(code)
    
    '''
    STATIC METHODS
    '''
    @staticmethod
    def __print_main_menu():
        print(f"\n\n{Main.C_LINE_DOUBLE}")
        print("=== MAIN  MENU")
        print(f"{Main.C_LINE_DOUBLE}")
        print("1. ToDo Menu")
        print("2. Course Menu")
        print("99. EXIT")
    
    @staticmethod
    def __print_todo_menu():
        print(f"\n\n{Main.C_LINE_DOUBLE}")
        print("=== TODO MENU")
        print(f"{Main.C_LINE_DOUBLE}")
        print("1. Show ToDo List")
        print("2. Add ToDo Item")
        print("3. Remove ToDo Item")
        print("4. Update ToDo Item")
        print("5. Clear ToDo List")
        print("99. EXIT")
    
    @staticmethod
    def __print_course_menu():
        print(f"\n\n{Main.C_LINE_DOUBLE}")
        print("=== TODO MENU")
        print(f"{Main.C_LINE_DOUBLE}")
        print("1. Show Course List")
        print("2. Add Course Item")
        print("3. Remove Course Item")
        print("99. EXIT")
    

main = Main()
main.start()
