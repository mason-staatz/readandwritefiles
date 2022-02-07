import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")

# to skip a line if the file contains a header
next(customer_file)

for record in customer_file:
    print("Last name:", record[2])
