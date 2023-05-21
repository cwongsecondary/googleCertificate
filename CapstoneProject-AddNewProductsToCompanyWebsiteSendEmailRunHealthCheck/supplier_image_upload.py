#!/usr/bin/env python3
# Attempting to UPLOAD the jpeg files to the Fruit Catalog Web Server
# supplier_image_upload_cw.py

import os
import requests

homedir_path = os.environ['HOME'] + '/'
inpath = homedir_path + "supplier-data/images"         # supplier-data/images
fruit_catalog_url = "https://httpbin.org/post"         #"http://localhost/upload/"
files = {}

for filename in os.listdir(inpath):
    if filename.endswith(".jpeg"):
        jpegsNoExt = (filename.split('.')[0])           # filename no Extension
        with open(os.path.join(inpath,filename), "rb") as opened:
            files={'file': opened}
            print(files.items())
            res = requests.post(fruit_catalog_url, files={'file': opened})
            #res = requests.post(fruit_catalog_url, files)   # data=file, Data MUST be passed as a Dict
            print("File: {} Status Code: {}".format(files,res.status_code))

