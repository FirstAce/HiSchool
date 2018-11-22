import json, requests
def quote():
    data = requests.get("https://talaikis.com/api/quotes/random/").text
    pdata = json.loads(data)
    text1 = pdata['quote'] + " by " + pdata['author']
    return text1

if __name__ == '__main__':
    text = quote()
    print(text)
