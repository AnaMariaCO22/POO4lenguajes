from car import Car
from account import Account

if __name__=="_main_":
    print("Hola Mundo")

    car=Car("AMS234", Account("Andres Herrera","Andres Herrera"))
    print(vars(car))
    print(vars(car.driver))