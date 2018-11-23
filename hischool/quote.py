import json, requests
def getQuote():
    data = requests.get("https://talaikis.com/api/quotes/random/").text
    pdata = json.loads(data)
    return {
        'quote': pdata['quote'], 
        'author': pdata['author']
    }

if __name__ == '__main__':
    text = quote()
    print(text)
