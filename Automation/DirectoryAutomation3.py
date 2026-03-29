import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("there is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("it is not a directory")
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        for fName in FileName:
            fName = os.path.join(FolderName,fName)
            print("File Name: " , fName)
            print("File SIze: ", os.path.getsize(fName))

def main():
    border = "-" * 52
    print(border)
    print("-----------Marvellous Directory Automation----------")
    print(border)

    if (len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("Please specify the name of Directory")
        return
    
    DirectoryScanner(sys.argv[1])
    

if __name__ =="__main__":
    main()