class Student:
    school="ABC Public School"
    def __init__(self,name):
        self.name=name
s1=Student("Asha")
s2=Student("Rohan")
print(s1.school)
print(s2.school)
Student.school="XYZ High School"
print(s1.school)
print(s2.school)        
