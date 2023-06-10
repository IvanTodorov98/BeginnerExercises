# This program calculates your salary and expenses

def calculate_monthly_salary(hourly_rate):
    working_hours_per_week = 39
    working_weeks = 4
    monthly_salary = hourly_rate * working_hours_per_week * working_weeks
    return monthly_salary

ivan_salary = calculate_monthly_salary(15.30) 
pesho_salary = calculate_monthly_salary(8.30)

if ivan_salary > pesho_salary: 
    print("Pesho e typak")
elif ivan_salary == pesho_salary:
    print("Pesho e sreden s Ivan")
else:
    print("Pesho stava")

salaries = [ivan_salary,pesho_salary]

for salary in ivan_salary:
    print(salary)

 

