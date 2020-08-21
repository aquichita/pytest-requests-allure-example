'''
@Author: your name
@Date: 2020-07-13 10:01:30
LastEditTime: 2020-08-18 14:50:50
LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\steps\interfaces\public.py
'''
import os
import re
import allure
from lib import client, gofers


@allure.step('登录认证')
def login(
    username=os.environ.get('username'),
    password=os.environ.get('password'),
):
    login_info = dict(
        username=username,
        password=gofers.rsa(password),
    )
    client.get('/oauth/login')
    login_response = client.post(
        path='/oauth/login',
        data=login_info,
        allow_redirects=False
    )
    # 302
    login_resp_loc = login_response.headers.get('Location')
    set_cookie = login_response.headers.get('Set-Cookie')
    client_id = re.search('client_id=(.*?)&', login_resp_loc).group(1)
    redirect_uri = re.search('redirect_uri=(.*?)$', login_resp_loc).group(1)
    headers302 = dict(
        Cookie=set_cookie.split(';')[0],
    )
    authorization = client.get(
        f"/oauth/oauth/authorize?response_type=token&client_id={client_id}&redirect_uri={redirect_uri}",
        headers=headers302,
        allow_redirects=False
    )
    access_token = "bearer " + \
        re.search(
            "access_token=(.*?)&",
            authorization.headers["Location"]
        ).group(1)
    allure.attach(access_token, "access_token")
    return dict(Authorization=access_token)


@allure.step('获取用户信息')
def user_info():
    auth = login()
    response = client.get(
        "/iam/hzero/v1/users/self",
        headers=auth
    )
    return dict(
        Authorization=auth,
        tenantId=str(response.json()["tenantId"])
    )
