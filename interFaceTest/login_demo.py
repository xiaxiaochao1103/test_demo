#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 作业22：
# 1.写一个登陆的函数，参数账号和密码可以灵活切换
# http://49.235.92.12:9000/api/v1/login
# body = {"username": "test",  "password": "123456"}
# 2.登录单独写一个py文件，其它.py文件地方导入登录的模块
import requests
import pytest


@pytest.fixture(scope="function")
def login(username, password):
    url = "http://49.235.92.12:9000/api/v1/login"
    body = {
        "username": username,
        "password": password
    }

    s = requests.Session()
    r = s.post(url=url, json=body)
    token = r.json()["token"]
    h = {
        "Authorization": "Token %s" % token
    }

    s.headers.update(h)
    return s