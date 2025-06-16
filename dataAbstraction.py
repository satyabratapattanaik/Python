# Abstraction definition

class Car:
    
    def __init__(self):
        Car.acc = False
        Car.brk = False
        Car.clutch = False
        
    def start(self):
        Car.clutch = True
        Car.acc = True
        print("Car Started..")
        
car1 = Car()
car1.start()