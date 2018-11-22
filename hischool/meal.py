import json, requests, re, urllib.parse
from bs4 import BeautifulSoup
from datetime import date, timedelta

sc_types = {
    "유치원": "01",
    "초등학교": "02",
    "중학교": "03",
    "고등학교": "04"
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
        data={ 'criteria': 'pageIndex=1&bsnmNm=' + urllib.parse.quote_plus(query) }).text
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

def getMealTableURL(school_info, meal_type, query_date):
    # (dict)school_info, (int)meal_type, (date obj / 'yyyy.mm.dd' formatted string)query_date
    if type(query_date) == date:
        query_date = query_date.today().strftime('%Y.%m.%d')
    elif type(query_date) != str:
        return False
    return (
        'http://' + school_info['office'] + '/sts_sci_md01_001.do?' # school office
        'schulCode=' + school_info['sccode'] + # school code 
        '&schulCrseScCode=' + str(int(school_info['type'])) + # school type -> 1 digit
        '&schulKndScCode=' + school_info['type'] + # school kind
        '&schMmealScCode=' + str(meal_type) + # school meal_type (1: 아침, 2: 점심, 3: 저녁)
        '&schYmd=' + query_date # 'yyyy.mm.dd' formatted string
    )

def getMeal(query, meal_type, days): 
    # query: keyword to search school name
    # meal_type: in [1, 2, 3]
    # days: how many days to query from now?

    school = searchSchool(query)
    query_date = date.today() + timedelta(days=days)
    day = query_date.weekday() + 1
    URL = getMealTableURL(school, meal_type, query_date)

    # https://github.com/junhoyeo/eunyeoul-chatbot-flask/blob/master/mealparser.py
    # using what I coded before: optimise later(todo)
    html = requests.get(URL).text # 생성한 URL의 html 저장
    soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup 객체 생성
    data = soup.find_all('tr')[2].find_all('td') # 식단표 부분 데이터만 찾아서 저장
    try:
        data = str(BeautifulSoup(html, 'html.parser').find_all('tr')[2].find_all('td')[day])
        for filter_data in ['[', ']', '<td class="textC">', '<td class="textC last">', '</td>', '.']:
            data = data.replace(filter_data, '') # filter html tags
        data = data.split('<br/>')
        data = data[:len(data)-1]
        for idx, item in enumerate(data):
            for char in reversed(item):
                if char.isdigit(): data[idx] = data[idx][:-1]
                else: break
                # crop allergy infomation so it do not damage things like '바나나우유(500ml)'
        return data
    except:
        return None

if __name__ == '__main__':
    print(getMeal('은여울중학교', 2, 0))
