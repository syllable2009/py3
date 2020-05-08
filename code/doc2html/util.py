def lines(file):
    for line in file:
        yield line  # 生成文件的每一行内容
    yield '\n'  # 为文件末尾添加空行，保证最后添加到block的行能够被生成。

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():  # 如果读取的行不是空行
            block.append(line)  # 添加行内容到列表
        elif block:  # 如果读取空行（如果文件末尾不是空行，则不会执行下方语句块，导致上方语句块最后一次添加的内容无法生成。）
            yield ''.join(block).strip()  # 连接列表中所有的行内容
            block = []


