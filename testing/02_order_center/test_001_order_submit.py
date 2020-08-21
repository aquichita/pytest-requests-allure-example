import allure
import pytest


@allure.epic("订单中心")
@allure.feature("订单")
@allure.story("订单新建")
@allure.title("新建订单1")
@allure.severity("normal")
@pytest.mark.dependency(depends=["test_order_submit2"])
@pytest.mark.single
def test_order_submit1(tms_om_save):
    """新建订单-默认参数1"""
    rep = tms_om_save
    pytest.assume(rep.json()["success"])
    pytest.assume(rep.json()["code"] == "0000")


@allure.epic("订单中心")
@allure.feature("订单")
@allure.story("订单新建")
@allure.title("新建订单2")
@allure.severity("normal")
@pytest.mark.flaky(reruns=3, reruns_delay=2)
@pytest.mark.dependency()
@pytest.mark.flow
def test_order_submit2(tms_om_save):
    """新建订单-默认参数2"""
    rep = tms_om_save
    code = rep.json()["code"]
    success = rep.json()["success"]
    pytest.assume(code == "0001")
    pytest.assume(success == True)
