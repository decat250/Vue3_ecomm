# -*- coding: utf-8 -*-
# https://ithelp.ithome.com.tw/articles/10202886

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

#我把api的處理都放在database/database.py 用來建立連線
from database.database import app as application

#我把api的處理都放在database/api.py裡面
from database.api import login
from database.api import newaccount

#app = Flask(__name__)#database.database裡面有定義app了，再寫會錯誤

#這就是app名稱
app = application
api = Api(app)

#一定要設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_cors import CORS
CORS(app, resources={r'/*': {'origins': '*'}})


#API
@app.route("/api/signin",methods=['POST'])
def signin():
    post_data = request.get_json()
    account = post_data.get('account')
    password = post_data.get('password')
    #account = request.form['account']#取得名為account的傳入值
    #password =  request.form['password']

    if(account != None and password !=None):
        try:
            r = login(account, password)#呼叫自己寫的函數來處理，Class login放在database/api裡面
            
            return r

        except Exception as e:
            return {"Status":"Failed", "Return": str(e)}

@app.route("/api/signup",methods=['POST'])
def signup():
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
        r = newaccount(account,name, password,phone,email)#呼叫自己寫的函數來處理，Class login放在database/api裡面
        
        #r會接到傳回來的東西
        
        return r

    except Exception as e:
        return {"Status":"Failed", "Return": str(e)}

if __name__ == '__main__':
    app.run(debug=True)
    