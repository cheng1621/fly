import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.selector import Selector
import json
from ..items import FlightItem
from scrapy.loader import ItemLoader
import datetime
try:
    null,false,true,display,data
except:
    null = None;false = False;true = True;display = 'display';data = 'data'
class flightSpider(CrawlSpider):
    name = "flight"
    allowed_domains = ["flights.ctrip.com"]
    start_urls = [
        "https://flights.ctrip.com/itinerary/api/12808/products"
    ]
    def start_requests(self):
        with open('loc.txt','r') as f:
            while True:
                now = datetime.date(2019, 4, 8)
                delta = datetime.timedelta(days=1)
                end = datetime.date(2019, 4,9)
                x = f.readline().strip()
                if not x:
                    break
                cityInfo = eval(x)
                while now < end:
                    data = {"flightWay":"Oneway","classType":"ALL","hasChild":'false',"hasBaby":'false',"searchIndex":'1',
                    "airportParams":[{"dcity":"BJS","acity":"%s"%cityInfo[2],"dcityname":u"北京","acityname":u"%s"%cityInfo[0],
                                      "date":"%s"%str(now),"dcityid": 1, "acityid": cityInfo[1]}]}
                    data = json.dumps(data)
                    now = now + delta
                    yield scrapy.Request(self.start_urls[0],method='POST',body = data,callback=self.parse_1,meta={'acity':'%s'%cityInfo[2]},
                                         dont_filter=True)
        f.close()
    def parse_1(self, response):
        try:
            RouteList = eval(response.text)['data']['routeList']
        except:
            pass
        else:
            a = response.meta['acity']
            if RouteList != None:
                for i in range(len(RouteList)):
                    x = eval(response.text)['data']['routeList'][i]['legs'][0]
                    y = eval(response.text)['data']['routeList'][i]
                    if y['routeType'] == 'Flight':
                        item = []
                        FlightInfo = ItemLoader(item=FlightItem(), response=response)
                        FlightInfo.add_value('ID', x['flightId'])
                        FlightInfo.add_value('FlightId',x['flight']['flightNumber'])
                        FlightInfo.add_value('FDid',x['flight']['flightNumber']+ '-' + x['flight']['departureDate'])
                        FlightInfo.add_value('StartCity',x['flight']['departureAirportInfo']['cityName'])
                        FlightInfo.add_value('ArriveCity',x['flight']['arrivalAirportInfo']['cityName'])
                        FlightInfo.add_value('StartAirport', x['flight']['departureAirportInfo']['airportName'])
                        FlightInfo.add_value('ArriveAirport', x['flight']['arrivalAirportInfo']['airportName'])
                        FlightInfo.add_value('type', x['flight']['craftTypeKindDisplayName'])
                        FlightInfo.add_value('AirType', x['flight']['craftTypeName'])
                        FlightInfo.add_value('food', x['flight']['mealType'])
                        j = x['cabins'][0]['price']['price']
                        for k in range(1,len(x['cabins'])):
                            j = min(j,x['cabins'][k]['price']['price'])
                        FlightInfo.add_value('price',j)
                        FlightInfo.add_value('discount', x['cabins'][0]['price']['discount'])
                        FlightInfo.add_value('time', datetime.datetime.now().strftime('%y%m%d'))
                        data = json.dumps({"dcity":"BJS","acity":"%s"%a,"startDate":"%s"%x['flight']['departureDate'],
                                           "flightNos":["%s"%x['flight']['flightNumber']]})
                        item.append(FlightInfo.load_item())
                        yield scrapy.Request('https://flights.ctrip.com/itinerary/api/12808/flightComfortableInfo',body = data,
                                             meta = {'info':item},method='POST',callback = self.parse_2)
    def parse_2(self,response):   # 获取航班延误率
        item = response.meta['info']
        try:
            x = eval(response.text)['data'][0]
        except:
            yield item[0]
        else:
            FlightInfo = ItemLoader(item=FlightItem(), response=response)
            FlightInfo.add_value('PunctStratRate', x['historyPunctuality'])
            FlightInfo.add_value('PunctArriveRate', x['historyPunctualityArr'])
            item[0].update(FlightInfo.load_item())
            data = json.dumps({'flightNo': '%s' % x['flightNo']})
            yield scrapy.Request('https://flights.ctrip.com/itinerary/api/12808/historyPunctuality', body=data,
                                 meta={'info': item}, method='POST', callback=self.parse_3)

    def parse_3(self,response):   # 获取平均延误时间
        item = response.meta['info']
        FlightInfo = ItemLoader(item=FlightItem(), response=response)
        x = eval(response.text)['data']
        dep = 0;arr = 0
        for i in range(len(x)):
            if x[i]['depDelay'] != None:
                dep = dep + x[i]['depDelay']
            if x[i]['arrDelay'] != None:
                arr = arr + x[i]['arrDelay']
        FlightInfo.add_value('LateStratTime', round(dep/len(x)))
        FlightInfo.add_value('LateArriveTime', round(arr/len(x)))
        item[0].update(FlightInfo.load_item())
        return item