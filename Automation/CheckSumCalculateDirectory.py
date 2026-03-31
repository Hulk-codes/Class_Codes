import hashlib
import os
def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()            # md5() is a inbuilt algorithm

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()         # gives CheckSum it is inbuilt function

def DirectoryWatcher(DirectoryName = "Marvellous"):
    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a directory")
        return

    for FolderName, SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            CheckSum = CalculateCheckSum(fname)

            print(f"File Name: {fname} Checksum : {CheckSum}")
            
def main():

    DirectoryWatcher()
   
if __name__ =="__main__":
    main()