def main():
    size = 0
    
    print("Enter the no of elements: ")
    size = int(input())

    data = list()

    print("enter the elements : ")
    
    for i in range(size):
        value = int(input())
        data.append(value)

    print(data)


if __name__ == "__main__":
    main()