from datetime import datetime
from aily.openapi.data import DataClient
from aily_crm.env import validate_access_token

uat = validate_access_token()

data = {
    'app_id': 'spring_49e962d9a3__c', # aily app_id，替换成你的aily app id
    "table_api_name": "object_record", # 数据表标识
    "primary_key": "_id", # 主键
    "records": [
        {
            "is_visit": True, # 布尔
            "record_type": "option_cus", # 文本
            "share": { "_id": 1804801500455971 }, # 关联类型 - 用户
            "owner": { "_id": 1804801500455971 }, # 关联关系（用户)， 用户ID替换成有权限的用户.
            "next_step": "进行现场培训",
            "short_progress": "AI 演示效果不错，但对使用还不理解。",
            "communication_record": "AI 演示",
            "communicator": "药亮销售部门",
            "follow_up_date": "2024-09-10 11:00:00",
            "opportunity": {"_id": 1805375554311339 },
            "customer": {"_id": 1805375474074684 },
        },
        {
            "is_visit": True, # 布尔
            "record_type": "option_cus", # 文本
            "share": { "_id": 1804801500455971 }, # 关联类型 - 用户
            "owner": { "_id": 1804801500455971 }, # 关联关系（用户)， 用户ID替换成有权限的用户.
            "next_step": "进行现场培训", # 文本
            "short_progress": "AI 演示效果不错，但对使用还不理解。",
            "communication_record": "AI 演示",
            "communicator": "宝桃销售部门",
            "follow_up_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # 日期
            "opportunity": {"_id": 1805375554308187 }, # 关联关系（单选)
            "customer": {"_id": 1805375474074636 },  # 关联关系（单选)
        }
    ],
    "table_type": "datatable", # 类型选择datatable
}


api = DataClient(uat)

response = api.write(data)
print('code: ', response.code)
print('items: ', response.items)
print('msg: ', response.msg)