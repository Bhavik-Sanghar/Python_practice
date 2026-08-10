class Count :
    def __init__(self):
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == 10:
            raise StopIteration
        self.current += 2
        return self.current 
            
        
for i in Count():
    print(i)