#!/usr/bin/env python

import csv
import os

"""
1 - function1 read_employees():
Open a CSV file as Read-only

2 - Read file 'employee-file' and append each row to list 'employee_list'
Function should return the contents of employee list
Function should return the contents of 'employee_list'

3 - function2: process_data()
Add the departments from list 'employee_list' into list 'department_list'
Then iterate through set(department_list), adding the department_name as the key and count as the value.
Function should return the contents of 'department_data'

4 - function3 - write_report()
Open File as 'w+', iterate through a 'sorted' dictionary; writing the key, followed by its value, then a newline

5 - Call the function read_employees, passing dir path, along with the csv file, and print the employee_list

6 - Call function process_data, passing 'employee_list'.  Print 'dictionary'

7 - Call function write_report, specify the dir path, writing to file 'report.txt'


"""





# csv module; csv.register_dialect, csv.DictReader
def read_employees(csv_file_location):
    # Open the file
    with open(csv_file_location,"r") as f:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        # Read the rows of the file into a dictionary
        employee_file = csv.DictReader(f, dialect='empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(data)

    return employee_list


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
       department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

# sorted, write to file
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

# os module; os.path.join, os.path.dirname
employee_list = read_employees(os.path.join(os.path.dirname(__file__),'c2-w2-employee-file.csv'))
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary,os.path.join(os.path.dirname(__file__),'report-sample-orig.txt'))
