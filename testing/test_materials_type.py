'''
@Author: Aquichita
@Date: 2020-07-15 15:59:46
@LastEditors: Please set LastEditors
@LastEditTime: 2020-07-15 16:00:33
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
