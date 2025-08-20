class Employee:
    salary = 100
    inc = 20

    @property
    def salaryAfterInc(self):
        return (self.salary + (self.inc/self.salary)*100)



    @salaryAfterInc.setter
    def salaryAfterInc(self, salary):
         self.inc = (salary - self.salary)*100/self.salary


e = Employee()
# print(e.salaryAfterInc)
e.salaryAfterInc =137
print(e.inc)
