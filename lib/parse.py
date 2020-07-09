#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass

import yaml

yaml.warnings({'YAMLLoadWarning': False})


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

    def content(self):
        return dict(self.yc)
