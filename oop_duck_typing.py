class Dog:
    def speak(self):
        print("Bark")
class Cat:
    def speak(self):
        print("Meow")
class Robot:
    def speak(self):
        print("Beep")
def make_it_speak(obj):
    obj.speak()
make_it_speak(Dog())
make_it_speak(Cat())
make_it_speak(Robot())
