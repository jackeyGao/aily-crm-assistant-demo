from aily.openapi.data import DataClient
from aily_crm.env import validate_access_token

uat = validate_access_token()

data = {
    'app_id': 'spring_49e962d9a3__c', # aily app_id，替换成你的aily app id
    "table_api_name": "object_requirement", # 数据表标识
    "primary_key": "_id", # 主键
    "records": [
        {
            "requirements": "药亮集团AI演示,演示飞书MyAI能力,Aily能力,多维表格AI魔方插件.", # 文本
            "title": "药亮集团AI演示", # 文本
            "resolve_time": "2024-09-10 11:00:00", # 日期类型
            "lookup_owner": [{ "_id": "1804801500455971" }], # 关联关系（多选)， 用户ID替换成有权限的用户.
        }
    ],
    "table_type": "datatable", # 类型选择datatable
}


api = DataClient(uat)

response = api.write(data)
print('code: ', response.code)
print('items: ', response.items)
print('msg: ', response.msg)