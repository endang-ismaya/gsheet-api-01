from google.oauth2.service_account import Credentials
from app.services.google_sheets import GoogleSheetService

# Creating credentials
creds = Credentials.from_service_account_file(
    "app/credentials/credentials.json",
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)

gservice = GoogleSheetService(creds=creds)


def get_google_service():
    return gservice
