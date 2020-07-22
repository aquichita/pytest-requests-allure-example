'''
@Author: your name
@Date: 2020-07-15 11:07:05
@LastEditTime: 2020-07-21 11:20:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\lib\parse.py
'''
from dataclasses import dataclass
from pathlib import Path
import sys

import yaml
import os

yaml.warnings({'YAMLLoadWarning': False})
_conffile = Path(".").resolve() / Path("env.yaml")


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

    def parametertable(self):
        return dict(self.yc)


if _conffile.exists() and str(_conffile).endswith(".yaml"):
    conf = Yml(_conffile).parametertable()
    print(conf)
    os.environ.update(conf)
else:
    raise FileNotFoundError(_conffile)


gofers = os.environ


def setattr(name, value):
    gofers.update(dict(name=value))
    os.environ.update(gofers)


def getattr(name):
    return os.environ.get("gofers").get(name)


def gen_allure_rep(allure, allure_dir, allure_report):
    if allure_dir:
        try:
            print('\n')
            os.system(f'{allure} generate -c {allure_dir} -o {allure_report}')
            if sys != 'Linux':
                os.system(f'{allure} open {allure_report}')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    print(Yml(_conffile).parametertable())
