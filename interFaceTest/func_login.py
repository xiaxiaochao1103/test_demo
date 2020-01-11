#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests


def login(s):


    url = "http://49.235.92.12:9000/api/v1/login"
    body = {
        "username": "test",
        "password": "123456"
    }

    r = s.post(url, json=body)
    print(r.json())

    token = r.json()["token"]
    print(token)

    h = {
        "Authorization": "Token %s" % token
    }

    s.headers.update(h)
    print(s.headers)
    return token


if __name__ == "__main__":
    s = requests.Session()
    token = login(s)
    url2 = "http://49.235.92.12:9000/api/v1/userinfo"
    r2 = s.get(url2)
    print(r2.text)