#Classes are blueprints for creating objects
#classes have models and properties

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def move(self):
        print("Car Moves")
    
    def getMakeAndModel(self):
        print(f"I'm a {self.make} {self.model}")

firstCar = Vehicle("Tesla", "Model 3")

# print(firstCar.make)
# print(firstCar.model) instead of printing we 
firstCar.getMakeAndModel()
firstCar.move()

secondCar = Vehicle("Porsche", "Cayman Series")
secondCar.getMakeAndModel()

#Now let's talk about Inheritance

