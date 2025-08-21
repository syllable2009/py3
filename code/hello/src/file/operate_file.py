import os

# shutil库作为os模块的补充,提供了复制、移动、删除、压缩、解压等操作
import shutil

def safe_move(src_path, dst_path):
    """安全移动文件（自动处理重名）"""
    filename = os.path.basename(src_path)
    dst_path = os.path.join(dst_path, filename)
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(dst_path):
        new_name = f"{base}_{counter}{ext}"
        dst_path = os.path.join(dst_path, new_name)
        counter += 1
    try:
        shutil.move(src_path, dst_path)
        print(f"文件已从 {src_path} 移动到 {dst_path}")
    except FileNotFoundError:
        print(f"错误：源文件 {src_path} 不存在")
    except PermissionError:
        print(f"错误：无权限操作文件 {src_path}")

def delete_file(file_path):
    """永久删除文件"""
    try:
        os.remove(file_path)
        print(f"文件 {file_path} 已删除")
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
    except PermissionError:
        print(f"错误：无权限删除文件 {file_path}")





