from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def start(self):
        print("Car starts with key ignition")

    def fuel(self):
        print("Fuel Type:", self.fuel_type)