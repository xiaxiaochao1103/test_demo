#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests

s = requests.Session()

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


url2 = "http://49.235.92.12:9000/api/v1/userinfo"
r2 = s.get(url2)
print(r2.text)


url3 = "http://49.235.92.12:9000/api/v1/userinfo"
body1 = {
    "name": "test",
    "sex": "M",
    "age": 20,
    "maill": "283340479@qq.com"
}
r3 = s.post(url3, json=body1)
print(r3.text)