
import math
print(round(5.678,2))
print(math.floor(5.6))
print(math.ceil(5.6))

from decimal import getcontext,Decimal
# print(getcontext ())
getcontext().prec = 50
print(Decimal(1)/Decimal(9))
print('----------------')
tup1 = ('physics', 'chemistry', 1997, 2000)
print(tup1[3])
list2 = [x for x in range(2)]
print(list2)
dict = {'name': 'Zara', 'age': 7, 'class': 'First'}
print(dict['name'])
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
print(dataScientist)
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print('\n', Month.Jan)
print('----------------')

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
print('----------------')

