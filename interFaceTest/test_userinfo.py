#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 作业23：
# 1.把登录写到fixture
# 2.pytest写的其它测试用例，修改个人信息，调用登录的fixture
# url = "http://49.235.92.12:9000/api/v1/userinfo"
#  body = {"name": "test",
# "sex": "M",
# "age": 20,
# "mail": "283340479@qq.com" }
import pytest
import requests
from interFaceTest.func_login import login


@pytest.fixture(scope="function")
def login_fix():
    print("登录")
    s = requests.Session()
    login(s)
    return s


def test_info(login_fix):
    print("用力1")
    s = login_fix
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    body = {"name": "test",
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"}
    r = s.post(url=url, json=body)
    print(r.text)
