# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:29:58 2020

@author: Home
"""

import requests
import time
from bs4 import BeautifulSoup
theDay = input("哪一天要搭高鐵(格式:2020/02/21)?")
timeSelect = input("想搭乘甚麼時間(格式:06:30.24小時制)?")
def searchTHSR(theDay, timeSelect):
    payload = {"startStation": "977abb69-413a-4ccf-a109-0272c24fd490",
               "endStation": "e6e26e66-7dc1-458f-b2f3-71ce65fdc95f",
               "theDay": theDay,
               "timeSelect": timeSelect,
               "waySelect": "DepartureInMandarin"}
    res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResultList",data = payload)
    soup = BeautifulSoup(res.text,"html.parser")
    Finish = False
    for i in range(1,11):
        trainNumber = soup.find_all('div',class_="ui-block-a")[i]
        trainTime = soup.find_all('div',class_="ui-block-b")[i]
        nonReservedNumber = soup.find_all('div',class_="ui-block-c")[i]
        if len(trainTime.text)<5:
            Finish = True
            break
        print("車次:"+trainNumber.text)
        print("出發-抵達(行車時間):"+trainTime.text)
        print("自由座車廂數:"+nonReservedNumber.text)
        print("=====================================================")
    if Finish:
        print("Ok")
    else:
        timeSelect = trainTime.text[0:4]+str(int(trainTime.text[4])+1)
        time.sleep(1)
        return searchTHSR(theDay,timeSelect)
searchTHSR(theDay, timeSelect)