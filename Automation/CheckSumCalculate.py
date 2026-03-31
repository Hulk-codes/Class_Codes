import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()            # md5() is a inbuilt algorithm

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()         # gives CheckSum it is inbuilt function

def main():
    
    Ret = CalculateCheckSum("Demo.txt")
    print("CheckSum is: " ,Ret)

if __name__ =="__main__":
    main()