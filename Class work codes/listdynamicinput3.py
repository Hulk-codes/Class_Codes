def Summation(Arr):
    sum = 0

    for i in range(len(Arr)):
        sum = sum + Arr[i]

    return sum


def main():
    size = 0
    value = 0
    Ret = 0
    
    print("Enter the no of elements: ")
    size = int(input())

    data = list()

    print("enter the elements : ")
    
    for i in range(size):
        value = int(input())
        data.append(value)

    
    Ret = Summation(data)
    print("Sum is : ",Ret)    


if __name__ == "__main__":
    main()