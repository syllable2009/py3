from os import path
import os


class PathUtils(object):

    '''
    返回一个目录和文件组合的地址
    目录不存在会新建
    文件名重复会加下划线数字区分
    '''
    @staticmethod
    def getPath(dir,file_name):
        file_path = path.join(dir, file_name)
        dir,file_name = path.split(file_path)
        if not path.exists(dir):
            os.makedirs(dir)
        else:
            i = 1;
            name, ext = path.splitext(file_name)
            while(path.exists(file_path)):
                file_name = name + '_' + str(i) + ext;
                i = i + 1
                file_path = path.join(dir, file_name)
        return path.join(dir, file_name)


if __name__ == '__main__':
    # PathUtils.getPath(path.abspath('.'),'abc.txt');
    # name, ext = path.splitext('/abc/a.txt')
    # print("{},{}".format( name, ext))
    # path,file_name = path.split('123/456/789.py')
    # print(path,file_name)
    pass
