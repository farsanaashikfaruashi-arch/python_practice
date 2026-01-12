class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Asha",90)
s2=Student("Rohan",80)
print("S1 name:",s1.name)
print("S2 name:",s2.name)
s1.marks=95
print("S1 marks change")
print("S1 marks:",s1.marks)
print("S2 marks:",s2.marks)
        
