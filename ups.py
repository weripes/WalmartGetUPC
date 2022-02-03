from bs4 import BeautifulSoup as bs4
import requests
import json


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = "https://www.walmart.com/ip/Lasko-Limited-Edition-20-Box-Fan-with-3-Speeds-B20610-Red-White-Blue/404928050?athcpid=404928050&athpgid=athenaHomepage&athcgid=dealspage-home-4446685&athznid=ItemCarouselType_BestInDeals&athieid=v1&athstid=CS020&athguid=466001f5-9a18a716-bed495689f15260d&athancid=null&athena=true"

url2 = 'https://www.walmart.com/ip/Midea-5-000-BTU-115V-Mechanical-Window-Air-Conditioner-MAW05M1WWT/212092810?athcpid=212092810&athpgid=athenaHomepage&athcgid=dealspage-home-4446685&athznid=ItemCarouselType_BestInDeals&athieid=v1&athstid=CS020&athguid=466001f5-9a18a716-89c28f1b9f15260d&athancid=null&athena=true'
url3 = 'https://www.walmart.com/ip/Midea-7-000-BTU-10-000-BTU-ASHRAE-115V-Portable-Air-Conditioner-with-ComfortSense-Remote-White-MAP07R1WWT/238274032?athcpid=238274032&athpgid=athenaItemPage&athcgid=null&athznid=PWVAV&athieid=v0&athstid=CS020&athguid=182e9217-007-17b06df3f1c89e&athancid=null&athena=true'
req = requests.get(url3, headers=HEADERS)

html = bs4(req.content, 'html.parser')



js = str(html.select('.tb-optimized'))[64:-10]

js = json.loads(js)


def walmart_get_upc(json_file):
    return json_file['item']['product']['buyBox']['products'][0]['upc']
    
print(walmart_get_upc(js))