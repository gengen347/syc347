"""
**************************
作者：李根
时间：2021/1/10  10:22
**************************
"""
import re

from common.handle_config import conf


def replace_data(data, cls):
    # 替换用例参数
    while re.search("#(.+?)#", data):
        item = re.search("#(.+?)#", data)
        # 需要替换的数据
        rep_data = item.group()
        # 要替换的属性
        attr = item.group(1)
        try:
            value = conf.get('test_data', attr)
        except:
            value = getattr(cls, attr)
        data = data.replace(rep_data, str(value))
    return data


if __name__ == '__main__':
    class EnvDate:
        member_id = 123
        user = "musen"
        loan = 31


    data = '{"member_id":"#member_id#","pwd":"#pwd#","user":"#user#","loan_id":"#loan#"}'

    res = replace_data(data, EnvDate)
    print(res)
