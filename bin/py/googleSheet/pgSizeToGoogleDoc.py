import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials

apkName = sys.argv[1]
apkSize = sys.argv[2]

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('PGAndroid-c94ec83c3089.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("pg_android_apk_size")
sheet = wks.worksheet('dev')
sheet.append_row([apkName,apkSize])
