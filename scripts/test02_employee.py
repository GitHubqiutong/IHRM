# 导包
import unittest


# 继承
import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_employee = ApiEmployee()

    # 新增员工
    def test01_post(self, username="tom_gz_999", mobile="13815477732", workNumber="10311101"):
        r = self.api_employee.api_post_employee(username, mobile, workNumber)
        log.info("正在调用新增员工接口：{}".format(r))

        assert_common(self, r)
        # print("新增员工结果：", r.json())
        log.info("新增员工响应数据：{}".format(r.json()))

        # 提取 员工id。 将id 赋值给 __init__中user_id变量
        api.user_id = r.json().get("data").get("id")
        log.info("提取 员工 id：{}".format(api.user_id))
        print("员工user_id值为：", api.user_id)

    # 更新员工
    def test02_put(self):
        r = self.api_employee.api_put_employee()
        log.info("正在调用更新员工接口：{}".format(r))
        assert_common(self, r)
        # print("更新员工结果：", r.json())
        log.info("更新员工响应结果：{}".format(r.json()))

    # 查询员工
    def test03_get(self):
        r = self.api_employee.api_get_employee()
        log.info("正在调用查询员工接口：{}".format(r))
        assert_common(self, r)
        # print("查询员工结果：", r.json())
        log.info("查询员工响应结果：{}".format(r.json()))



    # 删除员工
    def test04_delete(self):
        r = self.api_employee.api_delete_employee()
        log.info("正在调用删除员工接口：{}".format(r))
        # print("删除结果为：", r.json())
        # assert_common(self, r)
        assert False
        log.info("删除员工响应结果：{}".format(r.json()))

