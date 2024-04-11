from flask import Flask,render_template     #导入Flask类
import random
print(random.__file__)
app=Flask(__name__)         #实例化并命名为app实例

# 这个还有顺序，必须卸载执行之前？
@app.route('/')
def index():
    return 'welcome to my webpage!'

@app.route('/index')
def index2():
    msg="my name is xxx, China up!"
    return render_template("index.html",data=msg)   #调用render_template函数，传入html文件参数

if __name__=="__main__":
    app.run(port=2020,host="127.0.0.1",debug=True)   #调用run方法，设定端口号，启动服务

