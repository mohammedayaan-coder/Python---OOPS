class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

animal = Dog("pup")

print(animal.alive)
animal.eat()
animal.sleep()


