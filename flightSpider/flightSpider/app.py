import logging
import os

from flask import Flask, jsonify, abort, signals

from flightSpider.flightSpider.dao.FlightDao import FlightDao

app = Flask(__name__)

spiders = {
    "CA": "GuoHang",
    "GY": "GuiZhou",
    "SC": "ShanDong",
    "BK": "AoKai",
    "HU": "HaiNan",
    # "JD": "JinLu",
    "GS": "HaiNan",
    "CN": "HaiNan",
    # "PN": "HaiNan",
    # "8L": "HaiNan",
    "JD": "HaiNan",
    "UO": "HaiNan",
    "HX": "HaiNan",
    "MF": "XiaMen",
    "MU": "DongFang",
    "CZ": "NanFang",
    "3U": "SiChuan",
    "EU": "ChengDu",
    "HO": "JiXiang",
    "NS": "HeBei",
    "KN": "LianHe",
    "TV": "XiZang",
    "KY": "KunMing",
    "PN": "XiBu",
    "DZ": "DongHai",
    "QW": "QingDao",
    "RY": "JiangXi",
}


@app.route('/flight/<string:flightDate>/<string:flightNo>', methods=['GET'])
def getFlightInfo(flightNo, flightDate):
    try:
        if flightNo[0:2] not in spiders:
            spider = "FeiChangZhun"
        else:
            spider = spiders[flightNo[0:2]]
        print('scrapy crawl ' + spider + ' -a flightNo=' + flightNo + ' -a flightDate=' + flightDate)
        dao = FlightDao()
        dao.clearFlight(flightNo)
        os.system('scrapy crawl ' + spider + ' -a flightNo=' + flightNo + ' -a flightDate=' + flightDate)
        result = dao.searchFlight(flightNo)
        return jsonify({'flight': result})
    except Exception as error:
        # 出现错误时打印错误日志
        logging.error(error)
        result = error
        return jsonify({'error': '未知错误'})
    # if len(result) == 0:
    #     abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
