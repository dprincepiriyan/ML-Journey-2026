class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        #self.__age=age  # private attribute
    def move(self):
        print("drive")
class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("sail")
class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("fly")
car1 = car("Toyota", "Corolla")
boat1 = boat("Yamaha", "242X")
plane1 = plane("Boeing", "747")
for x in (car1, boat1, plane1):
    x.move()  # Calls the move method of each object

class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private attribute
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative")
p1 = person("Alice", 30)
print(p1.name)  # Accessing public attribute
print(p1.get_age())  # Accessing private attribute via getter
p1.set_age(35)      # Modifying private attribute via setter
print(p1.get_age())  # Accessing updated age
    