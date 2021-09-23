from Ninja import Ninja
from Pet import Pet

petCat = Pet("Naranjo", "Cat", "sleep", 100, 100, "Miauuuu")
ninjaEsteban = Ninja("Esteban", "Mora", petCat, "Osos", "Catfood")

print(ninjaEsteban)
print(ninjaEsteban.pet)
ninjaEsteban.walk()
print(petCat)
print(petCat.typePet)
petCat.noise()
