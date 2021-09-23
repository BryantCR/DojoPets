class Pet:

    def __init__(self, name, typePet, tricks, health, energy, noise):
        self.name = name
        self.typePet = typePet
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.pnoise = noise

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy = self.energy + 25
        print(f"Before Sleep Method, Your energy is: {self.energy}")
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"Before Eat Method, Your health is: {self.health}")
        print(f"Before Eat Method, Your energy is: {self.energy}")
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health = self.health + 5
        print(f"Before Play Method, Your health is: {self.health}")
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print(self.pnoise)
        return self