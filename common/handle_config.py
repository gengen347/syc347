"""
**************************
作者：李根
时间：2021/1/10  10:50
**************************
"""
from configparser import ConfigParser
from common.handle_path import CONFIG_PATH


class Config(ConfigParser):
    def __init__(self, file_dir, encoding='utf-8'):
        # 继承了别的类别忘了初始化
        super().__init__()
        self.file_dir = file_dir
        self.encoding = encoding
        self.read(file_dir, encoding=encoding)

    def config_write(self, config_block, config_name, write_value):
        self.set(config_block, config_name, write_value)
        self.write(fp=open(self.file_dir, 'w', encoding=self.encoding))


conf = Config(CONFIG_PATH)
if __name__ == '__main__':
    conf = Config(CONFIG_PATH)
    print(conf.get('report', 'filename'))
    conf.config_write('report', 'filename11', '77')
