# -*- coding: utf-8 -*-
# https://myapollo.com.tw/2016/09/28/python-sqlalchemy-orm-1/

from operator import le
import re
from this import d
from typing_extensions import runtime
from unicodedata import name
from unittest import result
from sqlalchemy import create_engine, and_, exc, Integer, ForeignKey, String, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import case
import json
# 從database/model引入所有class，包含與DB的映對(Mapping)關係
from database.model import *

# 從database/database把db傳過來
from database.database import db
from sqlalchemy import text

import random
from email.mime.text import MIMEText
import smtplib
from email.header import Header


db.create_all()  # db建立連線

# 用來登入的API的處理(一個Class)，這邊login會傳入兩個變數(帳號，密碼)


def login(ac, pw, googlelogin):  # 登入
    try:
        print(googlelogin)
        print(ac)
        print(pw)
        sql = text('select * from tb_user where User_account="' +
                   str(ac)+'" and user_password="'+str(pw)+'"')
        result = db.engine.execute(sql)
        data = []
        for row in result:
            data = [row[1], row[2], row[3], row[4], row[5], row[0]]
        if (len(data) == 0):
            if googlelogin == 0:
                return {"Status": "Failed", "Message": "帳號密碼錯誤"}
            else:
                return {"Status": "GN", "Message": "您是第一次使用Google帳號，請先建立帳號"}
        else:
            return {"Status": "Success", "Message": str(data[1])+"您好", "data": data}
    except Exception as e:
        print("error occur: %s" % (e))


def newaccount(account, name, password, phone, email):  # 註冊
    try:
        # 查詢帳號是否存在
        sql = text('select * from tb_user where User_account="' +
                   str(account)+'"')
        result = db.engine.execute(sql)
        data = []
        for row in result:
            data = [row[1]]
        if len(data) == 1:
            return {"Status": "Failed", "Message": "帳號已存在"}

        # 建立新帳號
        sql = text("insert into tb_user (User_account,User_name,User_password,User_phone,User_email) VALUES ('" +
                   account+"','"+name+"','"+password+"','"+phone+"','"+email+"')")
        result = db.engine.execute(sql)
        print(result)
        return {"Status": "Success", "Message": "帳號建立成功"}
    except Exception as e:
        print("error occur: %s" % (e))


def sendvaildresetpwd(account, email):  # 重設密碼接收驗證碼
    try:
        # 查詢帳號是否存在
        sql = text('select * from tb_user where User_account="' +
                   str(account)+'" and User_email="'+str(email)+'"')
        result = db.engine.execute(sql)
        data = []
        for row in result:
            data = [row[0], row[5]]
        if len(data) == 0:
            return {"Status": "Failed", "Message": "帳號或信箱錯誤"}

        # 產生驗證碼
        code = ''
        for i in range(5):
            num = str(random.randrange(10))     # 得到隨機數字並轉化成字元
            zm = chr(random.randrange(97, 123))     # 得到小寫字母的ascii碼值用chr轉換成字母
            zm_d = chr(random.randrange(65, 91))    # 得到大寫字母的ascii碼值用chr轉換成字母
            single = random.choice([num, zm, zm_d])  # 得到隨機的一個字元
            code += single                          # 字串拼接

        # 先刪除，後新增
        sq = "delete from tb_vaildcode where User_id = "+str(data[0])
        sql = text(sq)
        result = db.engine.execute(sql)

        sq = "insert into tb_vaildcode (User_id,Vaildcode_code) VALUES (" + \
            str(data[0])+","+"'"+str(code)+"')"
        sql = text(sq)
        result = db.engine.execute(sql)

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('asdfg199715@gmail.com', 'jsvquecuzexlumxj')
        message = MIMEText('您的重設驗證碼：'+str(code), 'plain', 'utf-8')
        message['From'] = Header("easy shop購物網站", 'utf-8')   # 发送者
        message['To'] = Header("easy shop@gmail.com", 'utf-8')        # 接收者

        subject = '密碼重設信件'
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj.sendmail("asdfg199715@gmail.com",
                         [str(data[1])], message.as_string())
        smtpObj.quit()  # 關閉本地端對遠端郵件伺服器的連線

        return {"Status": "Success", "Message": "驗證碼已寄到您的信箱", "id": data[0]}

    except Exception as e:
        print("error occur: %s" % (e))

# 重設密碼


def pwdreset(id, code, password):
    sql = text('select * from tb_vaildcode where User_id="' +
               str(id)+'" and Vaildcode_code="'+str(code)+'"')
    result = db.engine.execute(sql)
    data = []
    print(id)
    print(code)
    for row in result:
        data = [row[1], row[0]]
    if len(data) == 0:
        return {"Status": "Failed", "Message": "驗證碼錯誤"}
    else:
        sql = "update tb_user set User_password = '" + \
            str(password)+"' where User_id='"+str(data[0])+"'"
        result = db.engine.execute(sql)

        sql = "delete from tb_vaildcode where Vaildcode_id = '" + \
            str(data[1])+"'"
        result = db.engine.execute(sql)

        return {"Status": "Success", "Message": "密碼已修改"}


def productgetlist(typeid):  # 首頁取得商品
    print(typeid)
    sql = text('select * from tb_banner')
    result = db.engine.execute(sql)
    banner = []
    for row in result:
        banner.append(
            {"banner_id": str(row[0]), "item": "http://localhost/shop/banner/"+str(row[1])})

    #sql = text('select * from tb_product')
    if typeid == "null":
        sql = text("select * from tb_product")
    else:
        sql = text("select tb_product.product_id,tb_product.product_name FROM `tb_typecont` inner JOIN `tb_product` on tb_typecont.product_id = tb_product.product_id where tb_typecont.type_id = '"+str(typeid)+"'")
    result = db.engine.execute(sql)
    data = []
    for row in result:
        sql = text('select * from `tb_product_img` where `product_id` = "' +
                   str(row[0])+'" order by product_id')
        img = db.engine.execute(sql)
        imgsrc = ""
        for imgrow in img:
            imgsrc = imgrow[2]
        price = ""
        min = db.engine.execute(text(
            'select min(`product_opt_price`) from `tb_product_opt` where `product_id` = "' + str(row[0])+'"'))
        for r in min:
            price += str(r[0])+"~"
        max = db.engine.execute(text(
            'select max(`product_opt_price`) from `tb_product_opt` where `product_id` = "' + str(row[0])+'"'))
        for r in max:
            price += str(r[0])
        data.append({"product_id": str(row[0]), "product_name": str(row[1]), "product_price": str(
            price), "product_img": str(imgsrc)})

    producttype = db.engine.execute("SELECT * FROM `tb_producttype`")
    type = []

    type.append({"label": "全部商品", "key": "null"})
    for row in producttype:
        type.append({"label": str(row[1]), "key": str(row[0])})
    return {"Status": "Success", "productlist": data, "bannerimg": banner, "page": int(len(data)/10)+1, "type": type}


def infogetproduct(id):  # 商品頁取得內容

    sql = text('select * from tb_product where product_id="'+str(id)+'"')
    result = db.engine.execute(sql)
    data = {}
    opt = []
    for row in result:
        data["product_id"] = str(row[0])
        data['product_name'] = str(row[1])
        data['product_describe'] = str(row[3])
    price = ""
    min = db.engine.execute(text(
        'select min(`product_opt_price`) from `tb_product_opt` where `product_id` = "' + str(row[0])+'"'))
    for r in min:
        price += str(r[0])+"~"
    max = db.engine.execute(text(
        'select max(`product_opt_price`) from `tb_product_opt` where `product_id` = "' + str(row[0])+'"'))
    for r in max:
        price += str(r[0])
    data["product_price"] = price
    sql = text('select * from tb_product_img where product_id="'+str(id)+'"')
    result = db.engine.execute(sql)
    img = []
    for row in result:
        img.append({"id": row[1], "src": row[2]})
    data['product_img'] = img

    result = db.engine.execute('select * from tb_product_opt where product_id="'+str(id)+'"')
    opt = []
    optad = []
    opt.append({"value": "請選擇", "label": "請選擇", "disabled": "true"})

    for row in result:
        opt.append({"value": str(row[0]), "label": str(row[2])})
        optad.append({ "price": str(
            row[3]), "string": str(row[2])})
    data["opt"] = opt
    data["optad"] = optad
    return {"Status": "Success", "productdata": data}


def pricegetproduct(id):
    sql = text('select * from tb_product_opt where opt_id="'+str(id)+'"')
    result = db.engine.execute(sql)
    data = {}
    total = 0
    opt = []
    for row in result:
        total = str(row[3])
    opt.append({"value": "請選擇", "label": "請選擇", "disabled": "true"})
   
    data["opt"] = opt

    return {"Status": "Success", "productdata": data, "price": total}


def shopcartget(userid):
    sql = text('select * from tb_shopcart where user_id="'+str(userid)+'"')
    result = db.engine.execute(sql)
    data = []
    total=0
    for row in result:
        rowdata = {}
        productsql = text(
            'select * from tb_product where product_id="'+str(row[2])+'"')
        proresult = db.engine.execute(productsql)

        optsql = text(
            'select * from tb_product_opt where opt_id="'+str(row[4])+'"')
        optresult = db.engine.execute(optsql)

        rowdata["id"] = str(row[0])  # 購買ＩＤ
        for prorow in proresult:
            rowdata['name'] = str(prorow[1])  # 名稱
            # rowdata.append(prorow[0])
            
            for optrow in optresult:
                rowdata["price"] = str(optrow[3])  # 價格
                #rowdata["maxcount"] = str(optrow[4])  # 數量
                rowdata["option"] = str(optrow[2])  # 規格
        

        rowdata['count'] = row[3]
        total+=row[3]*optrow[3]
        rowdata['tot'] = row[3]*optrow[3]
        # rowdata.append(row[3])
        # rowdata.append(row[3]*prorow[2])
        # rowdata.append(None)

        data.append(rowdata)

    return {"data": data,"total":total}


def imgbanner(img):  # 商品頁取得內容

    sql = text('delete from tb_banner')
    result = db.engine.execute(sql)

    for i in img:
        sql = text(
            'insert into `tb_banner` (`banner_filename`) VALUES ("'+str(i)+'")')
        result = db.engine.execute(sql)

    return {"Status": "Success"}


def productnew(product_name, product_describe, opt):  # 新增商品
    sql = text("insert into `tb_product` (`product_name`,`product_describe`) VALUES ('" +
               str(product_name)+"','"+str(product_describe)+"')")
    db.engine.execute(sql)

    opt = json.loads(opt)
    print(opt)
    sql = text("SELECT product_id FROM `tb_product` order by product_id")
    lastid = 0
    result = db.engine.execute(sql)
    for row in result:
        lastid = row[0]
    for item in range(len(opt)):
        sql = text("insert into `tb_product_opt` (`product_id`,`product_opt_item`,`product_opt_price`) VALUES ('" +
                   str(lastid)+"','"+str(opt[item]['string'])+"','"+str(opt[item]['price'])+"')'")
        db.engine.execute(sql)

    return {"Status": "Success", "lastid": lastid}


def newproductimg(lastid, file):  # 新增商品相片
    for i in file:
        sql = text('insert into `tb_product_img` (`product_id`,`product_img_url`) VALUES ("' +
                   str(lastid)+'","http://localhost/shop/product/'+str(lastid)+'/'+str(i)+'")')
        db.engine.execute(sql)

    return {"Status": "Success", "Message": "商品新增成功"}


def listproductadmget():
    sql = text("select * from tb_product ORDER BY `tb_product`.`product_id` ASC")
    result = db.engine.execute(sql)
    data = []
    for row in result:
        rowdata = {}
        rowdata["id"] = row[0]
        rowdata['name'] = row[1]
        rowdata['price'] = row[2]

        data.append(rowdata)
    return {"data": data}


def productdel(id):
    sql = text("delete from tb_product where product_id =  '"+str(id)+"'")
    db.engine.execute(sql)

    return {"Status": "Success"}


def productedit(id, product_name, product_describe, opt):
    sqltext = "update tb_product set `product_name` = '" + \
        str(product_name)+"',`product_describe` = '" + \
        str(product_describe)+"' where `product_id` = '"+str(id)+"'"
    sql = text(sqltext)
    db.engine.execute(sql)

    sqltext = "delete from `tb_product_opt` where product_id = '"+str(id)+"'"
    sql = text(sqltext)
    db.engine.execute(sql)

    opt = json.loads(opt)
    for item in range(len(opt)):
        sql = text("insert into `tb_product_opt` (`product_id`,`product_opt_item`,`product_opt_price`) VALUES ('" +
                   str(id)+"','"+str(opt[item]['string'])+"','"+str(opt[item]['price'])+"')")
        db.engine.execute(sql)

    return {"Status": "Success"}


def editproductimg(lastid, file):
    sql = text(
        "delete from `tb_product_img` where `product_id` = '"+str(lastid)+"'")
    db.engine.execute(sql)
    for i in file:
        sql = text('insert into `tb_product_img` (`product_id`,`product_img_url`) VALUES ("' +
                   str(lastid)+'","http://localhost/shop/product/'+str(lastid)+'/'+str(i)+'")')
        db.engine.execute(sql)

    return {"Status": "Success", "Message": "商品新增成功"}


def cartaddto(userid, product_id, product_count, opt):  # 新增購物車項目
    shopchartid=None
    sql = text("select * from tb_shopcart where user_id='"+str(userid)+"' and item_opt = '"+str(opt)+"'")
    retsult = db.engine.execute(sql)
    for i in retsult:
        shopchartid = i[0]

    if (shopchartid != None):
        sql = text("update tb_shopcart set item_count=item_count+"+str(product_count)+" where shopcart_id = '"+str(shopchartid)+"'")
        db.engine.execute(sql)
    else:
        sql = text("insert into tb_shopcart	(`user_id`,`product_id`,`item_count`,`item_opt`) values ('" +
                str(userid)+"','"+str(product_id)+"','"+str(product_count)+"','"+str(opt)+"')")
        db.engine.execute(sql)
    return "success"

def shopcartcountchange(id, count):  # 修改購物車數量
    sql = text("update `tb_shopcart` set item_count = '" +
               str(count)+"' where `shopcart_id` = '"+str(id)+"'")
    db.engine.execute(sql)
    return "Success"


def cartdel(id):  # 刪除購物車項目
    sql = text("delete from `tb_shopcart` where `shopcart_id` = '"+str(id)+"'")
    db.engine.execute(sql)

    return {"Status": "Success", "Message": "商品新增成功"}


def get_type():
    type = text("select * from tb_producttype")
    result = db.engine.execute(type)

    typedata = []
    for row in result:
        typedata.append({'label': row[1], 'value': row[0]})

    product_data = []
    product = text("select * from tb_product")
    result = db.engine.execute(product)
    for row in result:
        product_data.append({'label': row[1], 'value': row[0]})

    return typedata, product_data


def del_type(typeid):  # 刪除標籤
    type = text("delete from tb_producttype where type_id = '"+str(typeid)+"'")
    db.engine.execute(type)
    return "刪除標籤成功"


def new_type(type):  # 新增標籤
    type = text(
        "insert into tb_producttype (`type_name`) VALUES ('"+str(type)+"')")
    db.engine.execute(type)
    return "新增標籤成功"


def change_type(typeid, type):  # 修改標籤
    type = text("update tb_producttype set `type_name` = '" +
                str(type)+"' where `type_id` = '"+typeid+"'")
    db.engine.execute(type)
    return "修改標籤名稱成功"


def typecont_get(typeid):  # 取得標籤內商品內容
    type = text("select * from tb_typecont where `type_id` = '"+str(typeid)+"'")
    result = db.engine.execute(type)
    data = []
    for row in result:
        data.append(row[2])
    return data


def typecont_change(typeid, data):  # 取得標籤內商品內容
    db.engine.execute(
        "delete from tb_typecont where type_id = '"+str(typeid)+"'")
    if len(data) == 0:
        return "修改成功"
    for i in data:
        db.engine.execute(
            "insert into tb_typecont (`type_id`,`product_id`) value ('"+str(typeid)+"','"+str(i)+"')")
    return "修改成功"

def creatorder(userid,date,name,phone,Logistics,address,TotalAmount,ordermark):
    db.engine.execute("insert into `tb_order` (user_id,order_time,user_name,user_phone,order_LogisticsType,order_address,order_total,order_mark,order_state) values ("+str(userid)+",'"+str(date)+"','"+str(name)+"','"+str(phone)+"','"+str(Logistics)+"','"+str(address)+"','"+str(TotalAmount)+"','"+str(ordermark)+"','代付款')")
    orderid = db.engine.execute("select max(order_id) from `tb_order`")
    lastorderid=0
    for i in orderid:
        lastorderid = i[0]
    shop = db.engine.execute("SELECT * FROM tb_shopcart INNER JOIN tb_product ON tb_product.product_id = tb_shopcart.product_id INNER JOIN tb_product_opt ON tb_product_opt.opt_id = tb_shopcart.item_opt where user_id = "+userid+";")
    for row in shop:
        db.engine.execute("insert into `tb_orderitem` (order_id,product_name,product_opt_item,product_opt_price,item_count) values ('"+str(lastorderid)+"','"+str(row[6])+"','"+str(row[11])+"','"+str(row[12])+"','"+str(row[3])+"')")
    db.engine.execute("delete from tb_shopcart where user_id = '"+str(userid)+"'")
    return lastorderid

def orderget(userid):
    data=[]
    order = db.engine.execute("select * from `tb_order` where user_id='"+str(userid)+"'")
    for i in order:
        temp={}
        temp["order_id"] = i[0]
        temp["order_time"] = i[2]
        temp['user_name'] = i[3]
        temp['order_LogisticsType'] = i[5]
        temp['order_total'] = i[7]
        temp['status'] = i[9]
        data.append(temp)
    return data

def updatestatus(orderid): #付款完成更新狀態
    print("update `tb_order` set order_state='已付款' where order_id = '"+str(orderid)+"'")
    db.engine.execute("update `tb_order` set order_state='已付款' where order_id = '"+str(orderid)+"'")
    return "success"

def orderre(order_id): #付款失敗重新付款
    item = db.engine.execute("select * from `tb_order` where order_id='"+str(order_id)+"'")
    total=0
    for i in item:
        total=i[7]
    
    return total
