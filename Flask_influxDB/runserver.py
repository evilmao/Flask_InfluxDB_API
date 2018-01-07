#coding:utf-8
'''
- 服务器端运行程序
'''
from DD_Robot_Monitor import app

app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)  #多线程开启
