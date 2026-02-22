No = 11     # Global

def fun():
    global No
    print("Value of No from fun is : ",No)    #11  
    No = No+1
    print("Value of No from fun is : ",No)  #12

print("Value of No is : ", No)  #11
fun()
print("Value of No is : ", No)  #12