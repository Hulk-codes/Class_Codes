# functional
#def CheckEven(No):
#   return(No % 2 == 0 )

CheckEven = lambda No : (No % 2 == 0 )    
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