class Employee:
    company = "xyz"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company="abc"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good with {self.showLanguage} language")
        




class Programmer(Employee):
    company="abc"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.showLanguage} language")


a = Employee()
a.name="ashish"
a.salary= 87877
b = Programmer()
b.name="ishan"
b.salary=87877878
a.show()
b.show()



