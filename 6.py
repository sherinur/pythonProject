import os

class Employee:
    def __init__(self, name, id_number, department, job_title):
        """ constructor """
        self.__name = name
        self.__id_number = int(id_number)
        self.__department = department
        self.__job_title = job_title

    def __str__(self):
        return (f"Name: {self.__name}"
                f"\nID Number: {self.__id_number}"
                f"\nDepartment: {self.__department}"
                f"\nJob Title: {self.__job_title}")

def load_employees():
    if os.path.exists('employees.txt'):
        with open('employees.txt', 'r') as file:
            data = file.read()
            if data:

    return {}



def main():
    while(True):
        print("What would you like to do?: ")
        print("\n 1) Look up an employee in the dictionary"
              "\n 2) Add a new employee to the dictionary"
              "\n 3) Change an existing employee’s name, department, and job title in the dictionary"
              "\n 4) Delete an employee from the dictionary"
              "\n 5) Quit the program \n")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            return 0;

main()