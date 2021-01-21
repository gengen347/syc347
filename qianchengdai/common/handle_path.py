import os

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_PATH = os.path.join(PATH, 'data/cases.xlsx')
CONFIG_PATH = os.path.join(PATH, 'conf/config.ini')
TEST_PATH = os.path.join(PATH, 'testcase')
REPORT_PATH = os.path.join(PATH, 'reports')
LOGS_PATH = os.path.join(PATH, 'logs')