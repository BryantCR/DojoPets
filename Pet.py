class Pet:

    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise

    def sleep(self, energy):
        self.energy = self.energy + 25
        print(f"Before Sleep Method, Your energy is: {self.energy}")
        return self

    def eat(self, energy, health):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"Before Eat Method, Your health is: {self.health}")
        print(f"Before Eat Method, Your energy is: {self.energy}")
        return self

    def play(self, health):
        self.health = self.health + 10
        print(f"Before Play Method, Your health is: {self.health}")
        return self

    def noise():
        if type == "Cat":
            print("Miauuuuuuu")
            print(self.noise)
        elif type == "Dog":
            print("Guauuuuuuu")
        elif type == "Bird":
            print("Tuituitui")
        elif type == "Fish":
            print("Gluglugluglu")