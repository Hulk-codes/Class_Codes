# Procedural
def CheckEven(No):
    if (No % 2 == 0 ):
        print("it is even")
    else:
        print("it is odd")    



def main():
    value = 0
    
    print("Enter Number: ")
    value = int(input())

    CheckEven(value)
   
if __name__ == "__main__" :
    main()  