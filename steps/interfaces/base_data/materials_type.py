'''
@Author: Aquichita
@Date: 2020-07-15 15:38:51
@LastEditors: Please set LastEditors
@LastEditTime: 2020-07-15 15:57:31
'''
import allure
from lib import request
from dataclasses import dataclass


@dataclass
class MaterialsType:
    tenantId: str = getattr("tenantId")
    headers: dict = dict(
        Authorization=getattr("Authorization")
    )

    @allure.step("新建物料大类")
    def submit(self, xid, name, **kwargs):
        data = [
            {
                "xid": xid,
                "name": name,
                "isActive": "Y",
                "__id": None,
                "_status": "create",
                "tenantId": self.tenantId
            }
        ]
        return request.post(
            path=f"/htms/v1/{self.tenantId}/basic/item/type/submit",
            headers=self.headers,
            json=data,
        )

    @allure.step("查询物料大类")
    def query(self, xid, name, is_active="Y", page=0, size=10):
        data = [
            {
                "xid": xid,
                "name": name,
                "isActive": is_active,
                "page": page,
                "size": size,
            }
        ]
        return request.get(
            path=f"/htms/v1/{self.tenantId}/basic/item/type/query",
            headers=self.headers,
            params=data,
        )
