import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path

import mysql.connector
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
sql_file_teardown = Path(".").resolve().joinpath(
    Path("extras"),
    Path("data"),
    Path("teardown.yaml")
)


@dataclass
class Yml:
    path: str

    def __getitem__(self, key: str = None):
        return str(self.yc[key]) if key in self.yc else None

    @property
    def parametertable(self):
        if Path.exists(self.path):
            with open(str(self.path), 'rb') as yf:
                self.yc = yaml.safe_load(yf)
            return dict(self.yc)


@dataclass
class mysql:
    db_info: dict = Yml(_conffile).parametertable
    def __new__(cls, path, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with open(str(path), 'rb') as yf:
                cls.yc = yaml.safe_load(yf)
            cls._instance = super().__new__(cls)
        return cls._instance

def _cursor():
    db = mysql.connector.connect(
        host="172.23.16.4",
        user="hone_dev",
        passwd="hone_dev2020",
        database="htms_op_business"
    )
    return db.cursor()


def sql(sql):
    _cursor().execute(sql)


if __name__ == "__main__":
    print(Yml(_conffile).parametertable)
    print(Yml(sql_file_teardown).parametertable)
    sql(Yml(sql_file_teardown).parametertable.get("carrier"))
