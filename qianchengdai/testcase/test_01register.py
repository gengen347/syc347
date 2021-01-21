import unittest
import requests
from common import myddt
from common.handle_db import db
from common.handle_excel import Excle
from common.handle_path import CASES_PATH
from common.handle_config import conf
from common.handle_data import replace_data
from tools.phone import random_phone
from common.handle_log import log

@myddt.ddt
class Register(unittest.TestCase):
    excel = Excle(CASES_PATH, 'register')
    case_data = excel.read_data()

    @myddt.data(*case_data)
    def test_01_register(self, item):
        # 第一步：准备数据
        url = conf.get('env', 'base_url') + item['url']
        method = item['method']
        headers = eval(conf.get("env", "headers"))
        Register.phone = random_phone()

        params = eval(replace_data(item['data'], Register))
        expected = eval(item['expected'])
        # 第二步：发送请求
        response = requests.request(url=url, method=method, json=params, headers=headers)
        res = response.json()
        print('预期结果', expected)
        print('实际结果', response.text)
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            check_sql = item['check_sql']
            if check_sql:
                res = db.find_all_data(check_sql.format(params["mobile_phone"]))
                self.assertTrue(res)
        except AssertionError as e:
            log.error("用例{}失败".format(item['title']))
            log.exception(e)
            raise e
        else:
            log.error("用例{}成功".format(item['title']))


if __name__ == '__main__':
    unittest.main()
