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
drive_service = build("drive", "v3", credentials=creds)

# creating instance of the service
sheets_service: Resource = build("sheets", "v4", credentials=creds).spreadsheets()

# creating sheet
response = sheets_service.create(
    body={"properties": {"title": "programmatically_01"}}
).execute()

sheet_id = response.get("spreadsheetId")
sheet_url = response.get("spreadsheetUrl")

# insert a new value into sheet
sheets_service.values().append(
    spreadsheetId=sheet_id,
    range="Sheet1!A1",
    valueInputOption="RAW",
    body={"values": [["testing", "testing 1123"]]},
).execute()


drive_response = (
    drive_service.permissions()
    .create(
        fileId=sheet_id,
        body={
            "role": "writer",
            "type": "user",
            "emailAddress": "endang.ismaya@gmail.com",
        },
        fields="id",
    )
    .execute()
)

print(drive_response)

print("sheet_url: ", sheet_url)
