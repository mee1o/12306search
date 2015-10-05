# -*- coding: utf-8 -*-
import requests
import re
import json

SEARCH_TICKET_URL="https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s"

def getStationName(chinese):
    stationTable = open("station_name.js").read()
    pattern = re.compile('\|'+chinese+'\|([A-Z]{3})');
    stationCode = pattern.search(stationTable)
    return stationCode.group(1)
    

def getInfoByUrl(queryDate, fromStation, toStation):
    fromStation = getStationName(fromStation)
    toStation = getStationName(toStation)
	# https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2015-10-23&from_station=NCG&to_station=CZQ
    url = SEARCH_TICKET_URL % (queryDate, fromStation, toStation)
    print url
    rawJson = requests.get(url, verify=False).text
    data = json.loads(rawJson)
    return data["data"]["datas"]

if __name__=="__main__":
    queryDate = '2015-01-27'
    fromStation = '成都'
    toStation = '拉萨'
    print getInfoByUrl(queryDate,fromStation,toStation)