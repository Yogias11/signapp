#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:22:38 2019

@author: awangga
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# In[]:
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sprdfile = client.open("2019Proyek2")
npm="113040087"
pertemuan="pertemuan4"
nilai=45
komentar="terus kerjakan sampai sudah di ujung dan berhasil"
tanggal="7 januari 2019"
sprdfile.get_worksheet(0).update_cell(sprdfile.get_worksheet(0).find(npm).row, sprdfile.get_worksheet(0).find(pertemuan).col, nilai)
sprdfile.get_worksheet(1).update_cell(sprdfile.get_worksheet(1).find(npm).row, sprdfile.get_worksheet(1).find(pertemuan).col, komentar)
sprdfile.get_worksheet(2).update_cell(sprdfile.get_worksheet(2).find(npm).row, sprdfile.get_worksheet(2).find(pertemuan).col, tanggal)
# In[]:
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

# In[]:
sheet.row_values(1)
# In[]:
sheet.col_values(1)
# In[]:
sprdfile.get_worksheet(0).cell(1, 1).value
# In[]:
sheet.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")
# In[]:

row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
index = 1
sheet.insert_row(row, index)
# In[]:
sheet.delete_row(1)
# In[]:
sheet.row_count
# In[]:
cell=sheet.find("113040087")
print("Found something at R%sC%s" % (cell.row, cell.col))

# In[]:
npm="113040087"
pertemuan="pertemuan5"
sheet.update_cell(sheet.find(npm).row, sheet.find(pertemuan).col, "7 januari 2019")
# In[]:
