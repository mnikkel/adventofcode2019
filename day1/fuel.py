with open('input') as f:
    modules = list(map(int, f.read().splitlines()))

def requiredFuel(mass):
    return mass // 3 - 2

masses = list(map(requiredFuel, modules))
print(sum(masses))

totalFuel = 0

for module in modules:
    fuel = requiredFuel(module)
    while fuel > 0:
        totalFuel += fuel
        fuel = requiredFuel(fuel)

print(totalFuel)
