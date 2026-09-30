'''
 #Find and print the highest-paid employee from each department. 
employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)
]

high_salary ={}
for employee in employees:
    name = employee[0]
    salary = employee [1]
    department = employee[2]

    if department not in high_salary or salary > high_salary[department][1]:
        high_salary[department] = (name , salary)
    for department , data in high_salary.items():
        print(department , data[0],data[1])






#Calculate and print the average salary for each department.

employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)

]

total_salary = {}
department_count ={}

for employee in employees:
    department = employee[1]
    salary = employee[2]

    if department not in total_salary :
        total_salary[department] = salary
        department_count[department]=1
    else:
        total_salary[department] += salary
        department_count[department] += 1
for department in total_salary:
    avrage_salary = total_salary[department] / department_count[department]
    print(department,avrage_salary)


#Print all employees whose salary is greater than the average salary of their department.
'''
employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)

]

total_salary = {}
department_count ={}

for employee in employees:
    name = employee[0]
    department = employee[1]
    salary = employee [2]

    if department not in total_salary :
        total_salary[department]=salary
        department_count[department] = 1
    else:
        total_salary[department] += salary
        department_count[department] += 1


for employee in employees:
    name = employee[0]
    department = employee[1]
    salary = employee [2]

    avrage_salary = total_salary[department] / department_count[department]
    if salary > avrage_salary :
        print(name,department,salary)



#Department with the Highest Average Salary
employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)

]

