class Employee:
    def __init__(self):
    
        self.name = ""
        self.monthly_salary = 0.0
        self.tax_percentage = 2.0  # Default tax percentage

    def get_data(self):
       
        self.name = input("Enter employee name: ")
        self.monthly_salary = float(input("Enter monthly salary: "))
        self.tax_percentage = float(input("Enter percentage of tax: "))

    def Salary_after_tax(self):
    
        tax_amount = (self.tax_percentage / 100) * self.monthly_salary
        salary_after_tax = self.monthly_salary - tax_amount
        return salary_after_tax

    def update_tax_percentage(self, new_tax_percentage):
   
        self.tax_percentage = new_tax_percentage


employee = Employee()

employee.get_data()


print(f"Salary after {employee.tax_percentage}% tax: ${employee.Salary_after_tax():.2f}")

new_tax_percentage = float(input("Enter new percentage of tax: "))
employee.update_tax_percentage(new_tax_percentage)


print(f"Salary after {employee.tax_percentage}% tax: ${employee.Salary_after_tax():.2f}")
