class Animal:
    def __init__(self, name, health):
        print(name + " is ALIVE! with an initial Health of " + str(health))
        self.name = name
        self.health = health
    def walk(self):
        self.health-=1
        print("WALK - Health decreased be 1 and is now:", self.health)        
        return self
    def run(self):
        self.health-=5
        print("RUN - Health decreased be 5 and is now:", self.health)
        return self
    def displayHealth(self):
        print("===================================")
        print("   Name: ", self.name)
        print(" Health: ", self.health)
        print("===================================")   

class Dog(Animal):
    def __init__(self, name, health=150):
        super().__init__(name, health)
    def pet(self):
        self.health+=5
        print("PET - Health increased be 5 and is now:", self.health)
        return self

class Dragon(Animal):
    def __init__(self, name, health=170):
        super().__init__(name, health)
    def fly(self):
        self.health+=10
        print("FLY - Health decreased be 10 and is now:", self.health)
        return self
    def displayHealth(self):
        super().displayHealth()
        print(" I am a Dragon")


# Do the things

monster = Animal("Sasquatch", 3000)
monster.walk().walk().walk().run().run().displayHealth()

dog = Dog("Corgi")
dog.walk().walk().walk().run().run().pet()
dog.displayHealth()

dog = Dog("Saint Bernard", 400)
dog.walk().walk().walk().run().run().pet()
dog.displayHealth()

hatchling = Dragon("Hatchling")
hatchling.fly().fly().run().walk().displayHealth()

#dog.fly() #should produce an error

