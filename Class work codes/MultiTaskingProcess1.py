import multiprocessing  
import time   
import os          

def SumEven(No):
    print("PID of SumEven : ", os.getpid())     #51
    print("PPID of SumEven : ", os.getppid())   #21

    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum+i

    print("Even sum is : ", Sum)

def SumOdd(No):
    print("PID of SumOdd : ", os.getpid())      #101
    print("PPID of SumOdd : ", os.getppid())    #21
    Sum = 0
    for i in range(1,No+1,2):
        Sum = Sum + i

    print("odd Sum is : ", Sum)


def main():
    print("PID of Main : ", os.getpid())   # 21
    print("PPID of Main : ", os.getppid())  # CMD 11

    start_time = time.time()

    P1 = multiprocessing.Process(target=SumEven, args=(100000000,))
    P2 = multiprocessing.Process(target=SumOdd, args=(100000000,))
   
    P1.start()
    P2.start()
   
    P1.join()
    P2.join()

    end_time = time.time()
    print("Time required: ", end_time - start_time)

    
if __name__ == "__main__":                                  
    main()