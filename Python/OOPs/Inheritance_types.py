class Employee:
    start_time = "10am"
    end_time = "6pm"


class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role


class Management(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary


mg1 = Management(50000,"HR")
print(mg1.role,mg1.salary,mg1.start_time,mg1.end_time)