import json, requests

with open('./school.json', 'r') as f:
    schooldata = json.loads(f.read())

import re, requests, urllib.parse
from bs4 import BeautifulSoup

def searchSchool(quary):
    html = requests.post('https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do', 
        data={ 'criteria': 'pageIndex=1&bsnmNm=' + urllib.parse.quote_plus(quary) }).text
    search_result = []
    for result in BeautifulSoup(html, 'html.parser').find_all('tbody')[1].find_all('tr'):
        search_item = [data.string for data in result.find_all('td')]
        search_result.append({
            'name': search_item[1],
            'sccode': search_item[2],
            'address': search_item[3],
        })
    return search_result

def getSchoolType(name):
    for key in schooldata['구분']:
        if key in name:
            return schooldata['구분'][key]

def getEduOfficeURL(address):
    addr = address.split(' ')[0]
    for key in schooldata['교육청']:
        if key in addr:
            return schooldata['교육청'][key]

if __name__ == '__main__':
    result = searchSchool('신촌')
    print(result[0])
    print(getSchoolType(result[0]['name']))
    print(getEduOfficeURL(result[0]['address']))
