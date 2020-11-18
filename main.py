# importing the required modules

import pyautogui
import subprocess
from datetime import datetime
from time import sleep

# zoom ids and passes for every day of the week

saturday = {"9207344064": "4dak8E", "4078407985": "tu@rumc", "2943572024": "szk@rumc"}  # SB TU SZK
sunday = {"9443918403": "nc@rumc", "4096669370": "gcs@rumc", "5887996472": "mhb@rumc"}  # NC GCS MHB
monday = {"6199024532": "mni@rumc", "4078407985": "tu@rumc", "9713219788": "yk@rumc"}  # MNI TU YK
tuesday = {"3187225592": "ms@rumc", "6442635633": "fr@rumc", "8068605560": "mzi@rumc"}  # MS FR MZI
wednesday = {"6166730587": "rai@rumc", "9713219788": "yk@rumc", "2134182170": "frn@rumc"}  # RAI YK FRN
thursday = {"6494909022": "aa@rumc", "8597574150": "mrn@rumc", "3187225592": "ms@rumc"}  # AA MRN MS

# zoom ids

saturday_ids = list(saturday.keys())
sunday_ids = list(sunday.keys())
monday_ids = list(monday.keys())
tuesday_ids = list(tuesday.keys())
wednesday_ids = list(wednesday.keys())
thursday_ids = list(thursday.keys())

# zoom passwords

saturday_pass = list(saturday.values())
sunday_pass = list(sunday.values())
monday_pass = list(monday.values())
tuesday_pass = list(tuesday.values())
wednesday_pass = list(wednesday.values())
thursday_pass = list(thursday.values())

first = False
second = False
third = False

now = datetime.now()
current_day = now.strftime("%A")

# if statements for each day

if current_day == "Saturday":
    while not first:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if current_hour == "11" and current_minute <= 40:
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(saturday_ids[0])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(saturday_pass[0])
            pyautogui.press("enter")
            first = True
        else:
            continue

    while not second:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "11" and current_minute >= 50) or (current_hour == "12" and current_minute <= 30):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(saturday_ids[1])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(saturday_pass[1])
            pyautogui.press("enter")
            second = True
        else:
            continue

    while not third:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "12" and current_minute >= 40) or (current_hour == "13" or current_minute <= 20):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(saturday_ids[2])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(saturday_pass[2])
            pyautogui.press("enter")
            third = True
        else:
            continue

elif current_day == "Sunday":
    while not first:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if current_hour == "11" and current_minute <= 40:
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(sunday_ids[0])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(sunday_pass[0])
            pyautogui.press("enter")
            first = True
        else:
            continue

    while not second:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "11" and current_minute >= 50) or (current_hour == "12" and current_minute <= 30):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(sunday_ids[1])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(sunday_pass[1])
            pyautogui.press("enter")
            second = True
        else:
            continue

    while not third:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "12" and current_minute >= 40) or (current_hour == "13" or current_minute <= 20):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(sunday_ids[2])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(sunday_pass[2])
            pyautogui.press("enter")
            third = True
        else:
            continue

elif current_day == "Monday":
    while not first:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if current_hour == "11" and current_minute <= 40:
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(monday_ids[0])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(monday_pass[0])
            pyautogui.press("enter")
            first = True
        else:
            continue

    while not second:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "11" and current_minute >= 50) or (current_hour == "12" and current_minute <= 30):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(monday_ids[1])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(monday_pass[1])
            pyautogui.press("enter")
            second = True
        else:
            continue

    while not third:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "12" and current_minute >= 40) or (current_hour == "13" or current_minute <= 20):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(monday_ids[2])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(monday_pass[2])
            pyautogui.press("enter")
            third = True
        else:
            continue

elif current_day == "Tuesday":
    while not first:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if current_hour == "11" and current_minute <= 40:
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(tuesday_ids[0])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(tuesday_pass[0])
            pyautogui.press("enter")
            first = True
        else:
            continue

    while not second:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "11" and current_minute >= 50) or (current_hour == "12" and current_minute <= 30):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(tuesday_ids[1])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(tuesday_pass[1])
            pyautogui.press("enter")
            second = True
        else:
            continue

    while not third:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "12" and current_minute >= 40) or (current_hour == "13" or current_minute <= 20):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(tuesday_ids[2])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(tuesday_pass[2])
            pyautogui.press("enter")
            third = True
        else:
            continue

elif current_day == "Wednesday":
    while not first:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if current_hour == "11" and current_minute <= 40:
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(wednesday_ids[0])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(wednesday_pass[0])
            pyautogui.press("enter")
            first = True
        else:
            continue

    while not second:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "11" and current_minute >= 50) or (current_hour == "12" and current_minute <= 30):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(wednesday_ids[1])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(wednesday_pass[1])
            pyautogui.press("enter")
            second = True
        else:
            continue

    while not third:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "12" and current_minute >= 40) or (current_hour == "13" or current_minute <= 20):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(wednesday_ids[2])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(wednesday_pass[2])
            pyautogui.press("enter")
            third = True
        else:
            continue

elif current_day == "Thursday":
    while not first:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if current_hour == "11" and current_minute <= 40:
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(thursday_ids[0])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(thursday_pass[0])
            pyautogui.press("enter")
            first = True
        else:
            continue

    while not second:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "11" and current_minute >= 50) or (current_hour == "12" and current_minute <= 30):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(thursday_ids[1])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(thursday_pass[1])
            pyautogui.press("enter")
            second = True
        else:
            continue

    while not third:
        current_hour = now.strftime("%H")
        current_minute = int(now.strftime("%M"))
        if (current_hour == "12" and current_minute >= 40) or (current_hour == "13" or current_minute <= 20):
            subprocess.Popen([r"C:\Users\mirza\AppData\Roaming\Zoom\bin\Zoom.exe"])
            sleep(10)
            join_btn = pyautogui.locateOnScreen(r".\img\join.png", confidence=0.7)
            x, y = pyautogui.center(join_btn)
            pyautogui.click(x, y)
            sleep(3)
            pyautogui.typewrite(thursday_ids[2])
            pyautogui.press("enter")
            sleep(3)
            pyautogui.typewrite(thursday_pass[2])
            pyautogui.press("enter")
            third = True
        else:
            continue










