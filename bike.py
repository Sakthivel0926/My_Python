from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, brand, speed, engine_cc):
        super().__init__(brand, speed)
        self.engine_cc = engine_cc

    def start(self):
        print("Bike starts with self-start button")

    def engine(self):
        print("Engine:", self.engine_cc, "CC")