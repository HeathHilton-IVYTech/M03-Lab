# Heath Hilton
# 11/13/2022

# Program: M03 Lab: List, Functions, and Classes

# A program to be an example for Super Classes.

class Vehicle:
  def __init__(self, type):
    self.type = type


class Automobile(Vehicle):
  def __init__(self, type, year, make, model, doors, roof):
    super().__init__(type)
    self.year = year
    self.make = make
    self.model = model
    self.doors = doors
    self.roof = roof


vType = input("Type of Vehicle: ")
vYear = input("Enter the year: ")
vMake = input("Enter manufacture: ")
vModel = input("Enter the model: ")
vDoors = input("Enter the Number of doors(2 or 4): ")
vRoof = input("Enter type of roof (solid or sun roof): ")

vehicle_1 = Automobile(vType, vYear, vMake, vModel, vDoors, vRoof)

print("\nVehicle Specifications ...")
print("Vehicle Type:", vehicle_1.type)
print("Year:", vehicle_1.year)
print("Make:", vehicle_1.make)
print("Model:", vehicle_1.model)
print("Number of Doors:", vehicle_1.doors)
print("Type of Roof:", vehicle_1.roof)