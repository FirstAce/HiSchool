import requests
r = requests.post('http://0.0.0.0:3000/getMeal', json={
    "version": "2.0",
    "action": {
        "actionName": "getMeal",
        "parameters": {
            "query": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            },
            "meal_type": {
                "type": "BID_TI_DURATION",
                "value": "점심"
            },
            "days": {
                "type": "BIT_DT_DAY",
                "value": "오늘"
            }
        }
    },
})
print(r.text)
