# 加载套件
import unittest

from unittestreport import TestRunner

from common.handle_config import conf
from common.handle_path import TEST_PATH, REPORT_PATH

suite = unittest.defaultTestLoader.discover(TEST_PATH)

# 执行用例
runner = TestRunner(suite,
                    filename=conf.get('report',"filename"),
                    report_dir=REPORT_PATH,
                    title='前程贷测试报告',
                    tester='李根',
                    desc="李根执行测试生产的报告",
                    templates=1
                    )
runner.run()
