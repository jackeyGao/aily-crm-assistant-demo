import os

APP_ID = os.environ.get("APP_ID", None)
APP_SECRET = os.environ.get("APP_SECRET", None)
UAT = os.environ.get("USER_ACCESS_TOKEN", None)


init_usage = """
请首先设置 APP_ID / APP_SECRET 变量.

export APP_ID="your app id";
export APP_SECRET="your app secret"
"""

uat_usage = """
请首先设置 USER_ACCESS_TOKEN 变量.

export USER_ACCESS_TOKEN="your user access token"
"""

def validate_access_token():
    if not UAT:
        raise Exception(uat_usage)
    
    return UAT


def init():
    if not APP_ID:
        raise Exception(init_usage)

    if not APP_SECRET:
        raise Exception(init_usage)
    

init()