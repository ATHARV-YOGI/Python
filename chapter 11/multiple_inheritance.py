class Employee:
    company = "xyz"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"        
    def printLanguages(self):
        print(f"out of all the languages here is your language: {self.lang}")


class Programmer(Employee, Coder):
      company="abc"


a=Programmer()
a.name="ishan"
a.salary=3989834
a.lang="python"
a.show()
a.printLanguages()
