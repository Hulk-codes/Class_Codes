
def EmployeeInfo(name,age,salary,city):
    print("name : ", name)
    print("age : ", age)
    print("salary : ", salary)
    print("city : ", city)


def main():
    
     # Keyword Argument
    EmployeeInfo(age=26, name="Rahul", city="Pune", salary=None) # correct Keyword Argument
    

if __name__ == "__main__":
    main()