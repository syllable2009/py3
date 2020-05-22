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
                if (type(i).__name__ == 'list'):
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

    # todo 保存json文件
    def saveJsonFile(self):
        pass

    def saveLine(self,dataline,_saveMethod,_indentNo):
        with open(self._fileUrl,_saveMethod, encoding='utf-8') as file:
            file.writerow(dataline+'\n')#indent 缩进字符个数

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
    file.readCsvFile('result.csv')