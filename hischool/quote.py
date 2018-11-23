from py_translator import Translator
import json, requests

def parseQuote(lang='en'):
    data = requests.get("https://talaikis.com/api/quotes/random/").text
    pdata = json.loads(data)
    if lang == 'ko':
        tran = Translator()
        return {
            'quote': tran.translate(pdata['quote'], src='en', dest='ko').text, 
            'author': tran.translate(pdata['author'], src='en', dest='ko').text
        }
    return {
        'en-quote': pdata['quote'], 
        'en-author': pdata['author']
    }

if __name__ == '__main__':
    text = parseQuote()
    print(text)
