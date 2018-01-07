#coding:utf-8
'''
-启用日志功能
'''
import logging

logging.basicConfig(
                    level = logging.DEBUG,
                    format = '%(asctime)s %(levelname)s %(message)s',
                    datefmt = '%a, %d %b %Y %H:%M:%S',
                    filename = 'Logs/api-server.log',
                    filemode = 'w'
                    )

logging.debug('app')
