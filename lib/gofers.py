import base64
import logging
import os
import platform
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

import mysql.connector
import yaml
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcsl_v1_5
from Crypto.PublicKey import RSA
from pyfiglet import Figlet

PROJECT_ROOT = Path(".").resolve()
REP_DIR = PROJECT_ROOT / Path("report")
RES_DIR = REP_DIR / Path("allure-results")
ALL_REP = REP_DIR / Path("allure-report")
EXTRAS_DIR = PROJECT_ROOT / Path("extras")

# logger = logging.getLogger()
# log_file = Path.joinpath(PROJECT_ROOT, Path("Gofers.log"))

# if Path.exists(log_file):
#     os.remove(log_file)

# project_desc = """

# Realization of HTTP API automated testing wheels by pytest+requests+allure.

# """
# with open(log_file, mode='w', encoding='utf-8') as f:
#     fl = Figlet(width=180)
#     log_file.write_text(project_desc + "\n\n" +
#                         fl.renderText(PROJECT_ROOT.name) +
#                         "\n\n"
#                         )
#     f.close()

# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter(
#     '%(asctime)s %(filename)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')

# ch = logging.StreamHandler()
# ch.setFormatter(formatter)

# fh = logging.FileHandler(log_file, encoding='utf-8')
# fh.setFormatter(formatter)


# def handlerHelper(func):
#     def wrapper(*args, **kwargs):
#         logger.addHandler(ch)
#         logger.addHandler(fh)
#         func(*args, **kwargs)
#         logger.removeFilter(ch)
#         logger.removeFilter(fh)

#     return wrapper


# @handlerHelper
# def debug(msg):
#     logger.debug(msg)


# @handlerHelper
# def info(log_meg):
#     logger.info(log_meg)


# @handlerHelper
# def warning(log_meg):
#     logger.warning(log_meg)


# @handlerHelper
# def error(log_meg):
#     logger.error(log_meg)


# @handlerHelper
# def critical(log_meg):
#     logger.error(log_meg)


def _allure():
    version = getconfattr("allure_version")
    if platform.system() != "Windows":
        name = "allure"
    else:
        name = "allure.bat"
    return EXTRAS_DIR.joinpath(
        Path(f"allure-{version}"),
        Path("bin"),
        Path(name)
    )


shutil.rmtree(REP_DIR, True)


def gen_allure_rep(allure_dir):
    if allure_dir:
        try:
            print('\n')
            gen_cmd = f'{_allure()} generate -c {RES_DIR} -o {ALL_REP} --clean'
            os.system(gen_cmd)
            if sys != 'Linux':
                open_rep_cmd = f'{_allure()} open {ALL_REP}'
                os.system(open_rep_cmd)
        except Exception as e:
            print(e)


def gen_html_rep(parameter_list):
    ...


yaml.warnings({'YAMLLoadWarning': False})
_conffile = Path(".").resolve() / Path("env.yaml")
SQL_DIR = Path(".").resolve().joinpath(
    Path("extras"),
    Path("data"),
)


@dataclass
class Yml:
    path: str = _conffile

    def __getitem__(self, key: str = None):
        return str(self.yc[key]) if key in self.yc else None

    @property
    def parametertable(self):
        if Path.exists(self.path):
            with open(str(self.path), 'rb') as yf:
                self.yc = yaml.safe_load(yf)
            return dict(self.yc)


# update environment by configfile.
os.environ.update(Yml().parametertable)


def getconfattr(name: str) -> str:
    return os.environ.get(name, None)


@dataclass
class mysql:
    db_conf = Yml(_conffile).parametertable
    db = mysql.connector.connect(
        host=db_conf['db_host'],
        user=db_conf['db_user'],
        passwd=db_conf['db_pwd'],
        database=db_conf['db_name'],
    )

    @classmethod
    def exec_sql(cls, sql):
        cls.db.cursor().execute(sql)
        cls.db.commit()

    @classmethod
    def exec_sqlyml(cls, sqlyml, *, msg=None):
        # info(f"{msg} start.") if msg else None
        if Path.exists(sqlyml):
            sqlyml = Yml(sqlyml).parametertable
        for name, value in sqlyml.items():
            # info(f"EXECUTE SQL NAME: {name}, VALUE: {value}")
            cls.exec_sql(sql=value)
        cls.db.cursor().close()
        cls.db.close()
        # info(f"{msg} end.") if msg else None


def rsa(rsa_str):
    public_key = '''-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJL0JkqsUoK6kt3JyogsgqNp9VDGDp+t3ZAGMbVoMPdHNT2nfiIVh9ZMNHF7g2XiAa8O8AQWyh2PjMR0NiUSVQMCAwEAAQ==
-----END PUBLIC KEY-----
'''
    rsa_str = bytes(rsa_str, encoding="utf8")
    rsa_key = RSA.importKey(public_key)
    cipher = Cipher_pkcsl_v1_5.new(rsa_key)
    return base64.b64encode(cipher.encrypt(rsa_str))
