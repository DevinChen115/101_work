import json

# jsonFilePath = input("please give me json file full path: ")

with open('pgwall.json') as data_file:    
    data = json.load(data_file)

style='<style type="text/css">#test{float:left;}</style>'
print(style)
print('<div>')
count = 1
for i in data["data"]["posts"]:
    print('<div id="test"><img src="'+i['thrumbNail']['small']+'"><br>')
    print(str(count) + " isPrivate: "+i['isPrivate']+' followed: '+ str(i['user']['followed']) +'</div>')
    count = count + 1
print('</div>')