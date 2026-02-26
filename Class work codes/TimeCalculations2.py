import time

def factorial(No):
    fact = 1

    for i in range(1,No+1):
        fact = fact * i


    return fact

def main():
    value = int(input("Enter Number : "))
    
    start_time = time.time()

    Ret = factorial(value)

    end_time = time.time()

    print("factorial is : ", Ret)
    print("Total execution time is : ", end_time - start_time)
    
    
if __name__ == "__main__":
    main()