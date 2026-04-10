from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Speed:", self.__speed)

    @abstractmethod
    def start(self):
        pass