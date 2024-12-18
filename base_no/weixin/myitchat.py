import itchat,re

#itchat这个开源项目，作者是@LittleCoder，已经把微信的接口完成了，大大的方便了我们对微信的挖掘，以下的功能也通过itchat来实现。
# 登录
itchat.login()
# 发送消息
itchat.send(u'你好', 'filehelper')

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

for i in friends[1:]:
    print(i["Sex"])
    # 获取个性签名
    signature = i["Signature"]
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    print(signature)