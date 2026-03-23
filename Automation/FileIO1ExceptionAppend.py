def main():
   
    try:
        fobj = open("Hello.txt", "a")
        print("File gets successfully open")

        fobj.write("Python Automation")

        fobj.close()

    except FileNotFoundError:
        print("unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()