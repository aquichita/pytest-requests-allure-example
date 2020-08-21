'''
Author: your name
Date: 2020-08-12 18:08:13
LastEditTime: 2020-08-12 18:19:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pytest-requests-allure-example\steps\interfaces\base_data\protocol_management\customer_management.py
'''
import allure
from lib import client, parameter
from dataclasses import dataclass


@dataclass
class CustomerManagement:
    session: dict

    @allure.step("新建客户")
    def submit(self, xid, name, contact, phone, **kwargs):
        data = [
            {
                "isActive": "Y",
                "xid": xid,
                "name": name,
                "customerNameAbbr": parameter.en(),
                "contact": contact,
                "phone": phone,
                "email": parameter.email(),
                "businessStartDate": parameter.dater().get("start"),
                "businessEndDate": parameter.dater().get("end"),
                "scopeBusiness": parameter.zh(),
                "remark": parameter.zh(),
                "__dirty": bool(1),
                "tenantId": self.session.get('tenantId')
            }
        ]
        return client.post(
            path=f"/htms/v1/{self.session.get('tenantId')}/basic/customer/submit",
            headers=self.session.get("Authorization"),
            json=data,
        )
