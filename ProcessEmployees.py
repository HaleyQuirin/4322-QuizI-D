"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file
infile = open("employee_data.csv", "r")
outfile = open("newemployee_data.csv", "w")
# outfile = csv.writer(write)
EmployeeDict = {}
# create an empty dictionary
# next(infile)

read = csv.reader(infile, delimiter=",")

outfile.write("Employee Name, Salary\n")

EmployeeSal = 0
# use a loop to iterate through the csv file
for line in read:
    FirstName = line[1]
    LastName = line[2]
    Salary = line[5]
    # New_Salary = float(line[5]) * 1.1
    newfile = FirstName + " " + LastName + ", " + Salary
    outfile.write(newfile + "\n")

    # check if the employee fits the search criteria
infile.close()
outfile.close()

print(EmployeeDict)
print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
