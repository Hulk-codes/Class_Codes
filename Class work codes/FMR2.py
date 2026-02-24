def Checkeven(No):
    return(No % 2 == 0)

def Increment(No):
    return No +1 


def main():
    data = [11,10,15,20,22,27,30]
    print("Actual data is : ", data)

    Fdata = list(filter(Checkeven, data))  
    print("Data after filter is : ", Fdata)

    Mdata = list(map(Increment, Fdata))
    print("Data after map is : ", Mdata)


if __name__ == "__main__":
    main()
