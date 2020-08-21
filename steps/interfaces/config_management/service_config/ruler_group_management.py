'''
Author: your name
Date: 2020-08-12 17:41:01
LastEditTime: 2020-08-12 17:59:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pytest-requests-allure-example\steps\interfaces\config_management\service_config\ruler_group_management.py
'''
import allure
from lib import client
from dataclasses import dataclass


@dataclass
class RulerGroupManagement:
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
