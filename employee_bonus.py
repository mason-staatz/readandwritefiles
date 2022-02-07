import csv

infile = open("EmployeePay.csv", "r")

employee_file = csv.reader(infile, delimiter=",")

# to skip a line if the file contains a header
next(employee_file)


for record in employee_file:
    salary = float(record[3])
    salaryF = "${:,.2f}".format(salary)
    bonus = float(record[4]) * float(record[3])
    bonusF = "${:,.2f}".format(bonus)
    total_pay = bonus + salary
    totalF = "${:,.2f}".format(total_pay)

    print("First name:", record[1])
    print("Last name:", record[2])
    print("Salary:", salaryF)
    print("Bonus:", bonusF)
    print("Total Pay:", totalF)
    input()
