#!/usr/bin/python
# -*- coding: UTF-8 -*-


# python作业15：
# 根据接口文档使用python发get请求，能请求成功
# 历史上的今天AppKey：57d46b7258fc47e14290c33537f23d36
# https://www.juhe.cn/docs/api/id/63
# import requests
# url = "http://api.juheapi.com/japi/toh"
# data = {
#     "key": "57d46b7258fc47e14290c33537f23d36",
#     "v": "1.0",
#     "month": "1",
#     "day": "2"
# }
# r = requests.get(url=url, params=data)
# print(r.text)


# python作业16：
# 使用python发post请求，
# 登陆接口基本信息
# POST /api/v1/login
# Content-Type: application/json
# {"username":"test","password":"123456"}
# 接口服务部署ip地址49.235.92.12， 端口9000
# 要求：
# 1.根据接口文档和部署地址拼接请求，能登录成功
# 2.取出token值，并打印出来
#
# import requests
# import json
# host = "http://49.235.92.12:9000"
# api = "/api/v1/login"
# data = {
#     "username": "test",
#     "password": "123456"
# }
# headers = {
#     "Content-Type": "application/json"
# }
#
# r = requests.post(url=host+api, json=data, headers=headers)
# content = r.text
# print(content)
# text_dict = json.loads(content)
# print(text_dict.get("token"))


# python作业19：
# 访问接口地址http://49.235.92.12:9000/api/test/demo（不需要登录）
# 根据name为yoyo111（list里面顺序不是固定的），取出对应的email值：123445@qq.com
# res_dict = {"code": 0, "msg": "success!", "datas":
#     [{"age": 20, "create_time": "2019-09-15", "id": 1, "mail": "283340479@qq.com", "name": "yoyo", "sex": "M"},
#      {"age": 21, "create_time": "2019-09-16", "id": 2, "mail": "123445@qq.com", "name": "yoyo111", "sex": "M"}]}

import requests
import json

url = "http://49.235.92.12:9000/api/test/demo"
r = requests.get(url=url)
res_dict = json.loads(r.text)
for data in res_dict["datas"]:
    for key, values in data.items():
        if values == "yoyo111":
            print(data.get("mail"))
