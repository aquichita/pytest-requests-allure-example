'''
@Author: your name
@Date: 2020-07-21 11:23:43
@LastEditTime: 2020-07-22 11:33:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\lib\log.py
'''
from dataclasses import dataclass
import logging
import os
import sys
from pathlib import Path

import yaml

logger = logging.getLogger()
log_file = Path.joinpath(Path(".").resolve(), Path("Gofers.log"))
if Path.exists(log_file):
    os.remove(log_file)
with open(log_file, mode='w', encoding='utf-8') as f:
    f.close()

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s %(filename)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')

ch = logging.StreamHandler()
ch.setFormatter(formatter)

fh = logging.FileHandler(log_file, encoding='utf-8')
fh.setFormatter(formatter)


def handlerHelper(func):
    def wrapper(*args, **kwargs):
        logger.addHandler(ch)
        logger.addHandler(fh)
        func(*args, **kwargs)
        logger.removeFilter(ch)
        logger.removeFilter(fh)

    return wrapper


@handlerHelper
def debug(msg):
    logger.debug(msg)


@handlerHelper
def info(log_meg):
    logger.info(log_meg)


@handlerHelper
def warning(log_meg):
    logger.warning(log_meg)


@handlerHelper
def error(log_meg):
    logger.error(log_meg)


@handlerHelper
def critical(log_meg):
    logger.error(log_meg)


def gen_allure_rep(allure, allure_dir, allure_report):
    if allure_dir:
        try:
            print('\n')
            os.system(f'{allure} generate -c {allure_dir} -o {allure_report}')
            if sys != 'Linux':
                os.system(f'{allure} open {allure_report}')
        except Exception as e:
            print(e)


def gen_html_rep(parameter_list):
    ...


yaml.warnings({'YAMLLoadWarning': False})
_conffile = Path(".").resolve() / Path("env.yaml")
sql_file_teardown = Path(".").resolve() / Path("extras") / \
    Path("data") / Path("teardown.yaml")


@dataclass
class Yml:
    path: str

    def __new__(cls, path, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with open(str(path), 'rb') as yf:
                cls.yc = yaml.safe_load(yf)
            cls._instance = super().__new__(cls)
        return cls._instance

    def __getitem__(self, key: str = None):
        return str(self.yc[key]) if key in self.yc else None

    @property
    def parametertable(self):
        return dict(self.yc)


if __name__ == "__main__":
    print(Yml(_conffile).parametertable)
    print(Yml(sql_file_teardown).parametertable)
