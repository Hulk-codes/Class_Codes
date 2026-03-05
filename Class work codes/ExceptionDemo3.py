def main():
    Ans = 0 
    try:
        print("Inside try")
        print("Enter first number: ")
        No1 = int(input())

        print("Enter Second number: ")
        No2 = int(input())
     
        print("Inside try")
        Ans = No1/No2
    except ZeroDivisionError as zobj:
        print("inside except : ",zobj)
    
    except ValueError as vobj: 
        print("Inside Except : ",vobj)

    except Exception as eobj:
        print("Inside except : ",eobj)
    finally:
        print("Inside fnally")

    print("Division is : ", Ans)


if __name__ == "__main__":
    main()