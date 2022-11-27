# sheets
# order of questions 
# change in questions
# scale
# sync
from google_apis import create_service
# Connect to Google Sheets Document
CLIENT_FILE = 'client-secret-desktop.json' #https://developers.google.com/docs/api/quickstart/python 
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
GOOGLE_SHEETS_ID = '1363JR-UGRjis8EX3_TkRCo2ZUmkghhBaR3w8ZJhQL7Q'

service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
print("service created")

import django
import os
import sys
sys.path.insert(1, '/Users/ameer/Documents/udaan/code/demos/google-form-clone')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'form.settings')
django.setup()

from index.models import *
import pprint as pp
def pullSampleData(form_code="hODPn5ZPmHJob6Ti6xcTCNQYAVCIHw"): # P0OQ4Y4rrnVRKSbiv6qjM403FvuguM hODPn5ZPmHJob6Ti6xcTCNQYAVCIHw
  f9=Form.objects.get(code=form_code)
  rs=Responses.objects.filter(response_to=f9)
  cummulative_resp =[]
  headlines=[]
  if rs:
    for r in rs:
      temp={}
      headlines_temp={}
      for ans in r.response.all():
        headlines_temp[ans.answer_to_id] = ans.answer_to.question
        #print(ans.id, ans.answer_to_id)
        if ans.answer_to.question_type == "multiple choice" or ans.answer_to.question_type == "checkbox":
          choice = ans.answer_to.choices.get(id = ans.answer).choice
          #print(choice)
        #print(temp)
        #print("<<",ans.answer_to_id in temp, ans.answer_to.question_type == "multiple choice")
        if ans.answer_to_id in temp and (ans.answer_to.question_type == "multiple choice" or ans.answer_to.question_type == "checkbox") :
          #print(">>temp",temp[ans.answer_to_id])
          #print(">>apend", temp[ans.answer_to_id], choice)
          #print("types:",type(temp[ans.answer_to_id]), type([choice]))
          xtemp = temp[ans.answer_to_id] + ", "+ choice
          temp[ans.answer_to_id]= xtemp
        else:
          if ans.answer_to.question_type == "multiple choice" or ans.answer_to.question_type == "checkbox":
            temp[ans.answer_to_id]=choice
          else:
            temp[ans.answer_to_id]=ans.answer
      #print(list(temp.values()))
      headlines=list(headlines_temp.values())
      cummulative_resp.append(list(temp.values()))
    #ansFirsts =rs.first().response.all().order_by('id')
    # for ans in ansFirsts:
    #   headlines.append(
    #     ans.answer_to.question
    #   )
    #pp.pprint(headlines)
    #print(">>>>")
    pp.pprint(cummulative_resp)
    #print("\n")
  return (list(dict.fromkeys(headlines)), cummulative_resp)

columns, recordset=pullSampleData()
# print(type(columns))
# print(type(recordset))

print("Cleaning Sheet")
# clear data
service.spreadsheets().values().clear(
    spreadsheetId=GOOGLE_SHEETS_ID,
    range='Sheet1'
).execute()

print("Writting Labels")
# insert column labels
service.spreadsheets().values().update(
    spreadsheetId=GOOGLE_SHEETS_ID,
    valueInputOption='USER_ENTERED',
    range='Sheet1!A1',
    body={
        'majorDimension': 'ROWS',
        'values': [columns]
    }
).execute()

print("Writting Data")
#insert dataset to worksheet
service.spreadsheets().values().update(
    spreadsheetId=GOOGLE_SHEETS_ID,
    valueInputOption='USER_ENTERED',
    range='Sheet1!A2',
    body={
        'majorDimension': 'ROWS',
        'values': recordset
    }
).execute()