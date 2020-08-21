'''
Author: your name
Date: 2020-08-12 17:50:52
LastEditTime: 2020-08-12 17:51:45
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pytest-requests-allure-example\steps\interfaces\config_management\service_config\track_profile.py
'''
import allure
from lib import client
from dataclasses import dataclass


@dataclass
class TrackProfile:
    session: dict

    @allure.step("新建规则组")
    def generate(self, ruleType, xid, name, isActive="Y", **kwargs):
        data = {
            "ruleType": ruleType,
            "xid": xid,
            "name": name,
            "isActive": isActive,
            "__dirty": bool(1)
        }
        return client.post(
            path=f"/htms/v1/{self.session.get('tenantId')}/htms/rule/group/generate",
            headers=self.session.get("Authorization"),
            json=data,
        )
