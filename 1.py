class Pet():
    def __init__(self, name, animal_type, age):
        """ constructor """
        self.__name = name
        self.__animal_type = animal_type
        self.__age = int(age)

    """ getter method """
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    """ setter method """
    def set_name(self, name):
        self.__name = name

    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age


name = input("What is name of your pet? ")
type = input("What type of your pet? ")
age = input("How old is your pet? ")

pet1 = Pet(name, type, age)

print(pet1.get_name())
print(pet1.get_type())
print(pet1.get_age())