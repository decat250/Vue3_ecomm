# -*- coding: utf-8 -*-
# https://ithelp.ithome.com.tw/articles/10202886
from datetime import datetime
import imp
from flask_cors import CORS
from multiprocessing.spawn import import_main_path
import os
import random
import shutil
import requests
import pprint
import datetime
from flask import Flask, request, jsonify, redirect, flash, url_for, render_template
from flask_restful import Api, Resource, reqparse, abort
import importlib.util

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
from database.api import listproductadmget
from database.api import productdel
from database.api import productedit
from database.api import editproductimg
from database.api import cartaddto
from database.api import shopcartget
from database.api import cartdel
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
    googlelogin = post_data.get("googlelogin")
    account = post_data.get('account')
    password = post_data.get('password')
    # account = request.form['account']#取得名為account的傳入值
    # password =  request.form['password']

    if(account != None and password != None):
        try:

            # 呼叫自己寫的函數來處理，Class login放在database/api裡面
            r = login(account, password, googlelogin)

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
        opt = request.form["opt"].split(",")
        product_name = request.form['product_name']
        product_count = request.form['product_count']
        product_describe = request.form['product_describe']
        product_price = request.form['product_price']

        r = productnew(product_name, product_count,
                       product_price, product_describe, opt)
        lastid = r["lastid"]

        path = app.config['UPLOAD_FOLDER']+"/product/"+str(lastid)
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

        file = request.files.getlist("file[]")
        out = []
        for files in file:
            print(files.filename)
            filename = (files.filename.split(".")[1])
            # filename = secure_filename(file.filename)
            newfilename = createRandomString(20)
            out.append(newfilename+"."+filename.split(".")[0])
            files.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                    "product/"+str(lastid)+"/"+newfilename+"."+filename.split(".")[0]))

        r = newproductimg(lastid, out)
        return {"Status": "Success", "Message": "商品新增成功"}


@app.route('/api/bannering', methods=['GET', 'POST'])  # banner照片編輯
def bannering():
    if request.method == 'POST':
        file = request.files.getlist("file[]")
        deletefolder = glob.glob(path+"/banner"+"/*")
        for f in deletefolder:
            os.remove(f)
        out = []

        for files in file:
            print(files.filename)
            filename = (files.filename.split(".")[1])
            # filename = secure_filename(file.filename)
            newfilename = createRandomString(20)
            out.append(newfilename+"."+filename.split(".")[0])
            files.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                    "banner/"+newfilename+"."+filename.split(".")[0]))
        imgbanner(out)

        return {"Status": "Success"}


@app.route('/api/productadmgetlist', methods=['GET', 'POST'])  # banner照片編輯
def productadmgetlist():
    try:
        r = listproductadmget()
        return r
    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


@app.route('/api/delproduct', methods=['GET', 'POST'])  # banner照片編輯
def delproduct():
    try:
        id = request.form['deleteid']
        r = productdel(id)

        if (r['Status'] == "Success"):
            shutil.rmtree(app.config['UPLOAD_FOLDER'] +
                          "product/"+str(id), ignore_errors=True)

        return {"Status": "Success", "Message": "商品刪除成功"}
    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


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


@app.route('/api/editproduct', methods=['GET', 'POST'])  # 編輯商品
def editproduct():
    if request.method == 'POST':
        opt = request.form["opt"].split(",")
        product_name = request.form['product_name']
        product_count = request.form['product_count']
        product_describe = request.form['product_describe']
        product_price = request.form['product_price']
        id = request.form['id']

        r = productedit(id, product_name, product_count,
                        product_price, product_describe, opt)
        lastid = id

        deletefolder = glob.glob(path+"/product/"+str(lastid)+"/*")
        for f in deletefolder:
            os.remove(f)

        file = request.files.getlist("file[]")
        out = []
        for files in file:
            filename = (files.filename.split(".")[1])
            newfilename = createRandomString(20)
            out.append(newfilename+"."+filename.split(".")[0])
            files.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                    "product/"+str(lastid)+"/"+newfilename+"."+filename.split(".")[0]))
        print(out)
        r = editproductimg(lastid, out)
        return {"Status": "Success", "Message": "商品修改成功"}


@app.route('/api/addtocart', methods=['GET', 'POST'])  # 編輯商品
def addtocart():
    if request.method == 'POST':

        userid = request.form['userid']
        opt = request.form['selopt']
        product_id = request.form['product_id']
        product_count = request.form['product_count']

        r = cartaddto(userid, product_id, product_count, opt)
        return {"Status": "Success", "Message": "商品已成功加入購物車"}


@app.route('/api/getshopcart/<userid>', methods=['GET', 'POST'])  # 取得購物車內容
def getshopcart(userid):
    if request.method == 'GET':
        r = shopcartget(userid)
        return r


@app.route('/api/delcart', methods=['GET', 'POST'])  # banner照片編輯
def delcart():
    try:
        id = request.form['deleteid']
        r = cartdel(id)
        return {"Status": "Success", "Message": "商品刪除成功"}
    except Exception as e:
        return {"Status": "Failed", "Return": str(e)}


@app.route('/api/pay', methods=['GET', 'POST'])
def pay():
    userid = request.form['userid']
    print(userid)
    import time
    date = time.time()
    tid = str(date) + 'Uid' + str(userid)
    print(tid)
    print(request.form['name'])
    print(request.form['phone'])
    print(request.form['address'])
    print(request.form['ordermark'])

    
    TotalAmount = request.form['TotalAmount']
    ItemName = request.form['ItemName']
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "ecpay_payment_sdk",
        "/Users/decat/Vue3_ecomm/flask/ecpay_payment_sdk.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    order_params = {
        'MerchantTradeNo': datetime.datetime.now().strftime("NO%Y%m%d%H%M%S"),
        'StoreID': '',
        'MerchantTradeDate': datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'PaymentType': 'aio',
        'TotalAmount': TotalAmount,
        'TradeDesc': '訂單測試',
        'ItemName': ItemName,
        'ReturnURL': 'http://127.0.0.1/test',
        'ChoosePayment': 'ALL',
        'ClientBackURL': 'http://localhost:8080/#/',
        'ItemURL': 'https://www.ecpay.com.tw/item_url.php',
        'Remark': '交易備註',
        'ChooseSubPayment': '',
        'OrderResultURL': 'http://127.0.0.1/test',
        'NeedExtraPaidInfo': 'Y',
        'DeviceSource': '',
        'IgnorePayment': '',
        'PlatformID': '',
        'InvoiceMark': 'N',
        'CustomField1': '',
        'CustomField2': '',
        'CustomField3': '',
        'CustomField4': '',
        'EncryptType': 1,
    }

    extend_params_1 = {
        'ExpireDate': 7,
        'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
        'ClientRedirectURL': '',
    }

    extend_params_2 = {
        'StoreExpireDate': 15,
        'Desc_1': '',
        'Desc_2': '',
        'Desc_3': '',
        'Desc_4': '',
        'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
        'ClientRedirectURL': '',
    }

    extend_params_3 = {
        'BindingCard': 0,
        'MerchantMemberID': '',
    }

    extend_params_4 = {
        'Redeem': 'N',
        'UnionPay': 0,
    }

    inv_params = {
        # 'RelateNumber': 'Tea0001', # 特店自訂編號
        # 'CustomerID': 'TEA_0000001', # 客戶編號
        # 'CustomerIdentifier': '53348111', # 統一編號
        # 'CustomerName': '客戶名稱',
        # 'CustomerAddr': '客戶地址',
        # 'CustomerPhone': '0912345678', # 客戶手機號碼
        # 'CustomerEmail': 'abc@ecpay.com.tw',
        # 'ClearanceMark': '2', # 通關方式
        # 'TaxType': '1', # 課稅類別
        # 'CarruerType': '', # 載具類別
        # 'CarruerNum': '', # 載具編號
        # 'Donation': '1', # 捐贈註記
        # 'LoveCode': '168001', # 捐贈碼
        # 'Print': '1',
        # 'InvoiceItemName': '測試商品1|測試商品2',
        # 'InvoiceItemCount': '2|3',
        # 'InvoiceItemWord': '個|包',
        # 'InvoiceItemPrice': '35|10',
        # 'InvoiceItemTaxType': '1|1',
        # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
        # 'DelayDay': '0', # 延遲天數
        # 'InvType': '07', # 字軌類別
    }

    # 建立實體
    ecpay_payment_sdk = module.ECPayPaymentSdk(
        MerchantID='2000132',
        HashKey='5294y06JbISpM5x9',
        HashIV='v77hoKGq4kWxNNIS'
    )

    # 合併延伸參數
    order_params.update(extend_params_1)
    order_params.update(extend_params_2)
    order_params.update(extend_params_3)
    order_params.update(extend_params_4)

    # 合併發票參數
    order_params.update(inv_params)

    try:
        # 產生綠界訂單所需參數
        final_order_params = ecpay_payment_sdk.create_order(order_params)

        # 產生 html 的 form 格式
        action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'  # 測試環境
        html = ecpay_payment_sdk.gen_html_post_form(
            action_url, final_order_params)
        return (html)
    except Exception as error:
        print('An exception happened: ' + str(error))


@app.route('/api/cvs/<LogisticsSubType>', methods=['GET', 'POST'])
def cvs(LogisticsSubType):

    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "ecpay_logistic_sdk",
        "/Users/decat/Vue3_ecomm/flask/ecpay_logistic_sdk.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    cvs_map_params = {
        "MerchantID": "2000132",
        "MerchantTradeNo": "anyno",
        "LogisticsType": "CVS",
        # 若申請類型為 B2C，只能串參數為 FAMI、UNIMART、HILIFE
        # 若申請類型為 C2C，只能串參數為 FAMIC2C、UNIMARTC2C、HILIFEC2C
        "LogisticsSubType": LogisticsSubType,
        "IsCollection": "N",
        "ServerReplyURL": "http://localhost/api/cvs_get",
        "ExtraData": "額外資訊",
        "Device": module.Device['PC'],
    }

    # 建立實體
    ecpay_logistic_sdk = module.ECPayLogisticSdk(
        MerchantID='2000933',
        HashKey='XBERn1YOvpM9nfZc',
        HashIV='h1ONHk4P4yqbl5LK'
    )

    try:
        # 產生綠界物流訂單所需參數
        final_params = ecpay_logistic_sdk.cvs_map(cvs_map_params)

        # 產生 html 的 form 格式
        action_url = 'https://logistics-stage.ecpay.com.tw/Express/map'  # 測試環境
        # action_url = 'https://logistics.ecpay.com.tw/Express/map' # 正式環境
        html = ecpay_logistic_sdk.gen_html_post_form(action_url, final_params)
        return (html)
    except Exception as error:
        print('An exception happened: ' + str(error))


@app.route('/api/cvs_get', methods=['GET', 'POST'])
def cvs_get():
    return redirect("http://localhost:8080/#/cvs_get/"+request.form['CVSStoreID']+"/"+request.form['CVSStoreName']+"/"+request.form['CVSAddress'], code=302)


@app.route('/api/cvs_home', methods=['GET', 'POST'])
def csv_home():
    spec = importlib.util.spec_from_file_location(
        "ecpay_logistic_sdk",
        "/Users/decat/Vue3_ecomm/flask/ecpay_logistic_sdk.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    create_shipping_order_params = {
        'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
        'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'LogisticsType': module.LogisticsType['HOME'],
        'LogisticsSubType': module.LogisticsSubType['TCAT'],
        'GoodsAmount': 1500,
        'CollectionAmount': 1500,
        'IsCollection': module.IsCollection['NO'],
        'GoodsName': '測試商品',
        'SenderName': '測試寄件者',
        'SenderPhone': '0226550115',
        'SenderCellPhone': '0911222333',
        'ReceiverName': '測試收件者',
        'ReceiverPhone': '0226550115',
        'ReceiverCellPhone': '0933222111',
        'ReceiverEmail': 'test@gmail.com',
        'TradeDesc': '測試交易敘述',
        'ServerReplyURL': 'https://www.ecpay.com.tw/server_reply_url',
        'ClientReplyURL': '',
        'Remark': '測試備註',
        'PlatformID': '',
        'LogisticsC2CReplyURL': 'https://www.ecpay.com.tw/logistics_c2c_reply',
    }

    shipping_home_params = {
        'SenderZipCode': '11560',
        'SenderAddress': '台北市南港區三重路19-2號10樓D棟',
        'ReceiverZipCode': '11560',
        'ReceiverAddress': '台北市南港區三重路19-2號5樓D棟',
        'Temperature': module.Temperature['FREEZE'],
        'Distance': module.Distance['SAME'],
        'Specification': module.Specification['CM_120'],
        'ScheduledPickupTime': module.ScheduledPickupTime['TIME_17_20'],
        'ScheduledDeliveryTime': module.ScheduledDeliveryTime['TIME_17_20'],
        'ScheduledDeliveryDate': '',
        'PackageCount': '',
    }

    # 更新及合併參數
    create_shipping_order_params.update(shipping_home_params)

    # 建立實體
    ecpay_logistic_sdk = module.ECPayLogisticSdk(
        MerchantID='2000933',
        HashKey='XBERn1YOvpM9nfZc',
        HashIV='h1ONHk4P4yqbl5LK'
    )

    try:
        # 介接路徑
        action_url = 'https://logistics-stage.ecpay.com.tw/Express/Create'  # 測試環境
        # action_url = 'https://logistics.ecpay.com.tw/Express/Create' # 正式環境

        # 建立物流訂單並接收回應訊息
        reply_result = ecpay_logistic_sdk.create_shipping_order(
            action_url=action_url,
            client_parameters=create_shipping_order_params)
        return (reply_result)

    except Exception as error:
        print('An exception happened: ' + str(error))


if __name__ == '__main__':

    path = "/opt/homebrew/var/www/shop/"
    app.config['UPLOAD_FOLDER'] = path
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.run(debug=True)
