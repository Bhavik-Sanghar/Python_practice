class Z:
    def greet(self):
        print("Z")
        
class Y:
    def greet(self):
        print("Y")

class A:
    def greet(self):
        print("A")

class B(A,Z):
    def greet(self):
        super().greet()
        print("B")

class C(Y,A):   
    def greet(self):
        super().greet()
        print("C")

class D(B, C):
    def greet(self):
        super().greet()
        print("D")

D().greet()
print(D.__mro__)
