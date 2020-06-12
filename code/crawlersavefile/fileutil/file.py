# encoding: utf-8
#!/usr/bin/python

import json
import csv

class File(object):

    def __init__(self,*args, **kwargs):
        pass

    # 保存列表list
    def writeCsvFileV(self,_fileUrl,_mode,dataline,_delimiter = ''):
        with open(_fileUrl, _mode, encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=_delimiter)
            ifRows = False
            for i in dataline:
                if (type(i).__name__ in ['list','tuple']):
                    ifRows = True
                    break
            if ifRows:
                writer.writerows(dataline)
            else:
                writer.writerow(dataline)

    # 保存dict
    def writeCsvFileKV(self,_fileUrl,_mode,_header,dataline,_delimiter = ''):
        with open(_fileUrl, _mode, encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, _header)
            writer.writeheader()
            writer.writerows(dataline)

    # 读取csv文件
    def readCsvFile(self,_fileUrl):
        with open(_fileUrl, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(row['name'], row['password'],row['status'])
                print(list(row.values()))

    # 保存json文件
    def saveJsonFile(self,_data,_fileUrl,_mode = 'w'):
        with open(_fileUrl, _mode, encoding='utf-8') as f:
            json.dump(_data, f)

    # 读json文件
    def readJsonFile(self,_fileUrl,_mode = 'r'):
        with open(_fileUrl, _mode) as f:
            return json.load(f)

    # 按行存文件
    def saveLine(self,_data,_fileUrl,_mode = 'a',_indentNo = 0):
        with open(_fileUrl,_mode, encoding='utf-8') as file:
            file.write(str(_data).strip()+'\n')#indent 缩进字符个数

    # 按行读文件
    def readLine(self,_fileUrl,_mode = 'r'):
        with open(_fileUrl, _mode) as f:
            line = f.readline()
            while line:
                print(line, end='')  # 在 Python 3中使用
                line = f.readline()


if '__main__' == __name__:
    header = ['name', 'password', 'status']
    dataV = [
        ['abc', '123456', 'PASS'],
        ['张五', '123#456', 'PASS'],
        ['张#abc123', '123456', 'PASS'],
        ['666', '123456', 'PASS'],
        ['a b', '123456', 'PASS']
    ]
    dataKV = [
        {'name': 'abc', 'password': '123456', 'status': 'PASS'},
        {'name': '张五', 'password': '123#456', 'status': 'PASS'},
        {'name': '张#abc123', 'password': '123456', 'status': 'PASS'},
        {'name': '666', 'password': '123456', 'status': 'PASS'},
        {'name': 'a b', 'password': '123456', 'status': 'PASS'}
    ]

    file = File();
    # file.writeCsvFileV('result.csv','w',header,_delimiter = ',');
    # file.writeCsvFileV('result.csv', 'a', dataV, _delimiter=',');
    # file.readCsvFileKV('result.csv','w',header,dataKV,_delimiter = ',')
    # file.readCsvFile('result.csv')
    _data = {1: 'Kelsey', 2: 'Simy', 3: 'ybb', 4: 'Eric'}
    # file.saveJsonFile(dataKV,'data.json','w')
    # json_file = file.readJsonFile('data.json')
    # print(type(json_file).__name__)
    # print(json_file)

    # file.saveLine(header,"data.txt",'a')
    # file.readLine("data.txt")

