'''
@Author: your name
@Date: 2020-07-20 15:34:58
LastEditTime: 2020-08-12 15:59:15
LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\conftest.py
'''
import json
import os
from pytest import fixture

from lib import gofers
from steps.interfaces import public
from steps.interfaces.base_data.carrier_management import CarrierManagement


def pytest_sessionstart():
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
def htms():
    gofers.info(
        json.dumps(
            dict(os.environ),
            sort_keys=True,
            indent=4
        ).encode('utf-8').decode('unicode_escape')
    )
    return public.user_info()


@fixture(scope="session", autouse=True)
def tms(htms):
    class OP():
        carrierManagement = CarrierManagement(htms)
    return OP()
