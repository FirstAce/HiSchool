import requests
r = requests.post('http://0.0.0.0:3000/', json={
    "version": "2.0",
    "action": {
        "actionName": "getSchool",
        "parameters": {
            'scname': {
                'value': '은여울중학교'
            }
        }
    },
})
print(r.text)
