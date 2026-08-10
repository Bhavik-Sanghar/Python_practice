class Box:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("__add__ called")
        return NotImplemented

    def __radd__(self, other):
        print("__radd__ called")
        return f"{other} + {self.value}"

b = Box(10)

print(5 + b)

class User:
    def __str__(self):
        return "STR"

    def __repr__(self):
        return "REPR"

u = User()

print(u)
print(repr(u))
print([u])

class Test:
    def __enter__(self):
        print("Enter")
        return "Python"

    def __exit__(self, exc_type, exc, tb):
        print("Exit")
        print(exc_type)
        return False

with Test() as value:
    print(value)
    raise ValueError("Oops")