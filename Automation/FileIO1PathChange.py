import os

def main():
    FileName = input("Enter the name of file: ")

    if(os.path.exists(FileName)):

        ret  = os.path.isabs(FileName)
        if (ret==True):
            print("it is absolute path")
        else:
            print("it is relative path")
            NewPath = os.path.abspath(FileName)
            print("Updated path: ", NewPath)
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()