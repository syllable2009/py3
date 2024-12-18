from urllib.parse import urlparse
import os
import wget
import requests

# 应该使用包含，有额外编码或者文件名称
DOWNLOAD_CONTENT_TYPES = ['application/octet-stream', 'audio/mpeg', 'lrc-application/octet-stream']
PICTURE_CONTENT_TYPES = ['image/avif', 'application/pdf', 'image/jpeg', 'image/png', 'image/gif',
                         'image/bmp', 'image/svg+xml', 'image/webp', 'image/tiff']
DOWNLOAD_CONTENT_DISPOSITION = 'attachment'


# 从url中解析文件名称
def extract_filename(url: str) -> str:
    # 解析 URL
    parsed_url = urlparse(url)
    # 获取路径部分
    path = parsed_url.path
    # 提取文件名
    filename = os.path.basename(path)
    return filename


def if_contain(lst: list, e: str) -> bool:
    if e is None:
        return False
    lower = e.lower()
    for l in lst:
        if lower in l:
            return True
    return False


# 根据content_type和content_disposition判断是否为文件下载响应
def if_download_file(content_type, content_disposition) -> bool:
    if content_type is None:
        content_type = ''
    if content_disposition is None:
        content_disposition = ''
    result = False
    if (if_contain(DOWNLOAD_CONTENT_TYPES, content_type) or if_contain(PICTURE_CONTENT_TYPES,
                                                                       content_type)
            or DOWNLOAD_CONTENT_DISPOSITION in content_disposition.lower()):
        result = True
    print(
        f"CM文件响应检测结果:{result}，content_type:{content_type}，content_disposition:"
        f"{content_disposition}")
    return result


# 根据content_type判断是否为图片响应
def if_download_picture(content_type: str) -> bool:
    if content_type is None:
        content_type = ''
    result = False
    if if_contain(PICTURE_CONTENT_TYPES, content_type):
        result = True
    print(f"CM图片响应检测结果:{result}，content_type:{content_type}")
    return result


# 利用requests开启可下载文件
def requests_download_file(url: str, path: str) -> None:
    try:
        print(f'requests开始下载: {url}')
        response = requests.get(url)
        content_type = response.headers.get('Content-Type', '""')
        content_disposition = response.headers.get('Content-Disposition', '""')
        if response.status_code == 200 and if_download_file(content_type, content_disposition):
            with open(path, 'wb') as file:
                file.write(response.content)
            print(f'requests下载完成: {path} from {url}')
        else:
            print(f'requests下载失败，状态码或文件类型不支持下载，状态码: {response.status_code}')
    except Exception as e:
        print(f'requests下载失败，url:{url}，{e}')


# 利用wget强制开启下载文件
def wget_download_file(url: str, path: str) -> None:
    try:
        print(f'wget开始下载: {url}')
        # 下载文件
        file_name = wget.download(url, out=path)
        print(f'wget下载完成: {file_name} from {url}')
    except Exception as e:
        print(f'wget下载失败，url:{url}，{e}')


def get_file_path(path: str, file: str):
    return path + file
