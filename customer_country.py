import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")
outfile = open("customer_country.csv", "w")
# to skip a line if the file contains a header

counter = 0
for record in customer_file:
    outfile.write(f"{record[1]}, {record[2]}, {record[4]}")
    outfile.write("\n")
    counter += 1


outfile.close()
customers.close()
print(counter - 1)
