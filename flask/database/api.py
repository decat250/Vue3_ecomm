# -*- coding: utf-8 -*-
# https://myapollo.com.tw/2016/09/28/python-sqlalchemy-orm-1/

from operator import le
import re
from this import d
from unicodedata import name
from sqlalchemy import create_engine, and_, exc, Integer, ForeignKey, String, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import case

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


def login(ac, pw):  # 登入
    try:
        sql = text('select * from tb_user where User_account="' +
                   str(ac)+'" and user_password="'+str(pw)+'"')
        result = db.engine.execute(sql)
        data = []
        for row in result:
            data = [row[1], row[2], row[3], row[4], row[5], row[0]]
        if (len(data) == 0):
            return {"Status": "Failed", "Message": "帳號密碼錯誤"}
        else:
            return {"Status": "Success", "Message": str(data[0])+"您好", "data": data}
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


def productgetlist():  # 首頁取得商品
    sql = text('select * from tb_banner')
    result = db.engine.execute(sql)
    banner = []
    for row in result:
        banner.append(
            {"banner_id": str(row[0]), "item": "http://localhost/shop/banner/"+str(row[1])})
    sql = text('select * from tb_product')
    result = db.engine.execute(sql)
    data = []
    for row in result:
        sql = text('select * from `tb_product_img` where `product_id` = "' +
                   str(row[0])+'" order by product_id')
        img = db.engine.execute(sql)
        imgsrc = ""
        for imgrow in img:
            imgsrc = imgrow[2]
        data.append({"product_id": str(row[0]), "product_name": str(row[1]), "product_price": str(
            row[2]), "product_count": str(row[3]), "product_img": str(imgsrc)})
    return {"Status": "Success", "productlist": data, "bannerimg": banner}


def infogetproduct(id):  # 商品頁取得內容

    sql = text('select * from tb_product where product_id="'+str(id)+'"')
    result = db.engine.execute(sql)
    data = {}
    num = []
    for row in result:

        data["product_id"] = str(row[0])
        data['product_name'] = str(row[1])
        data['product_price'] = str(row[2])
        data['product_count'] = str(row[3])
        data['product_describe'] = str(row[5])
        for i in range(int(row[3])):
            num.append({"label": str(i+1), "value": str(i+1)})
    data["num"] = num

    sql = text('select * from tb_product_img where product_id="'+str(id)+'"')
    result = db.engine.execute(sql)
    img = []
    for row in result:
        img.append({"id": row[1], "src": row[2]})
    data['product_img'] = img

    sql = text('select * from tb_product_opt where product_id="'+str(id)+'"')
    result = db.engine.execute(sql)
    opt = []
    optadm = []
    for row in result:
        optadm.append(row[2])
        opt.append({"label": str(row[2]), "value": str(row[0])})
    data["opt"] = opt
    data['optadm'] = optadm

    return {"Status": "Success", "productdata": data}


def shopcartget(userid):
    sql = text('select * from tb_shopcart where user_id="'+str(userid)+'"')
    print('select * from tb_shopcart where user_id="'+str(userid)+'"')
    result = db.engine.execute(sql)
    data = []
    for row in result:
        rowdata = []
        productsql = text('select * from tb_product where product_id="'+str(row[2])+'"')
        proresult = db.engine.execute(productsql)

        optsql = text('select * from tb_product_opt where opt_id="'+str(row[4])+'"')
        optresult = db.engine.execute(optsql)  

        rowdata.append(row[0]) #購買ＩＤ
        for prorow in proresult:
            #rowdata.append(prorow[0])
            rowdata.append(prorow[1]) #價格
            for optrow in optresult:
                rowdata.append(optrow[2])

            rowdata.append(prorow[2]) #數量

        rowdata.append(row[3])
        #rowdata.append(row[3]*prorow[2])
        #rowdata.append(None)


        data.append(rowdata)
    return {"data": data}


def imgbanner(img):  # 商品頁取得內容

    sql = text('delete from tb_banner')
    result = db.engine.execute(sql)

    for i in img:
        sql = text(
            'insert into `tb_banner` (`banner_filename`) VALUES ("'+str(i)+'")')
        result = db.engine.execute(sql)

    return {"Status": "Success"}


def productnew(product_name, product_count, product_price, product_describe, opt):  # 新增商品
    sql = text("insert into `tb_product` (`product_name`,`product_price`,`product_count`,`product_describe`) VALUES ('" +
               str(product_name)+"','"+str(product_count)+"','"+str(product_price)+"','"+str(product_describe)+"')")
    result = db.engine.execute(sql)

    sql = text("SELECT product_id FROM `tb_product` order by product_id")
    lastid = 0
    result = db.engine.execute(sql)
    for row in result:
        lastid = row[0]
    for item in opt:
        sql = text("insert into `tb_product_opt` (`product_id`,`product_opt_item`) VALUES ('" +
                   str(lastid)+"','"+str(item)+"')")
        db.engine.execute(sql)

    return {"Status": "Success", "lastid": lastid}


def newproductimg(lastid, file):  # 新增商品相片
    for i in file:
        sql = text('insert into `tb_product_img` (`product_id`,`product_img_url`) VALUES ("' +
                   str(lastid)+'","http://localhost/shop/product/'+str(lastid)+'/'+str(i)+'")')
        result = db.engine.execute(sql)

    return {"Status": "Success", "Message": "商品新增成功"}


def listproductadmget():
    sql = text("select * from tb_product ORDER BY `tb_product`.`product_id` ASC")
    result = db.engine.execute(sql)
    data = []
    for row in result:
        rowdata = []
        rowdata.append(row[0])
        rowdata.append(row[1])
        rowdata.append(row[2])
        rowdata.append(row[3])
        rowdata.append(row[4])

        data.append(rowdata)
    return {"data": data}


def productdel(id):
    sql = text("delete from tb_product where product_id =  '"+str(id)+"'")
    db.engine.execute(sql)

    return {"Status": "Success"}


def productedit(id, product_name, product_count, product_price, product_describe, opt):
    sqltext = "update tb_product set `product_name` = '"+str(product_name)+"', `product_count` = '"+str(product_count)+"',`product_price` = '"+str(
        product_price)+"',`product_describe` = '"+str(product_describe)+"' where `product_id` = '"+str(id)+"'"
    sql = text(sqltext)
    print(sqltext)
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


def cartaddto(userid, product_id, product_count, opt): #新增購物車項目
    sql = text("insert into tb_shopcart	(`user_id`,`product_id`,`item_count`,`item_opt`) values ('" +
               str(userid)+"','"+str(product_id)+"','"+str(product_count)+"','"+str(opt)+"')")
    db.engine.execute(sql)


def cartdel(id): #刪除購物車項目
    sql = text("delete from `tb_shopcart` where `shopcart_id` = '"+str(id)+"'")
    db.engine.execute(sql)

    return {"Status": "Success", "Message": "商品新增成功"}

