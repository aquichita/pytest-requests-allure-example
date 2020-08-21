import json
import os
from pytest import fixture
import pytest

from lib import gofers
from steps.interfaces import public
from steps.macros.order_center import order


def pytest_sessionstart():
    ...


def pytest_sessionfinish(session):
    # pytest --alluredir report/allure-results
    allure_dir = session.config.getoption('allure_report_dir')
    gofers.gen_allure_rep(allure_dir=allure_dir)
    ...


@fixture(scope="session", autouse=True)
def htms():
    json.dumps(
        dict(os.environ),
        sort_keys=True,
        indent=4
    ).encode('utf-8').decode('unicode_escape')
    return public.user_info()


@fixture(scope="session", autouse=True)
def tms(htms):
    class OP():
        order = order.Order(htms)
    return OP()


def pytest_configure(config):
    config._metadata.pop("JAVA_HOME")


@pytest.mark.optionalhook
def pytest_html_zh_results_table_header(cells):
    cells.pop(-1)


@pytest.mark.optionalhook
def pytest_html_zh_results_table_row(report, cells):
    cells.pop(-1)
