class PersonalData:
    def __init__(self, name, address, age, phone_number):
        """ constructor """
        self.__name = name
        self.__address = address
        self.__age = int(age)
        self.__phone_number = phone_number

    """ getters and setters """
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

my_data = PersonalData("Sheri Nurislam", "Kabanbai batyr 50", 18, "+7 777 777 77 77")
friend1_data = PersonalData("Joe Biden", "White House", 74, "+7 666 666 66 66")
friend2_data = PersonalData("Ernar Bukembaya", "Whiskey Hotel", 18, "+7 235 123 12 52")