from hischool import app
from hischool.database import *
from hischool.api import *
from flask import (
    render_template,
    redirect,
    request,
    abort,
    url_for,
    session
)

@app.route('/health')
def healthCheck():
    return 'OK'

@app.route('/', methods=['GET', 'POST'])
def home():
    req = request.json
    print(request.json)
    if req['action']['actionName'] == 'getMeal':
        return getMeal(req)
    elif req['action']['actionName'] == 'getQuote':
        return getQuote()
    return ''
