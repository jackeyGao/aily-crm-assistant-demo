# aily-crm-assistant-demo
Aily CRM 销售助手 demo


# Quickstart

```
# 设置开放平台环境变量，用于env.py 读取配置
$ export APP_ID="cli_a62b77a2xxxxxxxx"
$ export APP_SECRET="ypaasceiyt1j8xxxxxxxxxxxxx"

# 获取access_token.py
$ python get_access_token.py 
请访问地址: https://open.feishu.cn/open-apis/authen/v1/index?app_id=cli_a62b77axxxxxxxxxd&redirect_uri=https://ae.feishu.cn/ai/api/v1/adminops/authorize/larkOpenApi/callback&scope=aily:record:write
访问后输入地址栏URL的code参数的值, 注意: code的值是一串小写的字母和英文组合.
请输入code值: 002k6eadc6a74c0cbb760c5a3b57e293 # 这里输入访问上述URL获取到的code值。

获取UAT成功！
请复制下方您的User Access Token
u-camdkF9OF27GgLXjOBiqxxxxxxxxxxxxxxxxxxxxxxx

执行其他脚本时, 请先设置user access token环境变量.
通过以下命令创建:
export USER_ACCESS_TOKEN="u-camdkF9OF27GgLXjOBiqxxxxxxxxxxxxxxxxxxxxxxx";

注意: 请妥善保存 USER_ACCESS_TOKEN , 千万不要泄漏.

# 写入uat环境变量，用于下方写入操作鉴权.
$ export USER_ACCESS_TOKEN="u-camdkF9OF27GgLXjOBiqxxxxxxxxxxxxxxxxxxxxxxx";

# 执行批量写入操作
$ python data_write.py
code:  0
items:  [{'_id': '1805375391146091', 'success': True}]
msg:  

#当items存在记录且和输入个数吻合，表示创建成功。
```