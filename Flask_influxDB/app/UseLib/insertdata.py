#coding:utf-8
'''
- 数据库操作
- 连接influxBD数据库,将接收到服务器信息插入数据库
'''
from config import client, clienttz, clientjf, clientlives
from datetime import *

class insertdata_influx:
    
    def __init__(self,conn):
        self.c = conn

    def InsertDatas_AS(self,a):
        '''对应'''
        try:
            self.c.write_points(a)
            with open("/API/Logs/insert.log",'a+') as f:
                f.write("xswebapi-data insert success! {}\n".format(datetime.now()))
        except Exception as f:
            pass
