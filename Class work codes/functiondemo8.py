#accept : Multiple parameters
#return : multiple values

def marvellous1 (Value1, Value2):
    print("inside marvellous 1 : ",Value1, Value2)
    return 11,21,51

def main():
    result1 = None
    result2 = None
    result3 = None
    result1,result2,result3 = marvellous1("pyhton",21)
    print("return values are : ", result1,result2,result3)
  

if __name__ == "__main__":
    main()
