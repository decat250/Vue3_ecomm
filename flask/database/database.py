# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False#一定要設定
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/fet'#連接字串
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://decat:Dnj4.qIaugsqVJ3-@localhost:3306/test"

db = SQLAlchemy(app)#設定DB的物件

