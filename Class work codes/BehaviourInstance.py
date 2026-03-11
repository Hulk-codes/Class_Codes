class Demo:
    No = 10

    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def Fun(self):
        print("Inside instance method Fun: ", self.Value1, self.Value2)

    @classmethod
    def Sun(cls):
        print("Inside class Method sun: ", cls.No)

Demo.Sun()
print("Class variable: ", Demo.No)

obj = Demo(11,21)
obj.Fun()
print("Instance Variable: ", obj.Value1,obj.Value2)