# Task: Find the second-highest salary
'''
salaries = [45000, 62000, 38000, 75000, 52000, 90000, 48000]

highest_salary = 0
second_highest = 0
for i in salaries:
    if i > highest_salary:
     second_highest = highest_salary
     highest_salary = i

    elif i > second_highest :
       second_highest = i

print("second_highest",second_highest)



#Task: Find the frequency of each number
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20, 20]
cheked = []

for i in numbers:
    if i not in cheked:
        count = 0

        for j in numbers :
            if i == j :
                count += 1
        print(i ,"->",count)
        cheked.append(i)

#Find the salary that appears most frequently.
salaries = [45000, 52000, 38000, 75000, 62000, 52000, 90000, 45000]

cheked = []
most_frequent = 0
high_count = 0
for i in salaries:
    if i not in cheked:
        count =0

        for j in salaries:
            if i == j:
                count +=1
        print(i,'->',count)

        if count > high_count:
                high_count = count
                most_frequent = i
            
        cheked.append(i)
print("most_frequent",most_frequent)


Find the first number that appears only once.
numbers = [12, 5, 8, 12, 15, 5, 20, 8, 25, 15, 30]

cheked = []
unique = []

for i in numbers:
    if i not in cheked :
        count = 0

        for  j in numbers:
           if i == j:
            count += 1
        if count == 1: 
            unique.append(i)
            

    cheked.append(i)
print("unique->",unique)



#Find all duplicate numbers.
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]
cheked = []
duplicates = []
for i in numbers:
    if i not in cheked :
        count = 0
        for j in numbers:
            if i== j :
                count += 1
        if count > 1:
            duplicates.append(i)

        cheked.append(i)
print("duplicates",duplicates)



numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

cheked = []
first_count = 0
second_count = 0
first = 0 
second = 0

for i in numbers:
    if i not in cheked:
        count = 0

        for j in numbers:
            if i == j :
                count += 1

    if count > first_count :
        second_count = first_count
        first = second
        

        first_count = count 
        first = i
    elif count > second_count:
        second_count = count 
        second = i

    cheked.append(i)
print("second_most frequent number",second)

#Find the number with the highest frequency and its frequency.
numbers = [10, 20, 30, 10, 40, 20, 50, 30, 10, 60]
cheked = []

high_frequent = 0
frequency_count = 0
for i in numbers:
    if i not in cheked :
        count = 0
        for j in numbers:
            if i == j:
                count += 1

        if count > frequency_count :
            frequency_count = count 
            high_frequent = i

        cheked.append(i)
print('high_frequen',high_frequent)
print ('frequency',frequency_count)

# Find all numbers that appear more than once
numbers = [10, 20, 10, 30, 20, 40, 10, 30, 50, 20, 60]

cheked = []
frequent_number = 0
frequency_count =0

for i in numbers :
    if i not in cheked :
        count = 0
        for j in numbers :
            if i== j :
                count +=1 
        if count > frequency_count:
            frequency_count = count 
            frequency_count = i


        elif count > 1:
            frequent_number = count 
            frequent_number = i 
        

        cheked.append(i)
print("frequncy_count ",frequency_count)
print ("frequent_number ", frequent_number)
        

#Find the third-largest number without using:
numbers = [12,45,7,23,89,34,56,18,91]

largest = 0
second_largest = 0 
third_largest =0

for i in numbers:
    if i > largest :
        third_largest = second_largest
        second_largest = largest 
        largest = i

    elif i > second_largest:
        third_largest = second_largest
        second_largest = i

    elif i > third_largest :
        third_largest = i
print("third_largest",third_largest )


Find the second most frequent number without using'
numbers = [10, 25, 10, 30, 45, 25, 60, 30, 45, 70]

cheked = []
most_frequent = 0 
second_most_frequent = 0 

for i in numbers:
    if i not in cheked :
        count = 0
        for j in numbers:
            if j== i:
                count += 1
            if i > most_frequent:
             second_most_frequent = most_frequent
             most_frequent = i

            elif i > second_most_frequent and i != most_frequent:
               second_most_frequent = i
        cheked.append(i)


print("second most frequent ",second_most_frequent)
            



        
#Task: Find the frequency of each number without using
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20]

cheked = []

for i in numbers :
   if i not in cheked:
     count = 0
     for j in numbers :
       if  i == j:
          count+=1
     print(i,"->",count)
     cheked.append(i)

        
Task: Find the second highest unique salary without using:

salaries = [45000, 52000, 68000, 52000, 75000, 45000, 90000, 68000]

largest_salary = 0
second_largest = 0
for i in salaries:
    if i > largest_salary:
        second_largest = largest_salary
        largest_salary = i
    elif i > second_largest and i != largest_salary:
        second_largest = i 

print("second_largest salary",second_largest)


#Find all duplicate numbers without using set() or count().

numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

cheked =[]
duplicates=[]
for i in numbers:
    if i not in cheked :
        count = 0
        for j in numbers:
          if i == j :
                count += 1
        if count > 1 :
            duplicates.append(i)
        cheked.append(i)

print("duplicates",duplicates)



#Find the most frequently occurring number.

numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20, 50]

cheked = []
most_frequent_occure=0
high_count = 0
for i in numbers:
    if i not in cheked:
        count = 0
        for j in numbers :
            if i== j :
                count+=1
        if count > high_count:
            high_count = count
            most_frequent_occure = i

        cheked.append(i)
print("most_frequent_occure",most_frequent_occure)
print("high_value",high_count)



employees = [
    ("Amit", 50000),
    ("Rahul", 75000),
    ("Sneha", 60000),
    ("Priya", 90000),
    ("Vikas", 75000)
]

#Task: Find the employee with the second highest unique salary.
largest = 0
second_largest=0
second_employee = ""
for i in employees:
    salary = i[1]

    if salary > largest:
        second_largest = largest
        largest = salary
    elif salary > second_largest and salary != largest:
        second_largest = salary
        second_employee = i[0]
print("second_largest",second_largest)
print("employee name",second_employee)



#Find the second-highest distinct salary and print the employee name(s) who have that salary
employees = [
    ("Amit", 65000),
    ("Rahul", 85000),
    ("Sneha", 72000),
    ("Priya", 95000),
    ("Vikas", 85000)
]
largest = 0
second_largest = 0
employee_second = 0

for i in employees:
    name = i[0]
    salary = i[1]

    if salary > largest :
        second_largest = largest
        largest = salary 
        employee_second = []

    elif salary > second_largest and salary!= largest:
        second_largest = salary 
        employee_second = [name]
    elif salary == second_largest:
        employee_second.append(name)
print("second salary ",second_largest)
print ("employeee(s)",second_employee)





Find the salary that occurs more than once and print each salary with its frequency.

employees = [
    ("Amit", 65000),
    ("Rahul", 85000),
    ("Sneha", 72000),
    ("Priya", 85000),
    ("Vikas", 65000),
    ("Neha", 95000)
]

frequency = {}
for i in employees:
    salary = i[1]
    frequency[salary] =  frequency.get(salary,0) + 1
for salary,count in frequency.items():
    if count > 1:
     print(salary , count)

#Find and print the employee name(s) who have the same salary, along with that salary.

employees = [
    ("Amit", 65000),
    ("Rahul", 85000),
    ("Sneha", 72000),
    ("Priya", 95000),
    ("Vikas", 85000),
    ("Neha", 72000)
]

frequency = {}

for employee in employees :
    salary = employee[1]
    frequency[salary] = frequency.get(salary,0)+ 1

for employee in employees :
    name = employee[0]
    salary = employee[1]

    if frequency[salary] > 1:
        print(name , salary)



employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)
]
highest_salary = {}

for employee in employees:
    department = employee[1]
    salary = employee[2]

    if department not in highest_salary :
        highest_salary[department] = salary 
    elif salary > highest_salary[department]:
        highest_salary[department]=salary
    for department, salary in highest_salary.items():
        print(department , salary)

        
Find the employee with the second-highest salary and print their name and salary.


employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)
]

largest_salary =0
second_salary = 0
for employee in employees:
    name = employee[0]
    salary = employee[2]

    if salary > largest_salary :
        second_salary = largest_salary
        largest_salary = salary 

    elif salary > second_salary and salary != largest_salary:
        second_salary = salary 

print("second_hest _salary",second_salary)


# Find the highest-paid employee in each department and print:

employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)
]

high_paid = {}

for employee in employees:
    name = employee[0]
    department = employee[1]
    salary = employee[2]

    if department not in high_paid or salary> high_paid[department][1]:
        high_paid[department] = (name,salary)

    for department, data in high_paid.items():
        print(department ,data[0],data[1])

'''
#Find the average salary of each department and print:

employees = [
    ("Amit", "IT", 65000),
    ("Rahul", "HR", 55000),
    ("Sneha", "IT", 85000),
    ("Priya", "Finance", 70000),
    ("Vikas", "IT", 75000),
    ("Neha", "HR", 65000)
]

avg_salary = {}
total_salary = {}
department_count ={}

for employee in employees:
    name = employee[0]
    department = employee[1]
    salary = employee[2]

    if department not in total_salary :
        total_salary [department] = salary
        department_count[department] = 1
    else :
        total_salary[department] += salary
        department_count[department] += 1

for department in total_salary:
    avg_salary = total_salary[department] / department_count[department]

    print(department,avg_salary)
    
