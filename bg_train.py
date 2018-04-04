#!/usr/bin/env python
#-*-coding:UTF-8-*-
#encoding=utf-8
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import json
import warnings
import re
import pprint
import os
import time
warnings.filterwarnings("ignore")
global have
global train_num
global count
global day_url
have = 0
def main(day):
    global have
    global train_num
    global count
    global day_url
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer" : "https://train.qunar.com/stationToStation.htm?fromStation=%E5%93%88%E5%B0%94%E6%BB%A8&toStation=%E5%8C%97%E4%BA%AC&date=2018-02-12&drainage=",
        "User - Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML,like Gecko) Version/10.1.2 Safari/603.3.8"
    }
    day_url = "https://train.qunar.com/dict/open/s2s.do?callback=jQuery17207765959610044582_1516718746460&dptStation=%%E5%%8C%%97%%E4%%BA%%AC&arrStation=%%E5%%93%%88%%E5%%B0%%94%%E6%%BB%%A8&date=2018-02-%s&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1516718746689"%(str(day))
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
        time = time.encode("utf-8")
        time_long = time.split("小时")
        times = time_long[0]
        for seats in key["seats"]:
            if key["seats"][seats]["count"]>0 and int(times) < 12:
                 #print times,"+++++++",key["seats"][seats]["count"]
                 have = 1
                 train_num = key["trainNo"].encode("utf-8")
                 count = str(key["seats"][seats]["count"])

                #return have = 1,
           # count = seats["count"]
        #print sta_station,arr_station,date,time,count

    #
#    train = json.dumps(train_list, ensure_ascii=False)
 #   with open("./train_data", "w") as fp:
  #      fp.write(train.encode("utf-8"))
#

#    for index,NUM in enumerate(trainNo):
 #       print NUM

if "__main__" == __name__:
    while True:
        have = 0
        main(12)
        #if have == 1 :
            #print train_num,count
         #   os.system("echo 'have a train \n 车次:%s    余票:%s'  \n URL: %s | mail -s '火车票信息'  chen_yueyang@outlook.com,17801085150@163.com,1769239390@qq.com"%(train_num,count,day_url))
            #os.system("echo 'have a train \n 车次:%s    余票:%s'  \n 链接: %s | mail -s '火车票信息'  chen_yueyang@outlook.com"%(train_num,count,day_url))

        time.sleep(10)
        main(13)
        if have == 1:
            #have =1
            #print train_num,count
            os.system("echo 'have a train \n 车次:%s    余票:%s'  \n 链接: %s | mail -s '火车票信息'  chen_yueyang@outlook.com,17801085150@163.com,1769239390@qq.com"%(train_num,count,day_url))
            #print "www"
        time.sleep(120)
