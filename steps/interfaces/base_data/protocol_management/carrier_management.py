'''
@Author: your name
@Date: 2020-07-24 11:24:47
LastEditTime: 2020-08-12 16:25:00
LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pytest-requests-allure-example\steps\interfaces\base_data\carrier_management.py
'''
import allure
from lib import client, parameter
from dataclasses import dataclass


@dataclass
class CarrierManagement:
    session: dict

    @allure.step("新建承运商")
    def submit(self, xid, name, isActive="Y", autoAcceptTender="N", **kwargs):
        data = [
            {
                "isActive": isActive,
                "autoAcceptTender": autoAcceptTender,
                "xid": xid,
                "name": name,
                "servprovNameAbbr": parameter.zh(),
                "contact": parameter.zh(),
                "email": parameter.email(),
                "phone": parameter.phone(),
                "businessStartDate": parameter.dater().get("start"),
                "businessEndDate": parameter.dater().get("end"),
                "legalPerson": parameter.zh(),
                "externalInterfaceCode": xid,
                "licenceStartDate": parameter.dater().get("start"),
                "licenceEndDate": parameter.dater().get("end"),
                "registeredCapital": parameter.num(),
                "transportStartDate": parameter.dater().get("start"),
                "transportEndDate": parameter.dater().get("end"),
                "transportGrade": "1",
                "remark": parameter.zh(length=64),
                "__dirty": bool(1),
                "tenantId": self.session.get("tenantId")
            }
        ]
        return client.put(
            path=f"/htms/v1/{self.session.get('tenantId')}/basic/servprov/submit",
            headers=self.session.get("Authorization"),
            json=data,
        )

    @allure.step("查询承运商")
    def query(self, xid=None, name=None, phone=None, is_active="Y", page=0, size=10):
        data = [
            {
                "xid": xid,
                "name": name,
                "phone": phone,
                "isActive": is_active,
                "page": page,
                "size": size,
            }
        ]
        return client.get(
            path=f"/htms/v1/{self.session.get('tenantId')}/basic/servprov/query",
            headers=self.headers,
            params=data,
        )
