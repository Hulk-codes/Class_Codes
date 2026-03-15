class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
       

    def Fun(Self):
        print("Inside Fun method of Parent:")

class Child(Parent):
    def __init__(self):
        super().__init__()          # it is compulsory to call super as it will give access to parent __init__
        print("Inside Child Constructor")
        
    def Fun(self):
        super().Fun()               # here it will call Fun() of Parent //

        print("Inside Fun method of Child:")

cobj = Child()

cobj.Fun()


