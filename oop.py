from types import MethodDescriptorType
class Dog:
    def bark(self):
        return f"Woof from {self}!"

buddy = Dog()


print(Dog.bark)

print(buddy.bark)


method = buddy.bark

print(method.__func__)
print(method.__self__)

