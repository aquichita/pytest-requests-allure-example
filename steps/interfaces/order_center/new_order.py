#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure

from lib import request
from dataclasses import dataclass

from lib import parameters


@dataclass
class NewOrder:
    tenantId: str
    headers: dict

    @allure.step("订单新建")
    def submit(
        self,
        businessNumber,
        businessUnitName="TEST-华南区-001",
        itemAttribute="G",
        **kwargs
    ):
        '''
        @msg: 订单新建
        @param  businessNumber=外部订单号
        @return: response
        '''
        data = [
            {
                "businessUnitName": businessUnitName,
                "businessNumber": businessNumber,
                "planStartShippingDate": parameters.dater()["start"],
                "planDeliveryDate": parameters.dater()["end"],
                "itemAttribute": itemAttribute,
                "remark": "企业采购部门向供应商发出订货凭据\
                                        （包含成品、原材料、燃料、零部件、办公用品、服务等全部采购过程）。",
                "sourceLocationGid": 10333,
                "sourceLocationXid": 10333,
                "sourceLocationName": "TEST-西安-001",
                "sourceAddress": "陕西省 西安市 雁塔区 TEST-CUSTOMER-001",
                "sourceContacts": "TEST-CUSTOMER-001",
                "sourceCompanyPhone": "029-8835666",
                "sourcePhoneNumber": "15686208899",
                "sourceEmail": "test@outlook.com",
                "destLocationGid": 10334,
                "destLocationXid": 10334,
                "destLocationName": "TEST-北京-002",
                "destAddress": "北京市 北京市 朝阳区 TEST-LOCATION-002",
                "destContacts": "TEST-CUSTOMER-001",
                "destCompanyPhone": "029-8835123",
                "destPhoneNumber": "15686209900",
                "destEmail": "test@outlook.com",
                "orderTypeGid": 10063,
                "customerGid": 25075,
                "transportModeGid": 166,
                "sourceProvince": "陕西省",
                "sourceCity": "西安市",
                "sourceDistrict": "雁塔区",
                "sourceAreaGid": 10053,
                "destProvince": "北京市",
                "destCity": "北京市",
                "destDistrict": "朝阳区",
                "destAreaGid": 10058,
                "__dirty": "true",
                "movementLine": [
                    {
                        "itemCount": 1,
                        "weight": 0.05,
                        "volume": 0.25,
                        "itemValue": 196.8,
                        "itemXid": "TEST-MOVEMENT-001",
                        "itemName": "TEST-MOVEMENT-001",
                        "unitOfMeasurement": "件",
                        "cartonNumber": "23",
                        "itemGid": 374,
                        "unitVolume": 0.25,
                        "unitWeight": 0.05,
                        "__dirty": "true",
                        "tenantId": self.tenantId
                    },
                    {
                        "itemCount": 1,
                        "weight": 1,
                        "volume": 1,
                        "itemValue": 1759,
                        "itemXid": "TEST-MOVEMENT-002",
                        "itemName": "TEST-MOVEMENT-002",
                        "unitOfMeasurement": "件",
                        "cartonNumber": "17",
                        "itemGid": 375,
                        "unitVolume": 1,
                        "unitWeight": 1,
                        "__dirty": "true",
                        "tenantId": self.tenantId
                    }
                ],
                "businessUnitGid": 10161,
                "tenantId": self.tenantId
            }
        ]
        return request.post(
            path=f"/htms/v1/{self.tenantId}/htms/movement/saveNewOrder",
            headers=self.headers,
            json=data,
        )
