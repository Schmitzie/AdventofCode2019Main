# mass = 0
# module = 0
# fuel = ((int(mass/3))-2)
fuelSum = 0

modules = open("Modules", "r")
# print(modules.read())
for x in modules:
    fuel = ((int(int(x)/3))-2)
    fuelSum += fuel
print(fuelSum)