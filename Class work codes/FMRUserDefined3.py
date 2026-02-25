

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

def mapX(Task, Elements):       # task = Increment , elements = list
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    sum = 0

    for no in Elements:
        sum = Task(sum, no)
        
    return sum



def main():
    data = [11,10,15,20,22,27,30]
    print("Actual data is : ", data)

    Fdata = list(filterX(Checkeven, data))  
    print("Data after filter is : ", Fdata)

    Mdata = list(mapX(Increment, Fdata))
    print("Data after map is : ", Mdata)

    Rdata = reduceX(Add, Mdata)
    print("Data after reduce is : ", Rdata)


if __name__ == "__main__":
    main()
