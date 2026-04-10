from Car import Car
from bike import Bike

car1 = Car("Toyota", 180, "Petrol")
bike1 = Bike("Yamaha", 120, 150)

car1.show_details()
car1.start()
car1.fuel()

print("------------------")

bike1.show_details()
bike1.start()
bike1.engine()