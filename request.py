# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 01:17:01 2018

@author: POMAH
"""

import requests


files = {'file': ('IMG_5558.JPG', open('C:\\Users\\POMAH\\Downloads\\IMG_5558.JPG', 'rb'), 'image/jpeg')}
data = {
       'text' : 'asdsadsd',
       'font' : '1',
       'fontcol' : '1',
       'fontsize' : '1070',
       'prozr' : '50',
       'pos' : '0',
       'angle' : '0',
       'stepv' : '50',
       'stepg' : '50',
       'quality' : '85'

        
        
        
        
        }
r = requests.post("http://watermark.algid.net/ru/watermark-text-result.php",data = data, files = files)
print(r.text)