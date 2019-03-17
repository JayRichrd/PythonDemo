#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-03-14 20:40
# @Author: cainjiang
# @File  : Demo.py
age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)

bicycles = ['treak', 'redline', 'specialized']
print(bicycles)

print(bicycles[0].title())

print(bicycles[-1])

bicycles.append('ducati')
for bycle in bicycles:
    print(bycle)
    print('ok')

print(bicycles)

bicycles.reverse()
print(bicycles)
print(len(bicycles))

bicycles.sort(reverse=True)
print(sorted(bicycles, reverse=True))
print(bicycles)

bicycles.insert(1, 'honda')
print(bicycles)

del bicycles[0]
print(bicycles)

print(bicycles.pop(1))
print(bicycles)

bicycles.remove('honda')
print(bicycles)

for value in range(1, 5):
    if 3 <= value < 5:
        print(value)
    elif value < 3:
        print('小于3了，不打印')
    else:
        print('')

numbers = list(range(1, 11, 2))
print(numbers)
squares = []
for value in numbers:
    squares.append(value ** 2)
print(min(squares))
print(max(squares))
print(sum(squares))
pingfang = [number ** 2 for number in range(1, 11)]
print(pingfang)
print(pingfang[-3:])
dimens = (200, 300)
print(dimens)
