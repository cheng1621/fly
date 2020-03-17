
import requests
import time
session = requests.session()
header = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome /63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400',
        'Host': 'www.nitrafficindex.com',
        'Referer': 'http://www.nitrafficindex.com/trafficIndexAnalysis.html',
        'X-Requested-With':'XMLHttpRequest',
        'Accept':'application/json, text/javascript, */*',
        # 'Content-Type':'application/x-www-form-urlencoded',
        'Content-Type':'application/x-www-form-urlencoded',
        'Origin':'http://www.nitrafficindex.com'
    }
queryParams =  {
            'areaCode':'110000',
            # 'roadLevel':'1%2C2%2C3%2C4',
            'roadLevel':'1,2,3,4',
            # 'roadLevel':'1100000jian4guo2men2nei4da4jie1',
            'page':'1',
            'rows':'1000'
        }
# Cookie = [('JSESSIONID','JSESSIONID=92AF4B2E099D4E3F522640C564D32AE1')]
# Cookie = [('JSESSIONID','FA25F8C2696C615BBF37CD')]
# Cookie = dict(Cookie)
start_time = time.time()
r = session.post('http://www.nitrafficindex.com/traffic/getRoadIndex.do',params = queryParams,headers = header,verify = False)
end_time = time.time()
t = end_time - start_time
print(t)
for i in range(len(r.json()['rows'])):
    print(r.json()['rows'][i])


