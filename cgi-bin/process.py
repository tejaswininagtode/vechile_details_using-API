#!/usr/bin/python3

import xmltodict
import json
import parser
import os
import cgi
import subprocess as sp
import requests

print("content-type: text/html")
print()

def vehicle_info(text):
   r = requests.get(f'http://regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={str(text)}&username=Teju21@')
   data= xmltodict.parse(r.content)
   jdata=json.dumps(data)
   df = json.loads(jdata)
   df1 = json.loads(df['Vehicle']['vehicleJson'])
   return df1

form = cgi.FieldStorage()
cmd = form.getvalue("x")
print(cmd)

x=vehicle_info(cmd)
print(x)

