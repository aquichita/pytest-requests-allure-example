'''
Author: your name
Date: 2020-08-17 15:27:48
LastEditTime: 2020-08-18 09:22:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pytest-requests-allure-example\steps\macros\order_center\create_order.py
'''
import allure
from lib import client, gofers
from dataclasses import dataclass


@dataclass
class Order:
    session: dict

    @allure.step("订单新建")
    def tms_om_save(self,
                    businessUnitName,
                    businessNumber,
                    orderTypeGid,
                    planStartShippingDate,
                    planDeliveryDate,
                    transportModeGid,
                    itemAttribute,
                    sourceLocationGid,
                    sourceLocationXid,
                    sourceLocationName,
                    sourceAddress,
                    sourceContacts,
                    destLocationGid,
                    destLocationXid,
                    destLocationName,
                    destAddress,
                    destContacts,
                    **kwargs):
        data = {
            "paramIn": {
                "businessUnitName": businessUnitName,
                "businessNumber": businessNumber,
                "planStartShippingDate": planStartShippingDate,
                "planDeliveryDate": planDeliveryDate,
                "itemAttribute": itemAttribute,
                "remark": "订单备注-尽快发货",
                "sourceLocationGid": sourceLocationGid,
                "sourceLocationXid": sourceLocationXid,
                "sourceLocationName": sourceLocationName,
                "sourceAddress": sourceAddress,
                "sourceContacts": sourceContacts,
                "sourceCompanyPhone": "029-8835666",
                "sourcePhoneNumber": "15687208899",
                "sourceEmail": "xxx@hand-china.com",
                "sourceRemark": "发货备注-尽快发货",
                "destLocationGid": destLocationGid,
                "destLocationXid": destLocationXid,
                "destLocationName": destLocationName,
                "destAddress": destAddress,
                "destContacts": destContacts,
                "destCompanyPhone": "0913-8835888",
                "destPhoneNumber": "15686209900",
                "destEmail": "xxx@hand-china.com",
                "destRemark": "收货备注-尽快发货",
                "orderTypeGid": orderTypeGid,
                "customerGid": 25077,
                "transportModeGid": transportModeGid,
                "sourceProvince": "陕西省",
                "sourceCity": "西安市",
                "sourceDistrict": "雁塔区",
                "sourceAreaGid": 10053,
                "destProvince": "北京市",
                "destCity": "北京市",
                "destDistrict": "朝阳区",
                "destAreaGid": 10058,
                "__dirty": bool("true"),
                "movementLine": [
                    {
                        "itemCount": 80,
                        "weight": 4,
                        "volume": 20,
                        "itemValue": 90,
                        "itemXid": "TEST-MOVEMENT-001",
                        "itemName": "TEST-MOVEMENT-001",
                        "unitOfMeasurement": "件",
                        "cartonNumber": "1",
                        "itemGid": 374,
                        "unitVolume": 0.25,
                        "unitWeight": 0.05,
                        "__dirty": bool("true"),
                        "tenantId": 11
                    },
                    {
                        "itemCount": 35,
                        "weight": 35,
                        "volume": 35,
                        "itemValue": 120,
                        "itemXid": "TEST-MOVEMENT-002",
                        "itemName": "TEST-MOVEMENT-002",
                        "unitOfMeasurement": "件",
                        "cartonNumber": "2",
                        "itemGid": 375,
                        "unitVolume": 1,
                        "unitWeight": 1,
                        "__dirty": bool("true"),
                        "tenantId": 11
                    }
                ],
                "businessUnitGid": 10164
            },
            "macroCode": "TMS_OM_SAVE"
        }
        return client.post(
            path=f"/htms/v1/{self.session.get('tenantId')}/tp/macro/excuteMacro",
            headers=self.session.get("Authorization"),
            json=data,
        )

    def tms_om_delete(businessNumber):
        gofers.mysql.exec_sql(
            f"DELETE FROM `htms_op_business`.`tbl_order_movement` WHERE `NAME`=={businessNumber};")
