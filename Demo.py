#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-03-14 20:40
# @Author: cainjiang
# @File  : Demo.py
import matplotlib.pyplot as plt

from pizza import make_pizza as mp


def greet_user():
    """显示简单的问候语"""
    print("Hello")


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
if bicycles:
    print('列表不是空的')
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

alien_0 = {
    'point': '5',
    'color': 'green',
    'favorite': 'green',
}

alien_1 = {
    'point': '4',
    'color': 'red',
    'favorite': 'green',
}

aliens = [alien_0, alien_1]

for alien in aliens:
    print(alien)

print(sorted(alien_0.keys()))

for k, v in alien_0.items():
    print("\nKey: " + str(k))
    print("Value: " + str(v))

for k in alien_0.keys():
    print(k.title())

for v in set(alien_0.values()):
    print(v)

print(alien_0)
print(alien_0['color'])
print(alien_0['point'])
del alien_0['color']

waixingren = []
for alien_number in range(30):
    new_alien = {
        'point': '4',
        'color': 'red',
        'favorite': ['red', 'green', 'blue'],
        'planet': {
            'first': '地球',
            'second': '家园',
        },
    }
    waixingren.append(new_alien)
for alien in waixingren[:5]:
    print(alien)
print("……")
print("total num of alien: " + str(len(waixingren)))

# input_message = input("请输入信息，我会原样打印出来的：")
# print(input_message)
# age = input("年龄：")
# age = int(age)
# if age > 19:
#     print("你已经成年了")
# else:
#     print("你还没有成年呢")

current_num = 1
while current_num <= 5:
    current_num += 1
    if current_num == 2:
        continue
    print(current_num)

unconfired_users = ['alice', 'brian', 'candace']
confired_users = []
while unconfired_users:
    current_user = unconfired_users.pop()
    print("Verifying user: " + current_user.title())
    confired_users.append(current_user)
print("\nThe following users have been confirmed:")
for confired_user in confired_users:
    print(confired_user.title())

pets = ['dog', 'cat', 'dog', 'rabbit']
while 'dog' in pets:
    pets.remove('dog')
print(pets)

greet_user()
mp('mushroms', 'extra cheese')

input_values = [1, 2, 3, 4]
pingfang = [1, 4, 9, 16]
plt.title("pingfangshu")
# plt.plot(input_values, pingfang)
# plt.xlabel("Value")
# plt.ylabel("PingFang")
# plt.tick_params('both')

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, 20, edgecolors='none', c=y_values)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('pingfang.png', bbox_inches='tight')
