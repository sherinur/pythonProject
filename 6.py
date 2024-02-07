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
            return data
    return {}

def look_up(employees):
    id_number = input("Enter the employee's ID number: ")
    found = False
    for employee_info in employees.split('\n'):
        if id_number in employee_info:
            print("Employee is found:", employee_info)
            found = True
            break
    if not found:
        print("Employee not found.")

def add_employee(employees):
    name = input("Enter the employee's name: ")
    id_number = input("Enter the employee's ID number: ")
    department = input("Enter the department of the employee: ")
    job_title = input("Enter the job title of the employee: ")

    text = name + " " + id_number + " " + department + " " + job_title
    with open('employees.txt', 'a') as file:
        file.write(str(text) + "\n")

def main():
    while(True):
        employees = load_employees()
        print("What would you like to do?: ")
        print("\n 1) Look up an employee in the dictionary"
              "\n 2) Add a new employee to the dictionary"
              "\n 3) Change information of the employee"
              "\n 4) Delete an employee from the dictionary"
              "\n 5) Quit the program \n")

        choice = input("Enter your choice: ")

        if choice == '1':
            look_up(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            change_employee_details(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            save_employees(employees)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
