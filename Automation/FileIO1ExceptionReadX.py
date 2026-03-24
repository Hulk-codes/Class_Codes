def main():
   
    try:
        fobj = open("Hello.txt", "r")
        print("File gets successfully open")

        Data = fobj.read(6)

        print("Data from file is: ", Data)

        fobj.close()

    except FileNotFoundError:
        print("unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()