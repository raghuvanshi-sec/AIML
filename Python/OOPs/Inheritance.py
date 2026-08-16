class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self,new_end_time):
        self.end_time = new_end_time


class Programmer(Employee):
    def __init__(self,expertise):
        self.expertise = expertise

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role


staff1 = AdminStaff("HR")
staff1.change_time("7pm")
print(staff1.start_time, staff1.role, staff1.end_time)



    
