#!/usr/bin/env python
#-*-coding:UTF-8-*-
#encoding=utf-8
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import json
import warnings
warnings.filterwarnings("ignore")
import re
import pprint
import os
def main(day):
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer" : "https://train.qunar.com/stationToStation.htm?fromStation=%E5%93%88%E5%B0%94%E6%BB%A8&toStation=%E5%8C%97%E4%BA%AC&date=2018-03-14&drainage=",
        "User - Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML,like Gecko) Version/10.1.2 Safari/603.3.8"
    }
    day_url = "https://train.qunar.com/dict/open/s2s.do?callback=jQuery17207765959610044582_1516718746460&dptStation=%%E5%%8C%%97%%E4%%BA%%AC&arrStation=%%E5%%93%%88%%E5%%B0%%94%%E6%%BB%%A8&date=2018-03-%s&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1516718746689"%(str(day))
    result = requests.get(day_url,headers = headers)
    result_all =  result.content
    #  result_re = re.findall(r"({(.+?)})",result_all)
    #  print result_all
    p = r"{.*}"
    m = re.search(p,result_all)
    result_re =  m.group(0)    
    result_json = json.loads(result_re)
    sta_station = result_json["data"]["dptStation"]
    arr_station = result_json["data"]["arrStation"]
    date = result_json["data"]["dptDate"]
    train_list = result_json["data"]["s2sBeanList"]
    for key in train_list:
        time = key["extraBeanMap"]["interval"]
        for seats in key["seats"]:
            if key["seats"][seats]["count"]>0 :
                print "|",date,"|",key["trainNo"].rjust(6),"|",time.rjust(7),"|",sta_station,"-",arr_station,"|",key["seats"][seats]["count"],"|"
           # count = seats["count"]
        #print sta_station,arr_station,date,time,count

    #
#    train = json.dumps(train_list, ensure_ascii=False)
 #   with open("./train_data", "w") as fp:
  #      fp.write(train.encode("utf-8"))
#

#    for index,NUM in enumerate(trainNo):
 #       print NUM


if __name__ == "__main__":
    print "----------------------------------------------------------"
    print "|", " 出发时间 ", "|", " 车次 ".rjust(6), "|", "  时长    ", "|", "始发 ", "-", " 到达", "|","剩余", "|"
    print "----------------------------------------------------------"
    main(14)
    main(15)
    print "----------------------------------------------------------"



