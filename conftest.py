'''
@Author: your name
@Date: 2020-07-20 15:34:58
@LastEditTime: 2020-07-24 16:53:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\conftest.py
'''
import dataclasses

from pytest import fixture

from lib import gofers
from steps.interfaces import public
from steps.interfaces.base_data.carrier_management import CarrierManagement


def pytest_sessionstart():
    gofers.projectmark()
    gofers.mysql.exec_sqlyml(
        gofers.SQL_DIR.joinpath("teardown.yaml"),
        msg="环境清理"
    )
    ...


def pytest_sessionfinish(session):
    # pytest --alluredir report/allure-results
    allure_dir = session.config.getoption('allure_report_dir')
    gofers.gen_allure_rep(allure_dir=allure_dir)
    ...


@fixture(scope="session", autouse=True)
def session():
    gofers.info(public.login())
    gofers.info(public.user_info())
    ...


@fixture(scope="session", autouse=True)
def tms(session):
    @dataclasses
    class OP:
        carrierManagement = CarrierManagement()
    return OP()
