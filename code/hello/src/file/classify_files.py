import os

image_ext = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
video_ext = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')
ignore_ext = ('.torrent', '.ds_store')

def classify_files(directory):
    images = []
    videos = []
    # 使用os.walk()递归遍历目录树，自动处理子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_ext):
                file_path = os.path.join(root, file)
                images.append(file_path)
            elif file.lower().endswith(video_ext):
                file_path = os.path.join(root, file)
                videos.append(file_path)
            elif file.lower().endswith(ignore_ext):
                pass
            else:
                file_path = os.path.join(root, file)
                print(f"{file_path} is not video or image.")
    return {'images': images, 'videos': videos}

if __name__ == '__main__':
    # target_dir = input('请输入要扫描的目录路径: ')
    target_dir = '/Users/jiaxiaopeng/Downloads/电影合集'
    result = classify_files(target_dir)

    print('\n=== 图片文件 ===')
    for img in result['images']:
        print(img)

    print('\n=== 视频文件 ===')
    for vid in result['videos']:
        print(vid)