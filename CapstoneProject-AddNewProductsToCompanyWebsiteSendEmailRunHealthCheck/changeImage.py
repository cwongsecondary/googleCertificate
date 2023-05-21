#!/usr/bin/env python3

from PIL import Image
import os

homedir_path = os.environ['HOME'] + '/'
inpath = homedir_path + "supplier-data/images"
outpath = homedir_path + "supplier-data/images/"


for file in os.listdir(inpath):
    if file.endswith('.tiff'):
        absFilename = os.path.join(inpath,file)
        with Image.open(absFilename) as im:
            im = im.convert('RGB')
            fileNoExt = file.split('.')
            fileNoExt = fileNoExt[0]          
            im.resize((600,400)).save(outpath + fileNoExt + '.jpeg')
            print(os.path.join(outpath + fileNoExt + '.jpeg'))

