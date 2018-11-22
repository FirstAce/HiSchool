import json, requests, re, urllib.parse
from bs4 import BeautifulSoup

sc_meals = {
    "아침": 1,
    "점심": 2,
    "저녁": 3
}

sc_types = {
    "유치원": 1,
    "초등학교": 2,
    "중학교": 3,
    "고등학교": 4
}

sc_offices = {
    "서울": "stu.sen.go.kr",
    "부산": "stu.pen.go.kr",
    "대구": "stu.dge.go.kr",
    "인천": "stu.ice.go.kr",
    "광주": "stu.gen.go.kr",
    "대전": "stu.dje.go.kr",
    "울산": "stu.use.go.kr",
    "세종": "stu.sje.go.kr",
    "경기": "stu.goe.go.kr",
    "강원": "stu.kwe.go.kr",
    "충청북": "stu.cbe.go.kr",
    "충청남": "stu.cne.go.kr",
    "전라북": "stu.jbe.co.kr",
    "전라남": "stu.jne.go.kr",
    "경상북": "stu.kbe.go.kr",
    "경상남": "stu.gne.go.kr",
    "제주": "stu.jje.go.kr"
}

def getSchoolType(name):
    for key in sc_types:
        if key in name:
            return sc_types[key]

def getEduOfficeURL(address):
    addr = address.split(' ')[0]
    for key in sc_offices:
        if key in addr:
            return sc_offices[key]

def searchSchool(query):
    html = requests.post('https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do', 
        data={ 'criteria': 'pageIndex=1&bsnmNm=' + urllib.parse.quote_plus(quary) }).text
    for result in BeautifulSoup(html, 'html.parser').find_all('tbody')[1].find_all('tr'):
        search_item = [data.string for data in result.find_all('td')]
        search_result = {
            'name': search_item[1],
            'sccode': search_item[2],
            'address': search_item[3],
        }
        break
    search_result['type'] = getSchoolType(search_result['name'])
    search_result['office'] = getEduOfficeURL(search_result['address'])
    return search_result

def getMeal(school_info):
    pass
    
if __name__ == '__main__':
    result = searchSchool('한국디지털미디어고')
    print(result)
