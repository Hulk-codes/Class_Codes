import time
import os

def SumCube(No):
    print("Process is running with PID : ", os.getpid())
    Sum = 0
    
    for i in range(1,No+1):
        Sum = Sum + (i**3)

    return Sum


def main():
    data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    Result = []

    start_time = time.time()

    for i in range(len(data)):
        Ret = SumCube(data[i])
        Result.append(Ret)

    end_time = time.time()

    
    print(Result)
    print("Total time of execution: ", end_time - start_time)
    

if __name__ == "__main__":
    main()    