class Arithematic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        print("Object gets Created successfully")

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
   
obj1 = Arithematic(11,10)       # Arithematic(id(obj1), 11,10) ---> __int__(id(obj1),11,10)
obj2 = Arithematic(21,20)       # Arithematic(id(obj2), 21,20) ---> __int__(id(obj2),21,20)

ret = obj1.Addition()
print(ret)

ret = obj2.Substraction()
print(ret)