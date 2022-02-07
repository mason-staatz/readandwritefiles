import csv

averages = open("Student_Scores.csv", "r")

averages_file = csv.reader(averages, delimiter=",")
outfile = open("student_avg.csv", "w")


for score in averages_file:
    average = "{:.2f}".format((float(score[1]) + float(score[2]) + float(score[3])) / 3)

    outfile.write(f"{score[0]} = {average}")
    outfile.write("\n")


outfile.close()
averages.close()
