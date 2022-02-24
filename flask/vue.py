# -*- coding: utf-8 -*-
# https://ithelp.ithome.com.tw/articles/10202886
from flask_cors import CORS
from multiprocessing.spawn import import_main_path
import os
import random
from flask import Flask, request, jsonify, redirect, flash, url_for, render_template
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
from database.api import imgbanner
from database.api import productnew
from database.api import newproductimg
# app = Flask(__name__)#database.database裡面有定義app了，再寫會錯誤
import glob
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



@app.route('/api/newproduct', methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':    
        print(request.form)
        
        product_name = request.form['product_name']
        product_count = request.form['product_count']
        product_describe = request.form['product_describe']
        product_price = request.form['product_price']

        r = productnew(product_name,product_count,product_price,product_describe)
        lastid =r["lastid"]
        
        path=app.config['UPLOAD_FOLDER']+"/product/"+str(lastid)
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

        file = request.files.getlist("file[]")
        out=[]
        for files in file:
            print(files.filename)
            filename = (files.filename.split(".")[1])
            #filename = secure_filename(file.filename)
            newfilename = createRandomString(20)
            out.append(newfilename+"."+filename.split(".")[0])
            files.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                    "product/"+str(lastid)+"/"+newfilename+"."+filename.split(".")[0]))

        r = newproductimg(lastid,out)
        return {"Status":"Success","Message":"商品新增成功"}
   


@app.route('/api/bannering', methods=['GET', 'POST']) #banner照片編輯
def bannering():
    if request.method == 'POST':
        file = request.files.getlist("file[]")
        deletefolder = glob.glob(path+"/banner"+"/*")
        for f in deletefolder:
            os.remove(f)
        out=[]
        
        for files in file:
            print(files.filename)
            filename = (files.filename.split(".")[1])
            #filename = secure_filename(file.filename)
            newfilename = createRandomString(20)
            out.append(newfilename+"."+filename.split(".")[0])
            files.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                    "banner/"+newfilename+"."+filename.split(".")[0]))    
        imgbanner(out)
        
        return {"Status":"Success"}
   

def createRandomString(len):
    print('wet'.center(10, '*'))
    raw = ""
    range1 = range(58, 65)  # between 0~9 and A~Z
    range2 = range(91, 97)  # between A~Z and a~z

    i = 0
    while i < len:
        seed = random.randint(48, 122)
        if ((seed in range1) or (seed in range2)):
            continue
        raw += chr(seed)
        i += 1
    # print(raw)
    return raw


if __name__ == '__main__':
    path="/opt/homebrew/var/www/shop/"
    app.config['UPLOAD_FOLDER'] = path
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.run(debug=True)
