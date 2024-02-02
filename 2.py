class Car():
    def __init__(self, year_model, make):
        """ Constructor """
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    """ Getter method """
    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    """ Setter method """
    def set_year_model(self, year):
        self.__year_model = year

    def set_make(self, make):
        self.__make_ = make

    def set_speed(self, speed):
        self.__speed_ = speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5


year_model = input("Enter your year model: ")
make = input("Enter your make")
car = Car(year_model, make)

for i in range(5):
    car.accelerate()
    print(car.get_speed())

for j in range(5):
    car.brake()
    print(car.get_speed())