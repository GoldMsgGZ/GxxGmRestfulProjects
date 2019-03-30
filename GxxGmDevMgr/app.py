#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8


from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
import ConfigParser
import json

app = Flask(__name__)
#app = Flask('GxxGmDevMgr')

# 读取配置文件
config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))

# 配置文件服务监听部分
listen_ip = config.get("SERVER_INFO", "LISTEN_IP")
listen_port = config.get("SERVER_INFO", "LISTEN_PORT")


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

    return 'OK'


if __name__ == '__main__':
    app.run(host=str(listen_ip), port=int(listen_port), debug=True)
