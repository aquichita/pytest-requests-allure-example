'''
@Author: your name
@Date: 2020-07-20 15:34:58
@LastEditTime: 2020-07-20 15:36:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\lib\parameters.py
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import random
import string
import datetime
from collections import OrderedDict

START_DATE = "2020-01-01 00:00:00"
END_DATE = "2022-12-31 00:00:00"


def zh(length: int = 9) -> str:
    '''
    @msg: 随机生成指定长度的中文字符串
    @param {type} ： length=指定长度
    @return: 指定长度的中文字符串
    '''
    zhs: str = ""
    for i in range(length):
        zhs += chr(random.randint(0x4e00, 0x9fbf))
    return zhs


def en(length: int = 16) -> str:
    zhs = [random.choice(string.digits + string.ascii_letters)
           for i in range(length)]
    zhs = "".join(zhs)
    return zhs


def email(head: str = None) -> str:
    email_head = en() if not head else head
    email_end = random.choice((
        '@163.com',
        '@qq.com',
        '@126.com',
        '@outlook.com',
        '@hand-china.com'
    ))
    return email_head + email_end


def phone() -> str:
    head = ["130", "131", "132", "133", "134",
            "135", "136", "137", "138", "139",
            "147", "150", "151", "152", "153",
            "155", "156", "157", "158", "159",
            "186", "187", "188"]
    number = "".join(random.choice("0123456789") for i in range(8))
    return random.choice(head) + number


def b64encrypt(s: str) -> str:
    bytesString = s.encode(encoding='utf-8')
    return base64.b64encode(bytesString)


def dater(days: int = 7, weeks: int = 0,) -> datetime:
    start_date = datetime.datetime.today()
    work_date = datetime.timedelta(
        days=days,
        weeks=weeks
    )
    end_date = start_date + work_date
    return OrderedDict(
        start=start_date.strftime("%Y-%m-%d %H:%M:%S"),
        end=end_date.strftime("%Y-%m-%d %H:%M:%S")
    )


def xid(length: int = 9) -> str:
    default_str = "AT_RESOURCE_PRE_"
    str_list = [random.choice(string.digits + string.ascii_letters)
                for i in range(length)]
    random_str = ''.join(str_list)
    return default_str + random_str


def today(parameter_list):
    """2020-07-19 00:00:00"""
    ...
