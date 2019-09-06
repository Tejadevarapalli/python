class Employee():

    def __init__(self,fname=None,lname=None,sal=None,dep=None):
        self.fname=fname
        self.lname=lname
        self.sal=sal
        self.dep=dep

    def averagesal(self,employeelist=[],*args):
        total_sal=0
        employee_count=0
        for employee in employeelist:
           print(employee.fname)
           total_sal=total_sal+employee.sal
           employee_count+=1
        return total_sal/employee_count



class FulltimeEmployee(Employee):

    def __init__(self,fname,lname,sal,dep):
        Employee.__init__(self,fname,lname,sal,dep)



if __name__ == "__main__":
    print("Welcome to Teja Technologies\n")
    Input = input("press Y to continue to add employees\n")
    Employeeslist = []
    while (Input.upper() == 'Y'):
        fname = input("Enter the First name\n")
        lname = input("Enter the Last name\n")
        sal = int(input("Enter the salary\n"))
        dep = input("Enter the department\n")
        Employeeslist.append(FulltimeEmployee(fname, lname, sal, dep))
        print("Employee got successfully added into the system\n")
        print("To continue adding the employees PRESS 'Y' or press any key to abort\n")
        Input = input()
    print("average of salary")
    print(Employee().averagesal(Employeeslist))
    print("Employee count",len(Employeeslist))








