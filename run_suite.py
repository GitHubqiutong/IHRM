# 导包
import unittest

# 组装测试套件
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts", pattern="test*.py")

# 获取报告存储文件流， 实例化调用run 执行测试套件
with open("./report/ihrm_report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)