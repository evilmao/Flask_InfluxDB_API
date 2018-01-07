#coding:utf-8
'''
- 认证程序
'''
from functools import wraps
from flask import request, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from flask_httpauth import HTTPBasicAuth


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'apiuser_ad' and password == '6MZ>AZ,p1V0xBp6m'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
                    'Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 
                    401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'}
                    )

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


# 用户列表
auth = HTTPBasicAuth()
users = [
    {'username': 'apiuser_ad', 'password': generate_password_hash('6MZ>AZ,p1V0xBp6m')},
    {'username': 'moshiadmin', 'password': generate_password_hash(':pE$3KY7GY30F78e')}
]


@auth.verify_password
def verify_password(username, password):
    for user in users:
        if user['username'] == username:
            if check_password_hash(user['password'], password):
                return True
    return False


# Token 认证
app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    "secret-token-1": "jcA71L5mYi7XF6Z2",
    "secret-token-2": "3BVfGlA1WW43GqTT"
}


@auth.verify_token
def verify_token(token):
    g.user = None
    if token in tokens:
        g.user = tokens[token]
        return True
    return False
