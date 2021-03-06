import numpy as np

a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)

# print(a) # >>>[0 1 2 3 4]
# print(b) # >>>[0 1 2 3 4]
# print(c) # >>>[0 1 2 3 4]
# print(d) # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
# print(a[3]) # >>>3


a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
print(a)
print(a[2,4]) # >>>25