#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

x = [x*y for x in range(9) for y in range(9) if x % 1 == 0]
i = iter(x)
print(type(x))
print(next(i))
