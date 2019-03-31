#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8


from flask import Flask
from flask import request

from flask_sqlalchemy import SQLAlchemy
import pymysql

import ConfigParser
import json


#######################################################################################################################
#
# 读取配置文件
config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))

# 配置文件服务监听部分
listen_ip = config.get("SERVER_INFO", "LISTEN_IP")
listen_port = config.get("SERVER_INFO", "LISTEN_PORT")

# 配置数据库参数
mysql_host = config.get("DATABASE", "HOST")
mysql_port = config.get("DATABASE", "PORT")
mysql_username = config.get("DATABASE", "PORT")
mysql_password = config.get("DATABASE", "PORT")
mysql_dbname = config.get("DATABASE", "PORT")
mysql_connect_string = "mysql+pymysql://%s:%s@%s:%d/%s" %\
                       (str(mysql_username), str(mysql_password), str(mysql_host), int(mysql_port), str(mysql_dbname))




#######################################################################################################################
#
# 创建服务实例
#app = Flask(__name__)
app = Flask('GxxGmDevMgr')

app.config["SQLALCHEMY_DATABASE_URI"] = mysql_connect_string

app.config["SQLALCHEMY_COMMIT_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

# 获取数据库实例对象
database = SQLAlchemy(app)

#######################################################################################################################
#
# 具体的接口实现

# 这是一个样例接口
@app.route('/')
def hello_world():
    return 'Hello World!'


# 增加设备
@app.route('/GxxGm/DevMgr/AddDsj', methods=['POST'])
def add_device():
    raw = request.get_data()
    raw_json = json.loads(raw)
    # 取出设备信息
    device_code = raw_json["device_code"]
    device_name = raw_json["device_name"]
    device_state = raw_json["device_state"]

    return 'OK'


if __name__ == '__main__':
    app.run(host=str(listen_ip), port=int(listen_port), debug=True)
