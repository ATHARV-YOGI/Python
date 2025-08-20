class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow!")


d = Dog()        
d.bark()
