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

def login(ac, pw): #登入
    try:       
        sql = text('select * from tb_user where User_account="'+str(ac)+'" and user_password="'+str(pw)+'"')
        result = db.engine.execute(sql)
        data=[]
        for row in result:
            data=[row[1],row[2],row[3],row[4],row[5]]
        if (len(data) ==0):
            return {"Status":"Failed" , "Message": "帳號密碼錯誤"}   
        else:
            return {"Status":"Success" , "Message": str(data[0])+"您好","data":data}
    except Exception as e:
        print("error occur: %s" % (e))

def newaccount(account,name, password,phone,email): #註冊
    try:
        #查詢帳號是否存在
        sql = text('select * from tb_user where User_account="'+str(account)+'"')
        result = db.engine.execute(sql)
        data=[]
        for row in result:
            data=[row[1]]
        if len(data) == 1:
            return {"Status":"Failed" , "Message": "帳號已存在"}
        
        #建立新帳號
        sql = text("insert into tb_user (User_account,User_name,User_password,User_phone,User_email) VALUES ('"+account+"','"+name+"','"+password+"','"+phone+"','"+email+"')")
        result = db.engine.execute(sql)
        print(result)
        return {"Status":"Success" , "Message": "帳號建立成功"}
    except Exception as e:
        print("error occur: %s" % (e))


def sendvaildresetpwd(account,email): #重設密碼接收驗證碼
    try:
        #查詢帳號是否存在
        sql = text('select * from tb_user where User_account="'+str(account)+'" and User_email="'+str(email)+'"')
        result = db.engine.execute(sql)
        data=[]
        for row in result:
            data=[row[0],row[5]]
        if len(data) == 0:
            return {"Status":"Failed" , "Message": "帳號或信箱錯誤"}
        
        #產生驗證碼
        code = ''
        for i in range(5):
            num = str(random.randrange(10))     # 得到隨機數字並轉化成字元
            zm = chr(random.randrange(97, 123))     # 得到小寫字母的ascii碼值用chr轉換成字母
            zm_d = chr(random.randrange(65, 91))    # 得到大寫字母的ascii碼值用chr轉換成字母
            single = random.choice([num, zm, zm_d]) # 得到隨機的一個字元
            code += single                          # 字串拼接                
    
        #先刪除，後新增
        sq ="delete from tb_vaildcode where User_id = "+str(data[0])
        sql = text(sq)
        result = db.engine.execute(sql)    
        
        sq ="insert into tb_vaildcode (User_id,Vaildcode_code) VALUES ("+str(data[0])+","+"'"+str(code)+"')"
        sql = text(sq)
        result = db.engine.execute(sql)

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('asdfg199715@gmail.com','jsvquecuzexlumxj')
        message = MIMEText('您的重設驗證碼：'+str(code), 'plain', 'utf-8')
        message['From'] = Header("easy shop購物網站", 'utf-8')   # 发送者
        message['To'] =  Header("easy shop@gmail.com", 'utf-8')        # 接收者
        
        subject = '密碼重設信件'
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj.sendmail("asdfg199715@gmail.com", [str(data[1])], message.as_string())
        smtpObj.quit()  #關閉本地端對遠端郵件伺服器的連線

        return {"Status":"Success" , "Message": "驗證碼已寄到您的信箱","id":data[0]}

    except Exception as e:
        print("error occur: %s" % (e))

#重設密碼
def pwdreset(id,code,password) :
   
    sql = text('select * from tb_vaildcode where User_id="'+str(id)+'" and Vaildcode_code="'+str(code)+'"')
    result = db.engine.execute(sql)
    data=[]
    print(id)
    print(code)
    for row in result:
        data=[row[1],row[0]]
    if len(data) == 0:
        return {"Status":"Failed" , "Message": "驗證碼錯誤"}
    else:
        sql = "update tb_user set User_password = '"+str(password)+"' where User_id='"+str(data[0])+"'"
        result = db.engine.execute(sql)

        sql = "delete from tb_vaildcode where Vaildcode_id = '"+str(data[1])+"'"
        result = db.engine.execute(sql)

        return {"Status":"Success" , "Message": "密碼已修改"}