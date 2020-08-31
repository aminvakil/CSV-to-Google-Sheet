import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.service_account('client_secret.json')

spreadsheet = gc.open('TEST SHEET')

# Read CSV file contents
content = open('data.csv', 'r').read()

gc.import_csv(spreadsheet.id, content)
