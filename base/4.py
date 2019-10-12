import os, click

def test1():
    url = 'http://www.baidu.com/file/download?test=123'
    filename = url.split('/')
    print(filename)
    print(filename[-1])
    abc = input("你输出试试：\n")
    print(abc)

if __name__ == '__main__':
	music_list_name = 'music_list.txt'
	# 如果music列表存在, 那么开始下载
	if os.path.exists(music_list_name):
		with open(music_list_name, 'r') as f:
			music_list = list(map(lambda x: x.strip(), f.readlines()))

		for song_num, song_name in enumerate(music_list):
			print("{0},{1}".format(song_num, song_name))

	else:
	    click.echo('music_list.txt not exist.')