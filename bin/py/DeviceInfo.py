import subprocess
import sys
import os

sdkVerMap = {
                "23\n":"Android 6.0",
                "22\n":"Android 5.1 ",
                "21\n":"Android 5.0",
                "20\n":"Android 4.4W",
                "19\n":"Android 4.4",
                "18\n":"Android 4.3",
                "17\n":"Android 4.2 ~ 4.2.2",
                "16\n":"Android 4.1 ~ 4.1.1",
                "15\n":"Android 4.0.3 ~ 4.0.4",
                "14\n":"Android 4.0 ~ 4.0.2",
                "13\n":"Android 3.2 "
}

appMap = {
                "CM":"c",
                "CMS":"coty",
                "KBD":"cotor_en"
} # key:vale

def getAppVersionName(pkgName):
    cmd = "adb shell dumpsys package " + pkgName + " | grep versionName"
    #x = subprocess.check_output(cmd)
    x = os.popen(cmd)
    return x.read()

def getAppVersionCode(pkgName):
    cmd = "adb shell dumpsys package " + pkgName + " | grep versionCode"
    x = os.popen(cmd)
    #x = subprocess.check_output(["adb","shell","dumpsys","package",pkgName,"|","grep","versionCode"])
    #x.split("=")
    #return sdkVerMap[x[1]]

    result = str(x.read()).split("targetSdk=")
    return result[0] + "support "+sdkVerMap[result[1]] + " 以上"


def getDeviceInfo(pkgName):
    cmd = "adb shell getprop ro.product.model"
    x = os.popen(cmd)
    return x.read()

def getAndroidVersion():
    cmd = "adb shell getprop ro.build.version.release"
    x = os.popen(cmd)
    return "Android " + x.read()

def doGetPkgName(appName):
    try:
        #print(appName)
        appName = appName.upper()
        return appMap[appName]
    except:
        print("似乎打錯囉, 目前提供 CM, CMS, KBD")
        exit(1)
        #appNameA = input("請告訴我想要清除哪一個app1111, 目前提供 CM, CMS, KBD: ")
        #getPkgName(appNameA)

def getPkgName(appName):
    if(checkPara()):
        return doGetPkgName(appName[1])
    else:
        appNameA = input("請告訴我想要清除哪一個app, 目前提供 CM, CMS, KBD: ")
        return doGetPkgName(appNameA)

def checkPara():
    result = 0
    if (len(sys.argv) > 1):
        result = 1
    return result


pkgName = getPkgName(sys.argv)
print(getDeviceInfo(pkgName) + getAndroidVersion() +getAppVersionCode(pkgName))