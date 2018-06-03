# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:50:01 2018

@author: Administrator
"""
import urllib.request as r
print('欢迎使用全球天气APP')
print('1.查看当前城市天气，2.查看其他城市天气，3.保存当前城市天气')
menno=input('请输入菜单：')
if menno=='1':
    print('1.查看当前城市天气')
if menno=='2':
    print('2.查看其他城市天气')
if menno=='3':
    print('3.保存当前城市天气')
city_pinyin=input('请输入城市(拼音)：')
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
#json(dict)格式工具包
import json
data=json.loads(info)
weather={'最高温度':data['main']['temp'],
         '天气情况':data['weather'][0]['description'],
         '气压':data['main']['pressure']}
print('{}的最高温度为:{},天气情况为:{},气压为:{}'.format(city_pinyin,weather['最高温度'],
      weather['天气情况'],
      weather['气压']))


