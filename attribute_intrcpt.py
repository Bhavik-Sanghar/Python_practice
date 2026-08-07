class Student:
    def __init__(self):
        self.name = "Bhavik"

    def __getattribute__(self, attr):
        print("Searching:", attr)
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        print("Missing:", attr)
        return "Unknown"

s = Student()

print(s.name)
print(s.age)

#    obj.name
#       │
#       ▼
# __getattribute__()
#       │
#       ▼
# Data Descriptor?
#       │
#       ▼
# Instance __dict__?
#       │
#       ▼
# Non-Data Descriptor?
#       │
#       ▼
# Class Attribute?
#       │
#       ▼
# Parent Classes (MRO)?
#       │
#       ▼
# __getattr__?
#       │
#       ▼
# AttributeError