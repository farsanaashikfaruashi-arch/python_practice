class Student:
    def __init__(self, name, marks):
        self.name = name
        self._age = 20
        self.__marks = marks
    def get_marks(self):
        return self.__marks
s = Student("Asha", 90)
print(s.name)
print(s._age)
print(s.get_marks())
