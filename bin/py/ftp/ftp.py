from ftplib import FTP
import os

HOST = '10.33.142.21'
ACCOUNT = 'pgrw'
PWD = os.getenv('PWD') + 'a123'
PGVersion = os.getenv('PGVersion')
fileName = os.getenv('fileName')
filePath = os.getenv('filePath')
ftp = None


def main():
    connectToFTP()
    if(isFolderHave()):
        uploadFile()
    else:
        createFolder()
        uploadFile()


def connectToFTP():
    global ftp
    try:
        ftp = FTP(HOST)
        ftp.login(ACCOUNT, PWD)
    except:
        print ('ERROR:cannot reach " %s"' % HOST)
        return
    print ('Connected to host "%s"' % HOST + ' Success')


def isFolderHave():
    list = ftp.nlst()
    for name in list:
        if(name == PGVersion):
            return True
        else:
            continue
    return False


def createFolder():
    ftp.mkd(PGVersion)


def uploadFile():
    try:
        with open(filePath + fileName) as contents:
            ftp.cwd(PGVersion)
            ftp.storbinary('STOR %s' % fileName, contents)
        print('Upload " %s"' % fileName + ' Success')
    except Exception as e:
        print(e)
        print('ERROR:cannot upload " %s"' % fileName)
    ftp.close()


if __name__ == '__main__':
    main()
