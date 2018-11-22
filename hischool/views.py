from hischool import app
from hischool.database import *
from hischool.meal import getMeal
from flask import (
    render_template,
    redirect,
    request,
    abort,
    url_for,
    session
)
import json

@app.route('/health')
def healthCheck():
    return 'OK'
    
@app.route('/getMeal', methods=['POST'])
def meal():
    req = request.json
    query = req['action']['parameters']['query']['value']
    meal_type = req['action']['parameters']['meal_type']['value']
    days = req['action']['parameters']['days']['value']
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': {} 
    }
    resp['output']['meal'] = '\n'.join(getMeal(query, meal_type, days))
    return json.dumps(resp, ensure_ascii=False, indent=4)
