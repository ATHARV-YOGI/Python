class Employee:
    language = "Py"
    salary = 1200000




    def __init__(self): #dunder method which is automatically call
        print("i am creating an object")

    def getInfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")

    @staticmethod
    def greet():
        print("good ji")

# harry = Employee()
# harry.salary=34534

# rohan = Employee()

# harry.getInfo() # it converted into this ->Employee.getInfo(harry) so we have to always create formal parameters in the function 
# harry.greet()

harry = Employee()
harry.name = "harry"
print(harry.name, harry.salary)


