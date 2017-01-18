# coding=UTF-8
import json
import cloudvalue
import sys

def getCloudValeViaJsonFile():
    jsonFile = checkPara()
    with open(jsonFile) as data_file:
    # with open("PG_601.json") as data_file:    
        data = json.load(data_file)
    keylist = []
    for cloudevalue in data["data"]:
        if(cloudevalue["section"] == "screensaver"):
            keys = cloudevalue["key_value"].split(",")
            for i in keys:
                keylist.append(i)
    return keylist


def parseCloudValue():
    keylist = getCloudValeViaJsonFile()
    for session in cloudvalue.screensaver:
        print()
        print(session["NOTE"])
        for key in session:
            non = True
            for target in keylist:
                if '"'+key+'":' in target:
                    non = False
                    target = target.replace('{','').replace('}','')
                    str = '{0:-<50}'.format(target)
                    print(str + session[key])
            if(non):
                str = '{0: <50}'.format(key)
                print(str + session[key] + "(   本地端   )")

def checkPara():
    if (len(sys.argv) > 1):
        return sys.argv[1]
    else:
        jsonFile = input("give me json file: ")
        return jsonFile


parseCloudValue()







