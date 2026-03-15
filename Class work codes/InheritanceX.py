class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        self.No1 = 10
        self.No2 = 20

    def Fun(Self):
        print("Inside Fun method of Parent:" , Self.No1, Self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()          # it is compulsory to call super as it will give access to parent __init__
        print("Inside Child Constructor")
        self.A = 11
        self.B = 21

    def Sun(self):
        print("Inside Sun method of Child:",  self.A ,self.B, self.No1 , self.No2)

cobj = Child()

print(cobj.No1)  # 10
print(cobj.No2)  # 20

print(cobj.A)  # 11
print(cobj.B)  # 21

cobj.Fun()
cobj.Sun()