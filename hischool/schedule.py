from datetime import date, timedelta
from hischool.meal import *
import re

def getScheduleURL(school_info, q_year, q_month):
    return (
        'http://' + school_info['office'] + '/sts_sci_sf00_001.do?' # school office
        'schulCode=' + school_info['sccode'] + # school code 
        '&schulCrseScCode=' + str(int(school_info['type'])) + # school type -> 1 digit
        '&schulKndScCode=' + school_info['type'] + # school kind
        '&ay=' + str(q_year) + '&mm=' + str(q_month)
    )

def parseSchedule(query, query_month): 
    query_year = date.today().year
    school = School.query.filter_by(keyword=query).first()
    if school:
        school = school.data 
    else:
        school = searchSchool(query)
        try:
            db.session.add(School(keyword=query, data=school))
            db.session.commit()
        except:
            print('[*] DB commit error')
    URL = getScheduleURL(school, query_year, query_month)
    # print(URL)
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select('tr')

    # https://github.com/w3bn00b/tanbang-cafeteria/blob/master/tCafeteria.py
    # Copyright(MIT) (c) 2017 w3bn00b, return0927
    schedules = {}

    months = [ tag.text for tag in rows[0].find_all("th", attrs={"colspan":"2"}) ]
    months = [ int(x[:-1]) for x in months ]
    docYear = soup.select_one("select#grade").text.strip() # 받아 온 문서 상의 연도
    docYear = int(docYear)
    schedules[docYear] = {}

    for month in months:
        schedules[docYear][month] = {} # 각 별로 딕셔너리 지정

    for j in range(len(rows[1:])):
        tr = rows[1:][j]
        _legacy = [x.text.strip() for x in tr.find_all("td", attrs={"class": "textL"})] # 임시로 배열 저장
        for n in range(len(months)):
            schedules[docYear][months[n]][j+1] = _legacy[n] # 스케쥴 등록
    try:
        result = schedules[query_year][query_month]

        result = {k: v for k, v in result.items() if v not in ['여름방학', '하계방학기간', '겨울방학', '동계방학기간']}
        # 처리하지 않을 경우 아래와 같은 결과:
        # 1월 일정입니다. 1일은 신정, 3일은 겨울방학식, 4일은 겨울방학, 5일은 겨울방학 그리고 토요휴업일, 6일은 겨울방학, 7일은 겨울방학, 8일은 겨울방학, 9일은 겨울방학, 10일은 겨울방학, 11일은 겨울방학, 12일은 겨울방학 그리고 토요휴업일, 13일은 겨울방학, 14일은 겨울방학, 15일은 겨울방학, 16일은 겨울방학, 17일은 겨울방학, 18일은 겨울방학, 19일은 겨울방학 그리고 토요휴업일, 20일은 겨울방학, 21일은 겨울방학, 22일은 겨울방학, 23일은 겨울방학, 24일은 겨울방학, 25일은 겨울방학, 26일은 겨울방학 그리고 토요휴업일, 27일은 겨울방학, 28일은 겨울방학, 29일은 겨울방학, 30일은 개학식입니다.
        return result
    except:
        return '일정 정보가 존재하지 않습니다. ' + ', '.join([str(i) + '월' for i in months]) + ' 중 하나로 찾아보세요.'

if __name__ == '__main__':
    school_info = {'name': '은여울중학교', 'sccode': 'J100006779', 'address': '경기도 김포시 김포한강8로 173-48 (마산동)', 'type': '03', 'office': 'stu.goe.go.kr'}
    getScheduleURL(school_info, date.today())
