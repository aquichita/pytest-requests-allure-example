'''
@Author: Aquichita
@Date: 2020-07-09 17:15:27
@LastEditors: Please set LastEditors
@LastEditTime: 2020-07-15 16:09:05
'''
import dataclasses
import platform
import shutil
from pathlib import Path

from pytest import fixture

from lib.utils import _conffile, gen_allure_rep, getattr
from steps.interfaces.base_data import materials_type
from steps.interfaces.public import login, user_info

PROJECT_ROOT = Path(".").resolve()
REP_DIR = PROJECT_ROOT / Path("report")
RES_DIR = REP_DIR / Path("allure-results")
ALL_REP = REP_DIR / Path("allure-report")
EXTRAS_DIR = PROJECT_ROOT / Path("extras")


def allure():
    version = getattr("allure_version")
    if platform.system() != "Windows":
        name = "allure"
    else:
        name = "allure.bat"
    return EXTRAS_DIR / \
        Path("allure-".join(version)) / \
        Path("bin") / \
        Path(name)


def pytest_sessionstart():
    if Path(REP_DIR).exists():
        shutil.rmtree(path=REP_DIR)


def pytest_sessionfinish(session):
    # pytest --alluredir report/allure-results
    allure_dir = session.config.getoption('allure_report_dir')
    gen_allure_rep(
        allure=allure(),
        allure_dir=allure_dir,
        allure_report=ALL_REP
    )


@fixture(scope="session", autouse=True)
def session():
    login()
    user_info()
    ...


@fixture(scope="session", autouse=True)
def tms(session):
    @dataclasses
    class OP:
        materialstype = materials_type.MaterialsType()
    return OP()


if __name__ == "__main__":
    print(_conffile)
