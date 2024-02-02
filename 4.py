class Employee:
    def __init__(self, name, id_number, department, job_title):
        """ constructor """
        self.__name = name
        self.__id_number = int(id_number)
        self.__department = department
        self.__job_title = job_title

    def __str__(self):
        return f"Name: {self.__name}\nID Number: {self.__id_number}\nDepartment: {self.__department}\nJob Title: {self.__job_title}"

employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print("Employee 1:")
print(employee1)
print("\nEmployee 2:")
print(employee2)
print("\nEmployee 3:")
print(employee3)