from functools import reduce


Checkeven = lambda No : (No % 2 == 0)
Increment = lambda No : No +1
Add = lambda A, B : A + B

def filterX(Task, Elements):    # task = checkeven , elements = list
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if (Ret == True):
            Result.append(no)
    
    return Result

def main():
    data = [11,10,15,20,22,27,30]
    print("Actual data is : ", data)

    Fdata = list(filterX(Checkeven, data))  
    print("Data after filter is : ", Fdata)

    Mdata = list(map(Increment, Fdata))
    print("Data after map is : ", Mdata)

    Rdata = reduce(Add, Mdata)
    print("Data after reduce is : ", Rdata)


if __name__ == "__main__":
    main()
