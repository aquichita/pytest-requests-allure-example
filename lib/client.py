#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from collections import OrderedDict
from pathlib import Path

import allure
import requests
import urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

_logfile = Path(".").resolve() / Path("gofers.out")

logging.basicConfig(
    filename=_logfile,
    level=logging.DEBUG
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HTTP_TIMEOUT = 60
RETRY_TIMES = 3


class TMS(requests.Session):
    def __init__(self):
        super(TMS, self).__init__()
        retry = Retry(connect=RETRY_TIMES, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.mount('http://', adapter)
        self.mount('https://', adapter)

    def session(self, method, url, **kwargs):
        response = self.request(
            method, url, timeout=HTTP_TIMEOUT, **kwargs)
        info = OrderedDict(
            URL=response.request.url,
            Method=response.request.method,
            Body=None,
            ResponseStatusCode=str(response.status_code),
            ResponseBody=response.text,
        )

        if response.request.body:
            if isinstance(response.request.body, bytes):
                info.update(Body=response.request.body.decode(
                    'unicode-escape', errors="ignore"),)
            else:
                info.update(Body=response.request.body,)
        desc = json.dumps(info, sort_keys=True, indent=4)\
            .encode('utf-8')\
            .decode('unicode_escape')
        logging.debug(desc)
        allure.attach(desc)
        return response
