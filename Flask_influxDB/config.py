#coding:utf-8
from influxdb import InfluxDBClient
import os

basedir = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'E\xda\x80\xe0\x9c\xd8(k\xd2\x05C\x7fN\xf3wa\xe6,mX\xda\xedp\xe7'
DEBUG = False
access_keys = 'TAuQZkNq40TC6S28w8v8DibG96tW4ort0fF6eh49026i310otXeK3JkjnSWzsVsx'

client = InfluxDBClient('127.0.0.1', 8086, 'admin', 'xs9999ad',
                        'XSWebMonitor')  # 初始化
#增加鑫圣投资新接口
clienttz = InfluxDBClient('127.0.0.1', 8086, 'admin', 'xs9999ad', 'XSMCFX')

#鑫圣钜丰：
clientjf = InfluxDBClient('127.0.0.1', 8086, 'admin', 'xs9999ad', 'XSJF24K')

#直播接口:
clientlives = InfluxDBClient('127.0.0.1', 8086, 'admin', 'xs9999ad', 'Lives')
#直播接口花费时间统计：
lives_speedtimes = InfluxDBClient('127.0.0.1', 8086, 'admin', 'xs9999ad',
                                  'LivesSpeedTimes')
