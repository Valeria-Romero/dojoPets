class Pet:

    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type =  type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.noise} I'm full!")

    def play(self):
        self.health += 5
        print(f"{self.name} looks very happy!")

    def noise(self):
        print(self.noise)