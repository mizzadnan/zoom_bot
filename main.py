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
