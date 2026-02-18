# Procedural
def CheckEven(No):
    if (No % 2 == 0 ):
        return True
     
    else:
        return False
          
def main():
    value = 0
    Ret = False
    
    print("Enter Number: ")
    value = int(input())

    Ret = CheckEven(value)

    if (Ret == True):
        print("it is even")
    else:
        print("it is odd")    
   
if __name__ == "__main__" :
    main()  