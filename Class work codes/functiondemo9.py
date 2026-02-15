#One function can call another function 

def fun():
    print("inside fun")

def gun():
    print("inside gun") 


def main():
    fun()
    gun()
    

if __name__ == "__main__":
    main()
