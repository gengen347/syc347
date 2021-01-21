import random

from common.handle_config import conf
from common.handle_db import db

def random_phone():
    while True:
        phone = str(random.randint(13500000000,13599999999))
        sql ="SELECT * FROM futureloan.member WHERE mobile_phone={}".format(phone)
        res=db.find_all_data(sql)
        if not res:
            return phone


if __name__ == '__main__':
    print(random_phone())
