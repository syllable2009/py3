import os
from classify_files import image_ext, video_ext, ignore_ext

def list_directory_contents(path='.'):
    """列出指定路径下的所有条目（文件和子目录）"""
    try:
        entries = os.listdir(path)
        print(f"目录 '{os.path.abspath(path)}' 中的内容：")
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                print(f"根路径下出现错误的文件: {entry}")
            elif os.path.isdir(full_path):
                valid_files(full_path)
    except FileNotFoundError:
        print(f"错误：路径 '{path}' 不存在")
    except PermissionError:
        print(f"错误：无权限访问路径 '{path}'")


def valid_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        print(f"当前目录: {root}")
        print(f"子目录: {dirs}")
        print(f"文件: {files}")
        for file in files:
            file_lower = file.lower()
            if file_lower.endswith(image_ext):
               pass
            elif file_lower.endswith(video_ext):
               pass
            elif file_lower.endswith(ignore_ext):
                pass
            else:
                file_path = os.path.join(root, file)
                print(f"一级目录下出现错误的文件: {file_path}")

        for dir in dirs:
            print(f"一级目录下出现错误的目录: {dir}")

if __name__ == '__main__':
    target_dir = '/Users/jiaxiaopeng/at'
    # valid_files(target_dir)
    list_directory_contents(target_dir)
