from __future__ import print_function
import httplib2

from apiclient import discovery
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import os
import datetime

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json

CalendarTitle = os.environ['CalendarTitle']
Calendar_Start = os.environ['Calendar_Start']
# Calendar_End = os.environ['Calendar_End']
Calendar_End = datetime.datetime.strptime(Calendar_Start, "%Y-%m-%d") + datetime.timedelta(days = 1)
Calendar_End = Calendar_End.strftime("%Y-%m-%d")
Release_Day = Calendar_Start.replace("-", "/")
Release_Version = os.environ['Release_Version']
Release_Type = os.environ['Release_Type']
Release_Percentage = os.getenv('Release_Percentage')
Auto_Upgrade = os.getenv('Auto_Upgrade')
Sticker = os.getenv('Sticker')
Change_log = os.getenv('Change_log')
Size = os.getenv('Size')
Address = os.getenv('Address')

def calendarAddEvent():
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('FabricParser-8be73c6c3ce6.json', SCOPES)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    event = {
        "summary": CalendarTitle,
        "start": {
            "date": Calendar_Start
        },
        "end": {
            "date": Calendar_End
        }
    }
    event = service.events().insert(calendarId='conew.com_lkv6cfa084eb12ad5ere83m37k@group.calendar.google.com', body=event).execute()
    print ('Calendar Event created: %s' % (event.get('status') + "\n" + event.get('htmlLink')))


def addSheet():
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    RANGE = 'PG_Android!A2:K'
    spreadsheet_id = '19INfvzcS0ThpHeaoqeOOrBazrZBvJ38_umOSxUnGyt4'
    value_input_option = 'USER_ENTERED'

    value_range_body = {
        'values': [
            [Release_Day, 'PhotoGrid', Release_Version, Release_Type, 'success', Release_Percentage, Auto_Upgrade, Sticker, Change_log, Size, Address]
        ]
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_name('FabricParser-8be73c6c3ce6.json', SCOPES)
    http = credentials.authorize(httplib2.Http())
    # discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http)  # , discoveryServiceUrl=discoveryUrl)
    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=RANGE, valueInputOption=value_input_option, body=value_range_body)
    response = request.execute()
    print ('Sheet appened: %s' % (response.get('updates').get('updatedCells')))


if __name__ == '__main__':
    calendarAddEvent()
    addSheet()
