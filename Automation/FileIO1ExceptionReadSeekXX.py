# seek(Kuthe,Kuthun)
# Kuthun : 0 / 1 / 2 
# 0 : Starting
# 1 : Current
# 2 : End

def main():
   
    try:
        fobj = open("Hello.txt", "r")
        print("File gets successfully open")

        print("Current offset is: ", fobj.tell())       #0

        fobj.seek(11,0)

        print("Current offset is: ", fobj.tell())       #11
        
        Data = fobj.read(6)

        print("Current offset is: ", fobj.tell())       #17

        print("Data from file is: ", Data)              #mation

        fobj.close()

    except FileNotFoundError:
        print("unable to open file as there is no such file")

    finally:
        print("End of Application")
        

if __name__ == "__main__":
    main()