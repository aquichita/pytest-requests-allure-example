'''
@Author: your name
@Date: 2020-07-15 15:59:46
@LastEditTime: 2020-07-23 11:31:29
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\testing\test_materials_type.py
'''
import allure
import pytest


@allure.epic("基础数据")
@allure.feature("物料")
class TestMaterialsType:
    @pytest.mark.run(order=1)
    @allure.story("物料大类")
    @allure.title("物料大类-新建")
    @allure.severity("normal")
    def test_submit(self, tms):
        """新建物料大类-默认参数"""
        rep = tms.materials_type.submit(
            xid="TEST_MATERIALS_TYPE_001",
            name="TEST_MATERIALS_TYPE_001",
        )
        assert rep.json()["success"]
