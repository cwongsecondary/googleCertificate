#!/usr/bin/env python3
#run.py

import os
import requests

homedir_path = os.environ['HOME'] + '/'
descipt_path = homedir_path + "supplier-data/descriptions/"
img_path = homedir_path + "supplier-data/images/"
djangoDict = {}
url = "http://<ext_IP>/fruits"                                  # "http://127.0.0.1:8000/fruitwebapp/"


for filename in os.listdir(descipt_path):                       # supplier-data/descriptions/
    if filename.endswith(".txt"):
        with open(os.path.join(descipt_path,filename)) as file:
            lines = file.readlines()
            name = lines[0].strip()
            weight = int(lines[1].replace('lbs','').strip())
            description = lines[2].strip()
            image_name = filename.replace('txt','jpeg')

            # Add lines,weight,description to Dictionary
            data = {"name": name, "weight": weight, "description": description, "image_name": image_name}
    

        # Upload each jpeg file to url
        res = requests.post(url, json=data)
    if res.status_code == 201:
            print("Successful status code: " + str(res.status_code))
    else:
            print("Failed status error code: " + str(res.status_code))


