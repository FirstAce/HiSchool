import requests
r = requests.post('http://ubuntu.hanukoon.com:3000/', json={
    "version": "2.0",
    "action": {
        "actionName": "getSchool",
        "parameters": {
            "scname": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            }
        }
    },
})
print(r.text)
