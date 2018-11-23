# import requests
# r = requests.post('http://0.0.0.0:3000/', json={
#     "version": "2.0",
#     "action": {
#         "actionName": "getQuote",
#         "parameters": {}
#     },
# })
# print(r.text)
from hischool.schedule import *
r = parseSchedule('선린인', 11)
print(r)

