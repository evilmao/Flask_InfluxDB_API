#coding:utf-8
'''
- token设置
'''
from flask_httpauth import HTTPTokenAuth
from flask import g

auth1 = HTTPTokenAuth(scheme='fCa1eb4cxjBkIuiVvK328qp6LEl79rsG')
tokens = {
            "Access_Key_SecretKey_1": "John-acce_Kye1123123CCaavcxwer",
            "Access_Key_SecretKey_2": "Susan_acce_Kye1123123CCaavcxwer"
         }

@auth1.verify_token
def verify_token(token):
    g.user = None
    if token in tokens:
        g.user = tokens[token]
        return True
    else:
        return False

