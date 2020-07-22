import os
import json
import logging
from collections import OrderedDict
from pathlib import Path

import allure
import requests
import urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

LOGFILE = Path(".").resolve() / Path("gofers.log")
CONFIG = os.environ.get("gofers")

logging.basicConfig(
    filename=LOGFILE,
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

    def http(self, method, url, **kwargs):
        response = self.request(
            method, _url(url), timeout=HTTP_TIMEOUT, **kwargs)
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
        desc = json.dumps(
            info,
            sort_keys=True,
            indent=4
        ).encode('utf-8').decode('unicode_escape')
        logging.debug(desc)
        allure.attach(desc)
        return response


def _url(url: str):
    if not url.startswith("http"):
        if CONFIG["port"]:
            base_url = "".join(
                CONFIG["protocol"],
                "://",
                CONFIG["host"],
                ":",
                CONFIG["port"],
            )
        else:
            base_url = "".join(
                CONFIG["protocol"],
                "://",
                CONFIG["host"],
            )
        return base_url + url
    return url


http = TMS().http


def get(path, params=None, **kwargs):
    return http(method="get", url=path, params=params, **kwargs)


def options(path, **kwargs):
    return http(method="options", url=path, **kwargs)


def head(path, **kwargs):
    return http(method="head", url=path, **kwargs)


def post(path, data=None, json=None, **kwargs):
    return http(method="post", url=path, data=data, json=json, **kwargs)


def put(path, data=None, **kwargs):
    return http(method="put", url=path, data=data, **kwargs)


def patch(path, data=None, **kwargs):
    return http(method="patch", url=path, data=data, **kwargs)


def delete(path, **kwargs):
    return http(method="delete", url=path, **kwargs)
