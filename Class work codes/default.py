
def EmployeeInfo(name,age,salary,city="Pune"):
    print("name : ", name)
    print("age : ", age)
    print("salary : ", salary)
    print("city : ", city)


def main():
    
    EmployeeInfo("Rahul",26,2000) 
    print("-"*20)
    EmployeeInfo("Rahul",26,2000,"Mumbai") 

if __name__ == "__main__":
    main()