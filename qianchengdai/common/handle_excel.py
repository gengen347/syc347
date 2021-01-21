import openpyxl
from common.handle_path import CASES_PATH


class Excle:
    def __init__(self, file_name_path, sheet_name):
        self.file_name_path = file_name_path
        self.sheet_name = sheet_name

    def open(self):
        # 第一步：将excel文件加载到一个工作簿对象中
        self.wb = openpyxl.load_workbook(self.file_name_path)
        # 第二步：选择文件中的表单
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        self.open()
        res = list(self.sh.rows)
        title = [i.value for i in res[0]]
        cases_data = []
        for i in res[1:]:
            data = [j.value for j in i]
            dic = dict(zip(title, data))
            cases_data.append(dic)
        return cases_data

    def write_data(self, row, column, value):
        self.open()
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.file_name_path)


if __name__ == '__main__':
    data = Excle(CASES_PATH, 'register')
    datas = data.read_data()
    print(datas)
    data = Excle(CASES_PATH, 'Sheet2')
    data.write_data(row=1,column=1, value='gegeg')
