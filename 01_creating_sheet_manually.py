from googleapiclient.discovery import build, Resource
from google.oauth2.service_account import Credentials


# Creating credentials
creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)

# creating instance of the service
sheets_service: Resource = build("sheets", "v4", credentials=creds).spreadsheets()

# sheet_id (create manually thru gsheet gui and take the ID)
sheet_id = "1WApbKMIGhhmm3Cer-jL8ogP5mIrbbfcOGmVGLHbGHsc"

# insert a new value into sheet
sheets_service.values().append(
    spreadsheetId=sheet_id,
    range="Sheet1!A1",
    valueInputOption="RAW",
    body={"values": [["testing"]]},
).execute()
