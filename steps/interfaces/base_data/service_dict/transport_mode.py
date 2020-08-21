'''
Author: your name
Date: 2020-08-12 17:50:52
LastEditTime: 2020-08-12 17:59:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pytest-requests-allure-example\steps\interfaces\config_management\service_config\track_profile.py
'''
import allure
from lib import client
from dataclasses import dataclass


@dataclass
class TransportMode:
    session: dict

    @allure.step("新建运输模式")
    def submit(self, xid, name, transportModeType, **kwargs):
        data = [
            {
                "xid": xid,
                "name": name,
                "transportModeType": transportModeType,
                "isActive": "Y",
                "isMatchModels": "Y",
                "__dirty": bool(1),
                "tenantId": self.session.get('tenantId')
            }
        ]
        return client.post(
            path=f"/htms/v1/{self.session.get('tenantId')}/transport/mode/submit",
            headers=self.session.get("Authorization"),
            json=data,
        )
