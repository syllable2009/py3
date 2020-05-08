在Python开发和测试过程中主要有两种模式可以选择：脚本模式、命令行模式.
命令行模式在Python开发中并不陌生，简单的说就是python hello_world.py这种使用命令的模式运行Python程序.


tensorflow的Flags
# 内置的sys
import sys
def hello_world():
    print(sys.argv[1], sys.argv[2])
hello_world()
python test.py 1 2

#argparse
import argparse
arg = argparse.ArgumentParser("This is a test!")

def main(arg):
    print(arg.name)
    print(arg.age)
if __name__ == '__main__':
    arg.add_argument("--name", "-n", default="China", type=str, help="the name of your country.")
    arg.add_argument("--age", "-a", default=25, type=int, help="your age.")
    args = arg.parse_args()
    main(args)
python3 test.py --name Chinese --age 26   

# Flags
import tensorflow as tf
​
FLAGS = tf.flags.FLAGS
​
tf.flags.DEFINE_string("train_path", '/voc2012/JPEG', "training file path")
tf.flags.DEFINE_integer("batch_size", 64, "training batch size")
tf.flags.DEFINE_float("lr", 0.01, "learning rate")
​
def main(_):
    print(FLAGS.train_path)
    print(FLAGS.batch_size)
    print(FLAGS.lr)
​
if __name__ == '__main__':
    tf.app.run()  
   
# Click的开发初衷就是使用最少的代码，以一种可组合的方式创建漂亮的命令行接口。
import click

@click.command()
@click.option("--name", default="li", help="your name")
@click.option("--age", default=26, help="your age")
def hello_world(name, age):
    click.echo(name)
    print(age)
hello_world()

可以看出，上述主要用了click的3个方法，分别是，

command
option
echo
这3个方法在Click工具中至关重要，除此之外还有其他的方法，它们的功能分别是，

方法功能

command：用于装饰一个函数，使得该函数作为命令行的接口，例如上述装饰hello_world
option：用于装饰一个函数，主要功能是为命令行添加选项
echo：用于输出结果，由于print函数在2.x和3.x之间存在不同之处，为了更好的兼容性，因此提供了echo输出方法
Choice：输入为一个列表，列表中为选项可选择的值
 