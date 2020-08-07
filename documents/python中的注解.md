# @property
s = Student()
s.score = 9999
为了控制参数赋值，将方法转换成一个属性(调用不加括号)，修改后只有一个参数self
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# @abstractmethod
声明为抽象方法，含抽象方法的类不能实例化，必须重写@abstractmethod修饰的方法      

# @abstractmethod
静态方法，在不初始化一个对象的前提下，就可以调用其方法，

        