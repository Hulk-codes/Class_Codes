def display(A,B,C,D):
    print (A,B,C,D)

def main():
    #display(10,20)  will show error as this is not allowed coz arguments are 4 and parameters are 2
    #display(10,20,30,40,50) will show erroe as this is not allowed coz arguments are 4 and parameters are 5
    display(10,20,30,40) # allowed
if __name__ == "__main__":
    main()