# coding=UTF-8
import cloudvalue_pg
import json

# jsonFilePath = input("please give me json file full path: ")
jsonFile = input("give me json file: ")
with open(jsonFile) as data_file:    
    data = json.load(data_file)
keylist = []
for cloudevalue in data["data"]:
    if(cloudevalue["section"] == "screensaver"):
        keys = cloudevalue["key_value"].split(",")
        for i in keys:
            keylist.append(i)

for i in cloudvalue_pg.screensaver:
    non = True
    for j in keylist:
        if '"'+i+'":' in j:
            non = False
            j = j.replace('{','').replace('}','')
            str = '{0:-<50}'.format(j)
            print(str+cloudvalue_pg.screensaver[i])
    if(non):
        str = '{0: <50}'.format(i)
        print(str+"LocalDefault "+cloudvalue_pg.screensaver[i])


