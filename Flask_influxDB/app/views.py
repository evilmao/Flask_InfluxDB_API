#coding:utf-8

'''
- 用于API接口传输数据到Influxdb
'''
from app import app
from flask import request, abort, jsonify, make_response,render_template
from app.UseLib import TokenAccess
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from werkzeug.security import generate_password_hash, check_password_hash
from config import client
from Log import * #日志


#认证开始
from app.UseLib.insertdata import insertdata_influx

auth = HTTPBasicAuth()
users = [
            {'username': 'apiuser_ad', 'password': generate_password_hash('6MZkakap1V0xBS6m')},
            {'username': 'moshiadmin', 'password': generate_password_hash('1pEC3KY7GY30F7Se')}
        ]
dataws = insertdata_influx(client)


@auth.verify_password
def verify_password(username, password):
    '''authenticate'''
    for user in users:
        if user['username'] == username:
            if check_password_hash(user['password'], password):
                return True
    return False

#authenticate error
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/xsmcfx/1' , methods=['POST'])
@auth.login_required
def create_xsmcfx_1():
        if not request.json or not 'Payment' in request.json:
            abort(400)
        xsmcfx1 = {
                'measurement': 'Deposit_Injection_Amount',
                'tags':{
                'Account': request.json.get('Account'),
                'Money':request.json.get('Money'),
                'Payment':request.json.get('Payment'),
                'Bank':request.json.get('Bank'),
                'Source':request.json.get('Source'),
                'ErrorLog':request.json.get('ErrorLog'),
                'IPAddress': request.json.get('IPAddress'),
                },
                'fields':{
                'ReturnCode':request.json.get('ReturnCode')
                }
        }
        datatz.InsertDatas_xsmcfx([xsmcfx1])
        return "0"

@app.route('/api/xsmcfx/2', methods=['POST'])
@auth.login_required
def create_xsmcfx_2():
    pass


