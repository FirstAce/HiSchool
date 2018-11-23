from py_translator import Translator
import json, requests

def parseQuote():
    tran = Translator()
    data = requests.get("https://talaikis.com/api/quotes/random/").text
    pdata = json.loads(data)
    return {
        'quote': tran.translate(pdata['quote'], src='en', dest='ko').text, 
        'author': tran.translate(pdata['author'], src='en', dest='ko').text
    }

if __name__ == '__main__':
    text = parseQuote()
    print(text)
