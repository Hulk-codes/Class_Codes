import threading                

def SumEven(No):
    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum+i

    print("Even sum is : ", Sum)

def SumOdd(No):
    Sum = 0
    for i in range(1,No+1,2):
        Sum = Sum + i

    print("odd Sum is : ", Sum)


def main():
    SumEven(10000000)
    SumOdd(10000000)

    
if __name__ == "__main__":                                  
    main()