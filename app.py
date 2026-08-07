class BankAccount:
    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance
    
    def get_balance(self):
        return f'**************************\nOwner : {self.owner}\nBalance : {self.balance}\n**************************'
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return f'**************************\nOwner : {self.owner} \nDeposit amount : {amount} \nBalance : {self.balance}\n**************************'
    
    def withdraw(self,amount):
        if amount > self.balance: return f'**************************\nOwner : {self.owner} \nInsuffient Balance :(\n**************************'
        else :
            self.balance = self.balance - amount
            return f'**************************\nOwner : {self.owner} \nWithdrawl amount : {amount} \nBalance : {self.balance}\n**************************'


account_1 = BankAccount("Bhavik" , 5000)
account_2 = BankAccount("Akshay" , 500)

print(account_1.get_balance())
# Make a deposit in in account 1 of 2k
print(account_1.deposit(2000))
# Withdraw 4k from account 1  
print(account_1.withdraw(2000))


# Withdraw more money then avalibe in account 2 
print(account_2.withdraw(1000))



# -------------------------------------------------------------------------------------------------------
# BuildWrite a Student class — has name, grades list.

# - Methods: add_grade(), average(), is_passing()

class Student:
    design = "*-*-*-*-*-*-*-*-*-*"
    def __init__(self,name : str,grades: list):
        self.name = name
        self.grades = grades
    
    def add_grade(self,grade : int):
        self.grade = grade
        self.grades.append(grade)
        return f'{self.design}\nGrade Added to {self.name}\nGrades : {self.grades}'
    
    def average(self):
        total = sum(self.grades)
        length = len(self.grades)
        return f'{self.design}\nAverage Grade of {self.name} : {total/length}'
    
    def is_passing(self,passing_mark : int = 75):
        self.passing_mark = passing_mark
        is_pass = "Pass" if sum(self.grades)/len(self.grades) > passing_mark else "Fail"
        return f'{self.design}\n{self.name} {is_pass} in Exam'
    

student1 = Student("Bhavik" , [50,70,55,100])

# Avg of student 1
print(student1.average())
# Check if pass or not
print(student1.is_passing(60)) 


# Add Grade in list
print(student1.add_grade(99))
print(student1.average())
print(student1.is_passing())




        


        


        
