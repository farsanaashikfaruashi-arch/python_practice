class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
Dog().sound()
Cat().sound()
