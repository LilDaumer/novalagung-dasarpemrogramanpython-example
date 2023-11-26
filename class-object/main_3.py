# %% A.31.3. Property ➜ Attribute

class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0

car1 = Car()
print(f"car1 name: {car1.name}")
print(f"car1 manufacturer: {car1.manufacturer}")
print(f"car1 year: {car1.year}")

# %%

car1 = Car()
print(f"instance object: {car1}, type: {type(car1)}")
car1.name = "M3 GTR"
car1.manufacturer = "BMW"
car1.year = 2001
print(f"Car name: {car1.manufacturer} {car1.name}\nYear released: {car1.year}\n")

car2 = Car()
car2.name = "RX-8"
car2.manufacturer = "Mazda"
car2.year = 2002
print(f"Car name: {car2.manufacturer} {car2.name}\nYear released: {car2.year}\n")

car3 = Car()
car3.name = "Le Mans Quattro"
car3.manufacturer = "Audi"
car3.year = 2003
print(f"Car name: {car3.manufacturer} {car3.name}\nYear released: {car3.year}\n")
