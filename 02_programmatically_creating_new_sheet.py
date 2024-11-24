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

# creating sheet
response = sheets_service.create(
    body={"properties": {"title": "programmatically_01"}}
).execute()

# print(response)
"""
{'spreadsheetId': '1upgFzfG0nyLwfAQr5uyaVF8kmFfVV_OYa1aXH67u6ko', 'properties': {'title': 'programmatically_01', 'locale': 'en_US', 'autoRecalc': 'ON_CHANGE', 'timeZone': 'Etc/GMT', 'defaultFormat': {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}, 'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3}, 'verticalAlignment': 'BOTTOM', 'wrapStrategy': 'OVERFLOW_CELL', 'textFormat': {'foregroundColor': {}, 'fontFamily': 'arial,sans,sans-serif', 'fontSize': 10, 'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'foregroundColorStyle': {'rgbColor': {}}}, 'backgroundColorStyle': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}, 'spreadsheetTheme': {'primaryFontFamily': 'Arial', 'themeColors': [{'colorType': 'TEXT', 'color': {'rgbColor': {}}}, {'colorType': 'BACKGROUND', 'color': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}, {'colorType': 'ACCENT1', 'color': {'rgbColor': {'red': 0.25882354, 'green': 0.52156866, 'blue': 0.95686275}}}, {'colorType': 'ACCENT2', 'color': {'rgbColor': {'red': 0.91764706, 'green': 0.2627451, 'blue': 0.20784314}}}, {'colorType': 'ACCENT3', 'color': {'rgbColor': {'red': 0.9843137, 'green': 0.7372549, 'blue': 0.015686275}}}, {'colorType': 'ACCENT4', 'color': {'rgbColor': {'red': 0.20392157, 'green': 0.65882355, 'blue': 0.3254902}}}, {'colorType': 'ACCENT5', 'color': {'rgbColor': {'red': 1, 'green': 0.42745098, 'blue': 0.003921569}}}, {'colorType': 'ACCENT6', 'color': {'rgbColor': {'red': 0.27450982, 'green': 0.7411765, 'blue': 0.7764706}}}, {'colorType': 'LINK', 'color': {'rgbColor': {'red': 0.06666667, 'green': 0.33333334, 'blue': 0.8}}}]}}, 'sheets': [{'properties': {'sheetId': 0, 'title': 'Sheet1', 'index': 0, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}], 'spreadsheetUrl': 'https://docs.google.com/spreadsheets/d/1upgFzfG0nyLwfAQr5uyaVF8kmFfVV_OYa1aXH67u6ko/edit'}
"""

sheet_id = response.get("spreadsheetId")
print(sheet_id)

# insert a new value into sheet
sheets_service.values().append(
    spreadsheetId=sheet_id,
    range="Sheet1!A1",
    valueInputOption="RAW",
    body={"values": [["testing"]]},
).execute()


# get the value back
sheets_service.values().get(
    spreadsheetId=sheet_id,
    range="Sheet1!A1",
).execute()
