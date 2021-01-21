"""
**************************
作者：李根
时间：2021/1/11  11:28
**************************
"""
from common import  handle_excel
import unittest
from common import myddt
from common.handle_config import conf
from common.handle_data import replace_data
from common.handle_log import log
from common.handle_path import CASES_PATH
import requests

@myddt.ddt
class Login(unittest.TestCase):
    excel = handle_excel.Excle(CASES_PATH, 'login')
    case_data = excel.read_data()
    @myddt.data(*case_data)
    def test_02_login(self,item):
        url = conf.get('env','base_url')+item['url']
        headers =eval(conf.get('env','headers'))
        method= item['method']
        expected = eval(item['expected'])
        data = item['data']
        params = eval(replace_data(data, Login))
        respons =requests.request(url=url,method=method,json=params,headers=headers)
        print(respons.text)
        print(expected)
        res = respons.json()
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
        except AssertionError as e:
            log.error("用例{}失败".format(item['title']))
            log.exception(e)
            raise e
        else:
            log.error("用例{}成功".format(item['title']))

