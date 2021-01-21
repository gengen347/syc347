"""
**************************
作者：李根
时间：2021/1/10  9:13
**************************
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from common.handle_path import LOGS_PATH


class Log:
    @staticmethod
    def create_logger():
        # 第一步：创建日志收集器
        # 定义一个日志收集器，名字叫“TC_log”
        my_log = logging.getLogger('TC_log')
        # 设置收集器收集日志等级
        my_log.setLevel('DEBUG')

        # 第二步：创建日志输出渠道
        # 创建一个输出到控制台的输出渠道，设置输出等级，添加到收集器中
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        my_log.addHandler(sh)
        # 创建一个输出到文件的渠道，设置输出等级，添加到收集器中
        # 参数说明：输出日志文件名、产生日志的单位（s、h、d）、
        # 产生日志的单位数量、最多保存文件的数量、编码格式（每7秒产生一个日志文件）
        fh = TimedRotatingFileHandler(filename=os.path.join(LOGS_PATH,'time.log'), when='s', interval=7, backupCount=3, encoding='utf-8')
        fh.setLevel('DEBUG')
        my_log.addHandler(fh)

        # 第三步：日志输出格式
        formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        mat = logging.Formatter(formats)
        # 与输出渠道关联上
        fh.setFormatter(mat)
        sh.setFormatter(mat)

        return my_log


log = Log.create_logger()

if __name__ == '__main__':
    log = Log.create_logger()
    log.warning('aaa')
