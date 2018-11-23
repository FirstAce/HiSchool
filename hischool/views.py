from hischool import app
from hischool.database import *
from hischool.meal import getMeal
from hischool.quote import getQuote
from flask import (
    render_template,
    redirect,
    request,
    abort,
    url_for,
    session
)
import json

def healthCheck():
    return 'OK'

def meal(req):
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
    meal = getMeal(query, meal_type, days)
    meal = ', '.join(meal) + '입니다.' if meal else '급식이 없습니다.'
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': {
            'meal': meal
        } 
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)

def quote():
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': quote()
    }
    return json.dumps(resp, ensure_ascii=False, indent=4)

@app.route('/', methods=['GET', 'POST'])
def home():
    req = request.json
    print(request.json)
    if req['action']['actionName'] == 'health':
        return healthCheck()
    elif req['action']['actionName'] == 'getMeal':
        return meal(req)
    return ''
