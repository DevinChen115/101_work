from __future__ import print_function
import httplib2

from apiclient import discovery
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.http import MediaFileUpload
from apiclient import errors


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
credentials = ServiceAccountCredentials.from_json_keyfile_name('FabricParser-8be73c6c3ce6.json', SCOPES)
http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v2', http=http)


def upload():
    file_body = { 
        "title": "devin.apk",
        "mimeType": "application/vnd.android.package-archive",
        "parents": [{
            "id": "0Bz0SNDEIlvzKdVA0bU5PNGpGVXM"
        }]
    }
    media = MediaFileUpload('jp.co.MitsubishiElectric.VCP02_2015-07-13.apk', 
                            mimetype='application/vnd.android.package-archive',
                            resumable=True)
    file = drive_service.files().insert(body=file_body,
                                        media_body=media,
                                        fields='id').execute()
    # print ('File ID: %s' % file.get('id'))

    setPermission(file.get('id'))
    print(getFileURL(file.get('id')))


def setPermission(fileid):
    share_permission = {
        "withLink": "true",
        "role": "reader",
        "type": "anyone"
    }
    try:
        return drive_service.permissions().insert(fileId=fileid, body=share_permission).execute()
    except errors.HttpError, error:
        print ('An error occurred: %s' % error)
    return None


# def listFile():
#     # file = drive_service.files().list()
#     # print(file)

#     result = []
#     page_token = None
#     while True:
#         try:
#             param = {}
#             if page_token:
#                 param['pageToken'] = page_token
#             files = drive_service.files().list(**param).execute()

#             result.extend(files['items'])
#             page_token = files.get('nextPageToken')
#             if not page_token:
#                 break
#         except errors.HttpError, error:
#             print('An error occurred: %s' % error)
#             break
#     print(result)


def getFileURL(fileid):
    file = drive_service.files().get(fileId=fileid).execute()
    return file.get('alternateLink')


if __name__ == '__main__':
    upload()
