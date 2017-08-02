import json
import commands
import os

def getAuthor(file,line):
    cmd = "git log -L " + str(line) + "," + str(line) + ":" + file + " -1 | grep -i author"
    gitAuthor = commands.getoutput(cmd)
    return gitAuthor

def getDate(file,line):
    cmd = "git log -L " + str(line) + "," + str(line) + ":" + file + " -1 | grep -i date"
    gitDate = commands.getoutput(cmd)
    return gitDate

with open("/var/lib/jenkins/workspace/"+os.environ['JOB_NAME']+"/infer-out/report.json") as data_file:
    data = json.load(data_file)

dot = ",";

for i in range(len(data)):
    author = getAuthor(data[i]['file'],data[i]['line'])
    date = getDate(data[i]['file'],data[i]['line'])
    print data[i]['file']+dot+str(data[i]['line'])+dot+data[i]['bug_type']+dot+author+dot+date
