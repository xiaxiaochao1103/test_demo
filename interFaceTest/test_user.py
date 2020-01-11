#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
import pytest
import re


# 作业20：
# 用session会话保持方法，登录http://49.235.92.12:9000/admin/login/
# 账号 admin密码yoyo123456
# 并判断是否登录成功
# def test_login():
#     url = "http://49.235.92.12:9000/admin/login/"
#     s = requests.Session()
#     r = s.get(url=url)
#
#     csrfmiddlewaretoken = re.findall("'csrfmiddlewaretoken' value='(.+?)'", r.text)
#     print(csrfmiddlewaretoken)
#
#     body = {
#         "csrfmiddlewaretoken": csrfmiddlewaretoken,
#         "username": "admin",
#         "password": "yoyo123456",
#         "next": "/admin/"
#     }
#     r = s.post(url=url, data=body)
#     assert "Django administration" in r.text


# 作业21：
# session自动关联token，登录成功后把token更新到头部，后面所有请求自动带上token
# http://49.235.92.12:9000/api/v1/login
# body = {"username": "test",  "password": "123456"}
# 获取个人信息
# http://49.235.92.12:9000/api/v1/userinfo

from interFaceTest.login_demo import login


def test_get_userinfo():
    url2 = "http://49.235.92.12:9000/api/v1/userinfo"
    body = {
        "username": "test",
        "password": "123456"
    }
    s = login(body["username"], body["password"])

    r2 = s.get(url=url2, json=body)
    print(r2.json())
    assert r2.json()["msg"] == "sucess!" and r2.json()["code"] == 0


