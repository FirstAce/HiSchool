from hischool.meal import parseMeal
from hischool.quote import parseQuote
from hischool.schedule import parseSchedule
import json

def getMeal(req):
    query = req['action']['parameters']['query']['value']
    meal_type = req['action']['parameters']['meal_type']['value']
    meal_type = {
        'DAWN': 1,
        'MORNING': 1,
        '점심': 2,
        'DAY': 2,
        'NOON': 2,
        'EVENING': 3,
        'EARLYBIRD': 3,
        'NIGHT': 3,
        'MIDNIGHT': 3
    }[meal_type]
    days = req['action']['parameters']['days']['value'] 
    days = {
        'B_YESTERDAY': -2, 
        'YESTERDAY': -1, 
        'TODAY': 0, 
        'TOMORROW': 1, 
        'A_TOMORROW': 2, 
        'AA_TOMORROW': 3
    }[days]
    meal, q_date, q_type = parseMeal(query, meal_type, days)
    if meal:
        meal = q_date + '의 ' + q_type + '은 ' + ', '.join(meal) + '입니다.'
    else:
        meal = q_date + '에는 ' + q_type + '이 없습니다.'
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': {
            'meal': meal
        } 
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)

def getSchedule(req):
    query = req['action']['parameters']['name']['value']
    query_month = int(req['action']['parameters']['month']['value']) # DT_YMONTH
    this = parseSchedule(query, query_month)
    try:
        this = {k: v.replace('\n\n', ' 그리고 ') for k, v in this.items() if v}
        result = ', '.join([str(key) + '일은 ' + this[key] for key in this])
        result = str(query_month) + '월 일정입니다. ' + result + '입니다.'
    except:
        result = this
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': {
            'schedule': result
        } 
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)

def getKorQuote():
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': parseQuote(lang='ko')
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)

def getEngQuote():
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': parseQuote()
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)
