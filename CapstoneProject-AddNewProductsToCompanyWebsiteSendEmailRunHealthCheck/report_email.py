#!/usr/bin/env python3
# report_email_cw.py

import os
import sys
import locale
import requests
import datetime
from datetime import date
import reports
import emails              # emails_generate_send

homedir_path = os.environ['HOME'] + '/'
descipt_path = homedir_path + "supplier-data/descriptions/"
productWeight = {}
productWeight_list = []
product_message = []

def productWeight_dict_to_table(productWeight):
    """ Convert dict data to a list of lists """
    table_data = [["name", "weight"]]
    for item in productWeight:
        table_data.append(item["name"], item["weight"])
    return table_data


def process_data (descript_path):
    # TODO: Iterate through descriptions Directory, open each txt file, then return the acquired data with line     # breaks
    for filename in os.listdir(descipt_path):                       # supplier-data/descriptions/
        if filename.endswith(".txt"):
            with open(os.path.join(descipt_path,filename)) as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                productWeight[name] = weight
                productWeight_list.append("name: {}<br/>weight: {}<br/>".format(name,weight))
    return "<br/>".join(productWeight_list)

    '''
    for key in productWeight.keys():
        product_message.append("name: {}\nweight: {}\n".format(key,productWeight[key]))   
        Output:
        ['name: Blackberry\nweight: 150 lbs\n', 'name: Avocado\nweight: 200 lbs\n', 'name: Apple\nweight: 500 lbs\n', 'name: Kiwifruit\nweight: 250 lbs\n', 'name: Grape\nweight: 200 lbs\n', 'name: Watermelon\nweight: 500 lbs\n', 'name: Lemon\nweight: 300 lbs\n', 'name: Mango\nweight: 300 lbs\n', 'name: Strawberry\nweight: 240 lbs\n', 'name: Plum\nweight: 150 lbs\n']
    print(product_message)
    '''

    """
    Output:
    name: Blackberry
    weight: 150 lbs

    name: Avocado
    weight: 200 lbs

    name: Apple
    weight: 500 lbs

    name: Kiwifruit
    weight: 250 lbs

    name: Grape
    weight: 200 lbs

    name: Watermelon
    weight: 500 lbs

    name: Lemon
    weight: 300 lbs

    name: Mango
    weight: 300 lbs

    name: Strawberry
    weight: 240 lbs

    name: Plum
    weight: 150 lbs
    """


def main(argv):
    attachment = "/tmp/processed.pdf"

    # TODO: Generate PDF via reports.generate_report(attachment, title, paragraph)
    report_message = process_data(descipt_path)
    d = date.today()
    report_title = ("Processed Update on {} {}, {}".format(d.strftime("%B"),d.strftime("%d"),d.strftime("%Y")) + "<br/>")
    print(report_title)
    print(report_message)


    reports.generate_report("/tmp/processed.pdf", report_title, report_message)

    
    # TODO: Create and Send Email via emails.generate_email(sender, receiver, subject, body, attachment)
    sender = "automation@example.com"
    receiver = "chriswong@localhost" 
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
    

if __name__ == "__main__":
  main(sys.argv)

