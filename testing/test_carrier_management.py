'''
@Author: your name
@Date: 2020-07-15 15:59:46
@LastEditTime: 2020-07-24 17:25:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\testing\test_materials_type.py
'''
from lib.parameter import xid
import allure
import pytest


@allure.epic("基础数据")
@allure.feature("承运商")
class TestCarrierManagement:
    @allure.story("承运商管理")
    @allure.title("承运商管理-新建")
    @allure.severity("normal")
    def test_submit(self, tms):
        """新建承运商-默认参数"""
        rep = tms.carrierManagement.submit(
            xid="AT-CARRIER-001",
            name="AT-承运商-001",
        )
        assert rep.json()["success"]
