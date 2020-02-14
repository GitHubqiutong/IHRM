import api
import requests
from tools.get_log import GetLog

log = GetLog.get_logger()

class ApiLogin:
    # 初始化
    def __init__(self):
        # 组装 登录url
        self.login_url = api.api_host + "/api/sys/login"
        log.info("初始化登录 url：{}".format(self.login_url))

    # 登录接口封装
    def api_login(self, mobile, password):
        # 定义测试数据
        data = {"mobile": mobile, "password": password}
        # 调用post方法
        return requests.post(url=self.login_url, json=data, headers=api.headers)