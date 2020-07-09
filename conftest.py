#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pytest import fixture


def pytest_sessionstart():
    pass


@fixture(scope="session", autouse=True)
def tms():
    pass


def pytest_sessionfinish(session):
    pass
