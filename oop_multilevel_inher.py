class GrandFather:
    def house(self):
        print("House")
class Father(GrandFather):
    pass
class Son(Father):
    pass
s = Son()
s.house()
