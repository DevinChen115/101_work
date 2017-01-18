import json
import os
#from BugInfo import BugInfo
#from pprint import pprint

class BugInfo:
    def __init__(self, fileName, line, bug_type, qualifier):
        self.fileName = fileName
        self.line = line
        self.bug_type = bug_type
        self.qualifier = qualifier

with open('report.json') as data_file:    
    data = json.load(data_file)

bugInfoArray = []

for i in range(len(data)):
    bugInfoArray.append(BugInfo(data[i]['file'],data[i]['line'],data[i]['bug_type'],data[i]['qualifier']))


def getAuthor(file,line):
    cmd = "git log -L" + line + ", " + line + "\:" + file
    gitAuthor = os.popen(cmd).read()



# print(data[0]['line'])
# print(data[0]['file'])
# print(data[0]['bug_type'])
# print(data[0]['qualifier'])
#pprint(data)