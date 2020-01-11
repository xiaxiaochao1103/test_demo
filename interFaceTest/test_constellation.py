#!/usr/bin/python
# -*- coding: UTF-8 -*-


# python作业18：
# 根据作业17写的接口用例，任意选其中的3条用例
# 用pytest代码实现，执行结果截图
import json
import pytest
import requests
import pymysql


def test_normal_operation_01():
    url = "http://web.juhe.cn:8080/constellation/getAll"
    data = {
        "key": "cde5e16435cd0217f505a88898b60707",
        "consName": "天蝎座",
        "type": "year"
    }
    r = requests.get(url=url, params=data)
    res_dict = json.loads(r.content)
    print(res_dict, res_dict["resultcode"], res_dict["error_code"])
    assert res_dict["resultcode"] == "200" and res_dict["error_code"] == 0


def test_error_key_02():
    url = "http://web.juhe.cn:8080/constellation/getAll"
    data = {
        "key": "cde5e16435cd0217f505a88898b60707s",
        "consName": "天蝎座",
        "type": "year"
    }
    r = requests.get(url=url, params=data)
    res_dict = json.loads(r.content)
    print(res_dict, res_dict["resultcode"], res_dict["error_code"])
    assert res_dict["resultcode"] == "101" and res_dict["reason"] == "KEY ERROR!"


def test_error_en_consName_03():
    url = "http://web.juhe.cn:8080/constellation/getAll"
    data = {
        "key": "cde5e16435cd0217f505a88898b60707",
        "consName": "Scorpio",
        "type": "year"
    }
    r = requests.get(url=url, params=data)
    res_dict = json.loads(r.content)
    print(res_dict, res_dict["resultcode"], res_dict["error_code"])
    assert res_dict["error_code"] == 205801 and res_dict["reason"] == "NAME ERROR!"
