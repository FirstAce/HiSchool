import requests
r = requests.post('http://0.0.0.0:3000/getMeal', json={
    "version": "2.0",
    "action": {
        "actionName": "getMeal",
        "parameters": {
            "query": {
                "type": "string",
                "value": "은여울중학교"
            },
            "meal_type": {
                "type": "int",
                "value": 2
            },
            "days": {
                "type": "string",
                "value": 0
            }
        }
    }
})
print(r.text)
