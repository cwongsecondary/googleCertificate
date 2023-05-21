#!/usr/bin/env python3
#run_cw.py

import os
import requests
from requests.auth import HTTPBasicAuth

homedir_path = os.environ['HOME'] + '/'
descipt_path = homedir_path + "supplier-data/descriptions/"
img_path = homedir_path + "supplier-data/images/"
djangoDict = {}
url = "http://127.0.0.1:8000/fruitwebapp/"                      # "http://<ext_IP>/fruits"


for filename in os.listdir(descipt_path):                       # supplier-data/descriptions/
    if filename.endswith(".txt"):
        with open(os.path.join(descipt_path,filename)) as file:
            lineValue = file.read().strip().split('\n')
            djangoDict["title"] = lineValue[0]
            djangoDict["name"] = lineValue[0]
            djangoDict["weight"] = lineValue[1]
            djangoDict["description"] = lineValue[2]
            image_name = filename.replace('txt','jpeg')
            djangoDict["image_name"] = image_name

            #lines = file.readlines()
            #title = lines[0].strip()    # For Testing
            #name = lines[0].strip()
            #weight = int(lines[1].replace('lbs','').strip())    # might need to update 'lbs' to ' lbs'??
            #description = lines[2].strip()
            #image_name = filename.replace('txt','jpeg')

            # Add lines,weight,description to Dictionary
            #data = {"name": name, "weight": weight, "description": description, "image_name": image_name}
    #print(data)
    
            

    # Upload each jpeg file to url
    #res = requests.post(url, json=djangoDict)
        res = requests.post(url, json=djangoDict, auth=HTTPBasicAuth('chriswong', 'pw'))
    if res.status_code == 201:
            print("Successful Post:", djangoDict["title"] + ", status code: " + str(res.status_code))
    else:
            print("Error Encountered: " + djangoDict["title"] + ", status error code: " + str(res.status_code))


