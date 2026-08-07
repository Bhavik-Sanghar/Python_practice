class Descriptor:
    def __get__(self,instance,owner):
        print(instance)
        print(owner)
        return "HIiiii"

class Test: 
    test = Descriptor()

obj = Test()
print(obj.test)