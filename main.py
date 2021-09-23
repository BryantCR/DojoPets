from Pet import Pet
from Ninja import Ninja


petCat = Pet("Naranjo", "Cat", "sleep")
petDog = Pet("Zeus", "Dog", "Eat")

ninjaEsteban = Ninja("Esteban", "Mora", petCat, "Osos", "Catfood")
ninjaMaria = Ninja("Maria", "Gomez", petDog, "Tortillas", "Dogfood")

#print(ninjaEsteban)
ninjaMaria.walk().feed().bathe()
ninjaEsteban.walk().feed().bathe()
petCat.noise()
petCat.play().eat().sleep()

