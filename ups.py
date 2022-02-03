from bs4 import BeautifulSoup as bs4
import requests
import json


def walmart_get_upc(url):
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    req = requests.get(url, headers=HEADERS)
    html = bs4(req.content, 'html.parser')
    tag_script = str(html.select('.tb-optimized'))[64:-10]

    if tag_script == []:
        print('\n[!] UPC not found\n')
        return

    json_file = json.loads(tag_script)    
    upc_code = json_file['item']['product']['buyBox']['products'][0]['upc']

    return upc_code