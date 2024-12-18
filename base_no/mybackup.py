#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#基于python 的文件备份

import time,os


# 需要备份的目录
source = ['/Users/jiaxiaopeng/logs/']
# 保存备份的目录
backup_dir = '/Users/jiaxiaopeng/backup/'

#年月日
today_dir = backup_dir + time.strftime('%Y%m%d')
#时分秒
time_dir = time.strftime('%H%M%S')


target = backup_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'


zip_command = "zip -qr %s %s" %(target, ' '.join(source))

if not os.path.exists(today_dir):
    os.mkdir(today_dir)
# os.sep 通用文件分隔符
# zip -qr 压缩有的地址 需要压缩的文件路径
touch = today_dir + os.sep + time_dir + '.zip'
command_touch = "zip -qr " + touch +' '+ ' '.join(source)

print("touch:",touch)
print("command_touch:",command_touch)

# 
if os.system(command_touch)==0:
    print("Success backup Up")
else:
    print("Failed backup")



# if os.system(zip_command) == 0:
#     print("Successful backup")
# else :
#     print("Backup Failed")




