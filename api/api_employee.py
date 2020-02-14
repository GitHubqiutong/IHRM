import requests
import api
from tools.get_log import GetLog

log = GetLog.get_logger()

class ApiEmployee:
    # 初始化
    def __init__(self):
        # 新增 url
        self.api_post = api.api_host + "/api/sys/user"
        log.info("正在初始化新增 url：{}".format(self.api_post))

        # 修改、新增、删除 url
        self.api_employee_url = api.api_host + "/api/sys/user/{}"
        log.info("正在初始化修改、新增、删除 url：{}".format(self.api_employee_url))

    # 新增员工--》返回数据
    def api_post_employee(self, username, mobile, workNumber):
        data = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber
        }
        return requests.post(url=self.api_post, json=data, headers=api.headers)

    # 修改员工--》返回数据
    def api_put_employee(self):
        data = {"username": "tom-new"}
        return requests.put(url=self.api_employee_url.format(api.user_id), json=data, headers=api.headers)

    # 删除员工--》返回数据
    def api_delete_employee(self):
        return requests.delete(url=self.api_employee_url.format(api.user_id), headers=api.headers)

    # 查询员工--》返回数据
    def api_get_employee(self):
        return requests.get(url=self.api_employee_url.format(api.user_id), headers=api.headers)
