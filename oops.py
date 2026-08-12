class Animal:
    def __init__(self , type):
        self.type = type
    
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def speak(self):
        return "Woof"

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")

    def speak(self):
        return "Meow"

class Duck(Animal):
    def __init__(self):
        super().__init__("Duck")

    def speak(self):
        return "Quack"

    def speak(self):
        return "opps"

class Parrot(Animal):
    def __init__(self):
        super().__init__("Parrot")


dog = Dog()
print(dog.speak())

cat = Cat()
print(cat.speak())

duck = Duck()
print(duck.speak())

parrot = Parrot()
print(parrot.speak())
