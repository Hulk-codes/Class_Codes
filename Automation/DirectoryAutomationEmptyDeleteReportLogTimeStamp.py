import sys
import os
import time

def DirectoryScanner(DirName = "Marvellous"):
    border = "-" * 52
    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName , "w")
    
    fobj.write(border+"\n")
    fobj.write("This is a log file created by Marvellous Infosysytems\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write(border+"\n")
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("there is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("it is not a directory")
        return
    
    FileCount = 0 
    EmptyFileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirName):

        for fName in FileName:
            FileCount = FileCount+1

            fName = os.path.join(FolderName,fName)
            
            if(os.path.getsize(fName)==0):   #Empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fName)
    
    fobj.write(border+"\n")
    
    fobj.write("Total file scanned:  "+str(FileCount)+ "\n")
    fobj.write("Total Empty files count:  "+str(EmptyFileCount)+ "\n")
    fobj.write("This Log file is created at: "+timestamp+ "\n")
    fobj.write(border+ "\n")


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

    print(border)
    print("-----------Marvellous Directory Automation----------")
    print(border)

if __name__ =="__main__":
    main()