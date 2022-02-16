# -*- coding: utf-8 -*-
from database.database import db

# 自己設定的名稱，可以跟Database的Table不同


class tb_user(db.Model):
    __tablename__ = 'tb_user'  # 是Database裡面的哪個Table

    User_id = db.Column(db.Integer, primary_key=True)
    User_account = db.Column(db.VARCHAR(30))
    User_name = db.Column(db.VARCHAR(30))
    User_password = db.Column(db.VARCHAR(30))
    User_phone = db.Column(db.VARCHAR(30))
    User_email = db.Column(db.VARCHAR(30))

    def __init__(self, User_id, User_account, User_name, User_password, User_phone, User_email):
        self.User_id = User_id
        self.User_account = User_account
        self.User_name = User_name
        self.User_password = User_password
        self.User_phone = User_phone
        self.User_email = User_email
