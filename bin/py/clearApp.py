# encoding: utf-8

import sys
import os

appMap = {
			"CM":"",
			"CMS":"",
			"KBD":"",
			"LAU":"",
			"PG":""
		} # key:vale

def checkPara():
	result = 0
	if (len(sys.argv) > 1):
		result = 1
	return result


def doClearApp(appName):
	print(appName)
	appName = appName.upper()
	try:
	   pkgName = appMap[appName]
	   cmd = "adb shell pm clear " + pkgName
	   os.system(cmd) # 執行系統指令
	   cmd = 'adb shell am force-stop ' + pkgName
	   os.system(cmd)
	except:
		print("似乎打錯囉, 目前提供 CM, CMS, KBD")
		appName = input("請告訴我想要清除哪一個app, 目前提供 CM, CMS, KBD, LAU, PG: ")
		# input() 可以透過螢幕取得參數
		doClearApp(appName)

def clearApp(para):
	if(checkPara()):
		for x in range(1, len(para)):
			doClearApp(para[x])
	else:
		#print("請告訴我想要清除哪一個app, 目前提供 CM, CMS, KBD")
		appName = input("請告訴我想要清除哪一個app, 目前提供 CM, CMS, KBD: ")
		doClearApp(appName)

clearApp(sys.argv)
