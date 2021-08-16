import os
import requests
from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}


def download_file(url, store_path):
    filename = url.split('/')[-1]
    filepath = os.path.join(store_path, filename)
    data_folder = Path(filepath)
    if len(data_folder.suffix) == 0:
        filepath = filepath + ".jpg"
    file_data = requests.get(url=url, allow_redirects=True, headers=headers).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)


if __name__ == '__main__':
    down_url = "https://iknow-pic.cdn.bcebos.com/5d6034a85edf8db1670bb95a0b23dd54564e74e3";
    # i = 32
    # down_res = requests.get(url=down_url, headers=headers)
    # file_name = "/Users/jiaxiaopeng/Downloads/步步/" + str(i) + ".mp4";
    # with open(file_name, "wb") as code:
    #     code.write(down_res.content)
    download_file(down_url,"/Users/jiaxiaopeng/Downloads");


