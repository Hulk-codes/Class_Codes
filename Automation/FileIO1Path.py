import os

def main():
    FileName = input("Enter the name of file: ")

    ret  = os.path.isabs(FileName)
    if (ret==True):
        print("it is absolute path")
    else:
        print("it is relative path")
   

if __name__ == "__main__":
    main()