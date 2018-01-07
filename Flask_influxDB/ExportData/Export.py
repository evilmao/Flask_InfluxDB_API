#coding:utf-8
import json
from ExportData.Dbcol import clienttz, clientjf
import time

def showDatas_xstz():
    ''' '''
    resultcolldata = clienttz.query('select * from UserMobilePhone;')
    colldata = resultcolldata.items()[0][1]
    file = open('dataexport_tz.txt', 'w+')  # 打开文件
    file.truncate()  # 清空文件内容
    coll_redata = [ json.dumps(i["PhoneNumber"]) for i  in colldata ]
    data3 = list(set(coll_redata))
    for s in data3:
        with open("dataexport_tz.txt", 'a+') as f:
            f.write('{}\n'.format(s))


if __name__ == "__main__":
    showDatas_xstz()




