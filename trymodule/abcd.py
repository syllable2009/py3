# encoding: utf-8
#!/usr/bin/python

b = 2

class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print('my name is {name} and age is {age}'.format(name = self.name, age = self.age))