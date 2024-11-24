from googleapiclient.discovery import build


class GoogleSheetService:
    def __init__(self, creds):
        self.sheets_service = build("sheets", "v4", credentials=creds).spreadsheets()
        self.drive_service = build("drive", "v3", credentials=creds)
