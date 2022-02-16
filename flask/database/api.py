# -*- coding: utf-8 -*-
# https://myapollo.com.tw/2016/09/28/python-sqlalchemy-orm-1/

from operator import le
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
