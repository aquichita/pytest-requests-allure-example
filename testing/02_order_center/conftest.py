import pytest
from lib import parameter


@pytest.fixture(scope="module")
def tms_om_save(tms):
    response = tms.order.tms_om_save(
        businessUnitName="TEST-华中区-001",
        businessNumber=parameter.en(),
        orderTypeGid=10063,
        planStartShippingDate=parameter.dater().get("start"),
        planDeliveryDate=parameter.dater().get("end"),
        transportModeGid=166,
        itemAttribute="G",
        sourceLocationGid=10338,
        sourceLocationXid=10338,
        sourceLocationName="TEST-雁塔区物流中心-001",
        sourceAddress="陕西省 西安市 雁塔区",
        sourceContacts="TEST-联系人",
        destLocationGid=10339,
        destLocationXid=10339,
        destLocationName="TEST-朝阳区物流中心-002",
        destAddress="北京市 北京市 朝阳区",
        destContacts="北京客户")
    return response
