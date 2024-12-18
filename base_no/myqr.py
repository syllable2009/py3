import qrcode
from MyQR import myqr
import qrtools
from PIL import Image
import matplotlib.pyplot as plt
# 二维码内容
data = "https://www.baidu.com"

def simpleQr(data):
    # 生成二维码
    img = qrcode.make(data=data)
    # 直接显示二维码
    img.show()
    # 保存二维码为文件
    # img.save("/Users/jiaxiaopeng/temp/baidu.jpg")

def colorQr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 设置二维码数据
    qr.add_data(data=data)

    # 启用二维码颜色设置
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")

    # 显示二维码
    img.show()
    # 保存二维码为文件
    # img.save("/Users/jiaxiaopeng/temp/baidu.jpg")


