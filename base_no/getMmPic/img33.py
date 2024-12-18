# import pprint
import sys
import time
import datetime
# sys.path.append("/Users/jiaxiaopeng/git/py3/base/")
# pprint.pprint(sys.path)
from base_no import mydbutils1
import urllib.request


def insertDb(url=None, date=None, pic_id=None, create_time=None):
    pool = mydbutils1.get_db_pool(False)
    conn = pool.connection()
    cursor = conn.cursor()
    sql = "insert into 33img(url,date,pic_id,create_time) " \
          "values(%s,%s,%s,%s)"
    var = (url, date, pic_id, create_time)

    execute = cursor.execute(sql, var)
    conn.commit()
    # print("插入id：",execute.lastrowid)
    conn.close()


# insertDb("http://www.baidu.com",'2017-3-18',2345667,time.localtime())

def get_resource(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    res = urllib.request.Request(url=url, headers=headers)
    return urllib.request.urlopen(res)


# url = 'http://33img.com/upload/image/20190317/31710304837.jpg'
# resource = get_resource(url)
# print(resource.getcode())


def judge_pic_exist(url):
    try:
        res = urllib.request.urlopen(url=url)
    except BaseException:
        return False
    else:
        return True


def find_pic_id(second_url):
    base_url = 'http://33img.com/upload/image/'
    # second_url = '20190317/31710304837.jpg'
    return urllib.request.urljoin(base_url, second_url + '.jpg')

# 折半查找
def den_increase(date):
    id = 31810234161
    pic_id = str(id).zfill(11)
    date_pic_id = date + '/' + pic_id
    pic_url = find_pic_id(date_pic_id)
    print(pic_url)
    boolean = judge_pic_exist(pic_url)
    while boolean == False:
        pic_id =- 1000;
        pic_id = str(pic_id).zfill(11)
        date_pic_id = date + '/' + pic_id
        boolean = judge_pic_exist(date_pic_id)

    return pic_id;
    # max = 1233
    # min = 223
    # return min,max



if __name__ == '__main__':
    # print('url:', find_pic_id())
    # today_date = time.strftime("%Y%m%d", time.localtime())
    today = datetime.datetime.now()
    day = -1
    while day < 10:
        day += 1
        offset = datetime.timedelta(days=-day)
        re_date = (today + offset).strftime('%Y%m%d')
        increase = den_increase(re_date)
        print(re_date,increase)