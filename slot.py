class Test : 
    __slots__ = ("name",)
    def __init__(self,name : str):
        self.name = name
        print(name)

obj = Test("Bhavik")

print(obj.name)
print(Test.__dict__)