
from requests import get
from json import loads
from filetype import guess
from contextlib import closing

# 显示一段文字，将输入结果返回
def showInput(showText):
    return input(showText)

def downloadFile(file_full_name,now_photo_count,all_photo_count):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    # 开始下载图片
    with closing(get(file_url, headers=headers, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 文件总大小
        data_count = 0 # 当前已传输的大小
        with open(file_full_name, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                done_block = int((data_count / content_size) * 50) #分成50份显示
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r %s：[%s%s] %d%% %d/%d" % (file_full_name, done_block * '█', ' ' * (50 - 1 - done_block), now_jd, now_photo_count, all_photo_count), end=" ")

if __name__ == '__main__':
    # inputInt = '请输出字符串：\n'
    # text = showInput(inputInt)
    # while(int(text) > 0 or int(text) < 0):
    #     text = showInput('输入有误,'+inputInt)
    if(2>1):
        url = 'https://service.paper.meiyuan.in/api/v2/columns/flow/5c81087e6aee28c541eefc26?page=1&per_page=1'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    respond = get(url, headers=headers)

    photo_data = loads(respond.content)
    for photo in photo_data:
        file_url = photo['urls']['raw']
        print(file_url)
        file_name_only = file_url.split('/')
        print(file_name_only)
        file_name_only = file_name_only[len(file_name_only) - 1]
        print(file_name_only)
        # 下载完图片后获取图片扩展名，并为其增加扩展名,只能识别本地文件
        file_type = guess('/Users/jiaxiaopeng/111.jpg')
        print(file_type.__dict__)
        print(dir(file_type))
        # rename(file_full_name, file_full_name + '.' + file_type.extension)
        print("\n %s：[%s%s] %d%% %d/%d" % (
        './Users/jiaixaopneg/test', 30 * '█', ' ' * (50 - 1 - 30), 66, 2, 100),
              end=" ")
        print("\n %s：[%s%s] %d%% %d/%d" % (
            './Users/jiaixaopneg/test', 50 * '█', ' ' * (50 - 1 - 50), 66, 2, 100),
              end=" ")

