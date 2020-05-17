fuel_sum = 0

modules = open("Modules", "r")
# print(modules.read())

def total_module_fuel():
    fuel_module = 0
    ledger = ((int(int(x) / 3)) - 2)
    fuel_module += ledger
    while ledger > 5:
        ledger = ((int(int(ledger) / 3)) - 2)
        fuel_module += ledger
    return fuel_module

for x in modules:
    fuel_sum += total_module_fuel()
    # print(total_module_fuel())


print(fuel_sum)
