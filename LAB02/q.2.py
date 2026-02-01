#q.2
class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    
    def calculate_salary(self):
        print("salary:")
        
class FullTimeEmployee(Employee):
    def __init__(self,name,emp_id,monthly_salary):
        super().__init__(name,emp_id)
        self.monthly_salary=monthly_salary
        
    def calculate_salary(self):
        print("monthly salary is:" , self.monthly_salary)
        
class PartTimeEmployee(Employee):
    def __init__(self,name,emp_id,hours_worked, hourly_rate):
        super().__init__(name,emp_id)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate
        
    def calculate_salary(self):
        salary = self.hourly_rate * self.hours_worked
        print("salary is:", salary)
        
E1 = FullTimeEmployee("john",48903, 9000)
E2 = PartTimeEmployee( "Caleb", 48841, 30, 5)

E1.calculate_salary()
E2.calculate_salary()
