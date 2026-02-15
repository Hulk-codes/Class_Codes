
def EmployeeInfo(name,age,salary,city):
    print("name : ", name)
    print("age : ", age)
    print("salary : ", salary)
    print("city : ", city)


def main():
    # Positional //
   # EmployeeInfo("Rahul",26,20000,"Pune") # correct
   # EmployeeInfo(26,"Rahul","Pune",20000) # wrong

    EmployeeInfo(age=26, name="Rahul", city="Pune", salary=20000) # correct Keyword Argument
    

if __name__ == "__main__":
    main()