'''
Author: your name
Date: 2020-08-12 18:00:56
LastEditTime: 2020-08-12 18:06:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pytest-requests-allure-example\steps\interfaces\base_data\service_dict\order_type.py
'''
import allure
from lib import client
from dataclasses import dataclass


@dataclass
class OrderType:
    session: dict

    @allure.step("新建订单类型")
    def submit(self, xid, name, isActive="Y", **kwargs):
        data = [
            {
                "xid": xid,
                "name": name,
                "isActive": isActive,
                "__id": 1587,
                "_status": "create",
                "tenantId": self.session.get("tenantId")
            }
        ]
        return client.post(
            path=f"/htms/v1/{self.session.get('tenantId')}/ordertype/submit",
            headers=self.session.get("Authorization"),
            json=data,
        )
