# -*- coding: utf-8 -*-
# https://ithelp.ithome.com.tw/articles/10202886
from flask_cors import CORS
import imp
from multiprocessing.spawn import import_main_path
import os
from werkzeug.utils import secure_filename

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

# 我把api的處理都放在database/database.py 用來建立連線
from database.database import app as application

# 我把api的處理都放在database/api.py裡面
from database.api import login
from database.api import newaccount
from database.api import sendvaildresetpwd
from database.api import pwdreset
from database.api import productgetlist
from database.api import infogetproduct
# app = Flask(__name__)#database.database裡面有定義app了，再寫會錯誤

# 這就是app名稱
app = application
api = Api(app)

# 一定要設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r'/*': {'origins': '*'}})

# API


@app.route("/api/signin", methods=['POST'])
def signin():
    post_data = request.get_json()
    account = post_data.get('account')
    password = post_data.get('password')
    # account = request.form['account']#取得名為account的傳入值
    # password =  request.form['password']

    if(account != None and password != None):
        try:
            # 呼叫自己寫的函數來處理，Class login放在database/api裡面
            r = login(account, password)

            return r

        except Exception as e:
            return {"Status": "Failed", "Return": str(e)}


@app.route("/api/signup", methods=['POST'])
def signup():  # 註冊帳號
    post_data = request.get_json()
    account = post_data.get('account')
    password = post_data.get('password')
    name = post_data.get('name')
    phone = post_data.get('phone')
    email = post_data.get('email')

    '''
    account = request.form['account']
    name =  request.form['name']
    password =  request.form['password']
    phone =  request.form['phone']
    email = request.form['email']
    '''

    try:
        # 呼叫自己寫的函數來處理，Class login放在database/api裡面
        r = newaccount(account, name, password, phone, email)

        # r會接到傳回來的東西

        return r

    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


@app.route("/api/resetpwdsendvaild", methods=['POST'])
def resetpwdsendvaild():  # 註冊帳號

    post_data = request.get_json()

    account = post_data.get('account')
    email = post_data.get('email')
    '''
    account = request.form['account']
    email = request.form['email']
    '''

    try:
        # 呼叫自己寫的函數來處理，Class login放在database/api裡面
        r = sendvaildresetpwd(account, email)

        # r會接到傳回來的東西

        return r

    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


@app.route("/api/resetpwd", methods=['POST'])
def resetpwd():  # 重設密碼

    post_data = request.get_json()

    id = post_data.get('id')
    code = post_data.get('code')
    password = post_data.get('password')
    '''
    id = request.form['id']
    code = request.form['code']
    password=request.form['password']
    '''
    try:
        # 呼叫自己寫的函數來處理，Class login放在database/api裡面
        r = pwdreset(id, code, password)
        return r

    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


@app.route('/api/getproductlist', methods=['GET'])  # 首頁取得商品
def getproductlist():
    try:
        r = productgetlist()
        return r

    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


@app.route('/api/getproductinfo/<id>', methods=['GET'])  # 商品資訊頁取得商品內容
def getproductinfo(id):
    
    try:
        r = infogetproduct(id)
        return r

    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


if __name__ == '__main__':

    app.run(debug=True)
