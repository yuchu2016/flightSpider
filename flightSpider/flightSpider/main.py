from scrapy.cmdline import execute

import sys
import os

# execute(["scrapy", "crawl", "Qingdao"])
flightNo = 'NS3261'
flightDate = "2018-06-11"
execute(["scrapy", "crawl", "FeiChangZhun", '-a', 'flightNo=' + flightNo, '-a', 'flightDate=' + flightDate])
