from Pet import Pet

class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"Walk method will execute play method")
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"Feed method will execute eat method")
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"bathe method will execute noise method")
        self.pet.noise()
        return self
    