import os

def main():
    FileName = input("Enter the name of file: ")

    ret  = os.path.exists(FileName)
    
    if (ret == True):
        fobj = open(FileName, "r")
        print("File gets successfully open")

    else:
        print("There is no such file")
   

if __name__ == "__main__":
    main()