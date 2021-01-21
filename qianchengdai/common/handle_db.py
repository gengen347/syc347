"""
**************************
作者：李根
时间：2021/1/10  16:33
**************************
"""
import pymysql
from common.handle_config import conf


class DB:
    def __init__(self, host, port, user, password):
        # 第一步：连接数据库
        self.con = pymysql.connect(host=host,
                                   port=port,
                                   user=user,
                                   password=password,
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)
        # 第二步：创建一个游标对象
        self.cur = self.con.cursor()

    def find_all_data(self, sql):
        # 获取查询到的所有数据,注意要先同步数据再查
        self.con.commit()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res


db = DB(host=conf.get('mysql', 'host'),
        port=conf.getint('mysql', 'port'),
        user=conf.get('mysql', 'user'),
        password=conf.get('mysql', 'password'))
