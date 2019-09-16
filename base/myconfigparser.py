import configparser
# 初始化
conf = configparser.ConfigParser()
# 读取配置文件
conf.read('config.ini', encoding='utf-8')

# 获得配置文件中的所有sections
print(conf.sections())
# section是区分大小写的，写成小写会被认为不存在
print(conf.has_section('mysql'))


# 获取section = Mysql 下的所有options，即keys
# option 不区分大小写，判断结果为True
if conf.has_section('Mysql'):
    print(conf.options('Mysql'))
    print(conf.items('Mysql'))