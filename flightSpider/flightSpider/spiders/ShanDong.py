import scrapy

from ..Item.ShanDongItems import ShanDongItems


class ShangDongSpider(scrapy.Spider):
    name = "ShanDong"

    def __init__(self, flightNo=None, flightDate=None, *args, **kwargs):
        super(ShangDongSpider, self).__init__(*args, **kwargs)
        self.flightNo = flightNo
        self.flightDate = flightDate

    def start_requests(self):
        url = 'http://www.sda.cn/ajaxGetByFlightNo.shtml'
        yield scrapy.FormRequest(
            url=url,
            formdata={"vNum": self.flightNo},
            callback=self.parse
        )

    def parse(self, response):
        selector = scrapy.Selector(response)
        flights = selector.xpath('//table/tbody/tr')
        for i, flight in enumerate(flights):
            # flightInfo = flight.extract()
            # print(flightInfo)
            item = ShanDongItems()
            i += 1
            item['airlineCorp'] = '山东航空'
            flightNo = flight.xpath('//tr[' + str(i) + ']/td[1]/text()').extract_first(default='')
            item['airline'] = flightNo
            expDeptTime = flight.xpath('//tr[' + str(i) + ']/td[5]/text()').extract_first(default='')
            item['expDeptTime'] = expDeptTime
            expArrTime = flight.xpath('//tr[' + str(i) + ']/td[9]/text()').extract_first(default='')
            item['expArrTime'] = expArrTime
            actDeptTime = flight.xpath('//tr[' + str(i) + ']/td[6]/text()').extract_first(default='')
            item['actDeptTime'] = actDeptTime
            actArrTime = flight.xpath('//tr[' + str(i) + ']/td[10]/text()').extract_first(default='')
            item['actArrTime'] = actArrTime
            item['status'] = flight.xpath('//tr[' + str(i) + ']/td[11]/text()').extract_first(default='')
            # print(flightNo + expDeptTime + expArrTime + actDeptTime + actArrTime)
            yield item

    pass
