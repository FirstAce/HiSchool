from hischool import app
from hischool.db import *
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
    
@app.route('/getMeal/<school>', methods=['GET', 'POST'])
def meal():
    # req = request.json
    resp = { 
        'version': '2.0', 
        'resultCode': 'OK',
        'output': {} 
    }
    resp['output']['meal'] = getMeal()
    return json.dumps(resp, ensure_ascii=False, indent=4)
