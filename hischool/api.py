from hischool.meal import parseMeal
from hischool.quote import parseQuote
import json

def getMeal(req):
    query = req['action']['parameters']['query']['value']
    meal_type = req['action']['parameters']['meal_type']['value']
    meal_type = {
        'MORNING': 1,
        '점심': 2,
        'EVENING': 3
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
    meal = parseMeal(query, meal_type, days)
    meal = ', '.join(meal) + '입니다.' if meal else '급식이 없습니다.'
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': {
            'meal': meal
        } 
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)

def getQuote():
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': parseQuote()
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)
