# Polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    return "running!"

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    return "Sail!"

class Plane(Vehicle):
  def move(self):
    return "Fly!"

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  move=x.move()
  print(f"Brand name {x.brand}, Model name is {x.model} is move {move}")
