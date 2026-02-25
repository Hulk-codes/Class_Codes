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
        sum = Task (sum,no)
        
    return sum