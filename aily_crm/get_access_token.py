from aily.openapi import UserAccessTokenClient
from aily.openapi.data import DataClient

from aily_crm.env import APP_ID, APP_SECRET


client = UserAccessTokenClient(
    app_id=APP_ID,
    app_secret=APP_SECRET,
)

# 拼接认证URL
url = f"https://open.feishu.cn/open-apis/authen/v1/index?app_id={APP_ID}"
url += "&redirect_uri=https://ae.feishu.cn/ai/api/v1/adminops/authorize/larkOpenApi/callback"
url += "&scope=aily:record:write"

print(f"请访问地址: {url}")
print(f"访问后输入地址栏URL的code参数的值, 注意: code的值是一串小写的字母和英文组合.")
code = input("请输入code值: ")

client.init_with_code(code)
uat = client.get_user_access_token()

print(f"""
获取UAT成功！

请复制下方您的User Access Token
{uat}

执行其他脚本时, 请先设置user access token环境变量.
通过以下命令创建:
export USER_ACCESS_TOKEN="{uat}";

注意: 请妥善保存 USER_ACCESS_TOKEN , 千万不要泄漏.
""")