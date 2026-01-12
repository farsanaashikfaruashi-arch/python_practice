class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        @classmethod
        def from_birth_year(cls,name,birth_year):
            current_year=2025
            age=current_year-birth_year
            return cls(name,age)
p1=Person.from_birth_year("Asha",2000)
print(p1.age)
