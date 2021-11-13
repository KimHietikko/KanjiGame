import sys

import gspread
import random
import keyboard

from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Kanji").sheet1

while True:
    try:
        row = random.uniform(2, 2034)

        kanjicell = sheet.cell(row, 1).value
        meaningcell = sheet.cell(row, 3).value
        romajicell = sheet.cell(row, 4).value

        pprint(kanjicell)

        romaji = input("Write in romaji: ")

        if keyboard.is_pressed('q'):
            print("\nyou pressed Esc, so exiting...")
            break

        if romaji == romajicell:
            print("Good job!")
            print(kanjicell + " means: " + meaningcell)

        else:
            print("Correct answer was: " + romajicell)
            print(kanjicell + " means: " + meaningcell)

        print("--------------------------------------------------------")

    except:
        break
