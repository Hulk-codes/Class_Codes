No = 11     # Global

def fun():
    No = 21
    print("Value of No from fun is : ",No)      
    No = No+1
    print("Value of No from fun is : ",No)

print("Value of No is : ", No)  #11
fun()
print("Value of No is : ", No)