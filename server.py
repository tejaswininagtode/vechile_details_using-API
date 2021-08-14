import xmltodict
import json
import parser
import os
 def vehicle_info(text):
    r = requests.get(f'http://regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={str(text)}&username=nikhiltidke101')
    data= xmltodict.parse(r.content)
    jdata=json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1