import unittest
from parameterized import parameterized
from api.api_login import ApiLogin
from tools.assert_common import assert_common
from tools.read_yaml import read_yaml
import api
from tools.get_log import GetLog

log = GetLog.get_logger()

class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        # 获取ApiLogin对象
        self.api_login = ApiLogin()

    # 登录测试接口方法
    @parameterized.expand(read_yaml("login.yaml"))
    def test_login(self, mobile, password):
        log.info("正在读取参数化数据：{}".format(read_yaml("login.yaml")))
        # 调用登录接口
        result = self.api_login.api_login(mobile, password)
        log.info("正在调用登录接口：{}".format(result))
        # print("登录结果为：", result.json())
        r = result.json()
        log.info("登录响应数据：{}".format(r))

        # 断言
        assert_common(self, result)

        # 提取 token
        token = r.get("data")
        log.info("正在提取token：{}".format(token))
        api.headers["Authorization"] = "Bearer " + token
        log.info("添加 token 值 到：{}".format(api.headers))
        print("追加token后的 headers为：", api.headers)

