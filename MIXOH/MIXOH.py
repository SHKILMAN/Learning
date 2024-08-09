# print("Hello World")
# print("se \n \n co \t nd line")
# print("результат: ", 5 ** 3)
# print("результат: ", pow(5, 3))
# print("результат: ", round(5 / 3))
# input("Your age: ")
# number = 5
# digit = 4.3546
# word = "результат:"
# print(word, digit)
# del number

# number = 8
# print("number:", number)

#num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# num1 = num1 + 5
# num1 += 5

# print("result: ", num1 + num2)
# print("result: ", num1 - num2)
# print("result: ", num1 * num2)
# print("result: ", num1 / num2)
# print("result: ", num1 // num2)
# print("result: ", num1 % num2)
# print("result: ", num1 ** num2)

# word = "Hello"
# print(word * 5)

# word = 10
# print(word + 10)

# if 5==5:
#     print("yes")
# #     print("!!!")
# user_data = int(input("Enter a number: "))
#
# ishappy = True
#
# if ishappy or user_data == 1:
#     print("You are Happy")
# elif user_data == 5:
#     print("Number is 5")
# else:
#     print("You are Sad")

# user_data = int(input("Enter a number: "))
# if user_data > 5:
#     print("Number is bigger than 5")
# if user_data < 5:
#     print("Number is smaller than 5")
# if user_data == 5:
#     print("Number is equal to 5")

# data = input("Enter you number: ")
#
# number = 5 if data == "five" else 0

# if data == 'Five':
#     number = 5
# else:
#     number = 0

# print(number)



#
# for i in range(1, 11, 2):
#     print(i)
#
# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "l":
#         count += 1
#
# print("Count:", count)

# i = 5
# while i < 15:
#     print(i)
#     i += 2
#
# TTT = True
#
# while TTT:
#     if input("Enter code: ") == "stop":
#         TTT = False
#         print ("Victory")
#
# for i in range(1, 11):
#     if i == 8:
#         break
#
#     if i % 2 == 0:
#         continue
#
#     print(i)

# found = None
# for i in "hello":
#     if i == "r":
#         found = True
#         break
# else:
#     found = False
#
# print(found)
#
# nums = [4, 45, 6, 7, 43, 246, 7, "hello", 4.33, True, [3,4,6,7]]
# nums[0] = 400
# nums[9] = 44.44
# print(nums[-1][-1])
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.append(100)
# numbers.insert(3, True)
# b = [2, 3, 5, 5, 6, 7, 8, 654, 3, 2]
# numbers.extend(b)
# numbers.sort()
# numbers.reverse()
# numbers.pop(0)
# numbers.remove(2)
# numbers.clear()

# print(numbers.count(5))
# print(len(numbers))
#
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, "hello", False]
# for el in nums:
#     el *= 2
#     print(el)
#
# n = int(input("Enter length: "))
#
# user_list = []
#
# i = 0
# while i < n:
#     string = "Enter element # " + str(i+1) + ": "
#     user_list.append(input(string))
#     i += 1
#
# print(user_list)

# word = "Hello World, sport, car"
# print(word[1])
# print(len(word))
# print(word.count("l"))
# print(word.lower())
# print(word.upper())
# print(word.capitalize())
# print(word.title())
# hobby = word.split(', ')
# print(hobby[1])
#
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
#
# result = ", ".join(hobby)
# print(result)
#
# word = "football"
#
# print(word[0:-1:2])
#
# lis = [6, 4, "Stroka", True, 6.5]
# print(lis[2:5:2])
# print(lis[::2])
# print(lis[::-1])
#
data = (0, 1, 2, 3, 4, 5, True, 5.3, 'Hello World')
# print(data[1:5])
#
# print(data.count(3))

# data = (5,)

# print(data)
# for el in data:
#     print(el)
#
# nums = [5, 6, 7, 8, 9, 10]
# new_data = tuple(nums)
# word = tuple('Hello World')
# print(new_data)
# print(word)

# country = {'code': 'USA', 'name': 'United States of America', 'population': 2000000}
# country = dict(code='usa', name='United States')
# print(country['name'])
# print(country['population'])

# print(country.items())
#
# for key, value in country.items():
#     print(key, " - ", value)
#
# print(country['code'])
# print(country.get('name'))
# country.pop('population')
# country.clear()
# country.popitem()
# print(country.keys())
# print(country.values())
# country['code'] = 'none'
# print(country.items())
#
# person = {
#     'user_1': {
#         'first_name': 'John',
#         'last_name': 'Doe',
#         'age': 25,
#         'address': ('UA'),
#         'grades': {'math': 5, 'PE': 10}
#     }
# }
#
# print(person['user_1'])

# data = set('Hello World')
# data = {5, 6, 7, 8, 5, 5, 5, 5}
#
# data.add(44)
# data.update(['55', True, 4, 6.5])
# data.remove(True)
# data.pop()
# data.clear()
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 5, 5, 5, 0, 3, 2, 5]
# new_nums = set(nums)
# print(new_nums)
# new_data = frozenset([7, 4, 5, 3, 6, 4, 6, 3, 7, True, 'Five'])
# print(new_data)
#
# def test_func(word):
#     # pass
#     print(word, end="")
#     print("!")
#
# test_func("Hi")
# test_func(5)
# test_func(True)

# def summa(a, b):
    # res = a + b
    # print("Result: ", res)
    # return a + b

# summa(5.4, 6.5)
# res = summa(5.4, 6.5)
# print(res)
# print(summa("Wi", "Fi"))

# def minimal(l):
#     min_number = l[0]
#     for el in l:
#         if el < min_number:
#             min_number = el
#     print(min_number)
#
# nums1 = [9, 22, 55, 1, 2, 3, 4, 5]

# min = nums1[0]
# for el in nums1:
#     if el < min:
#         min = el
#
# print(min)

# nums2 = [9, 2.2, 55, 1, 2, 3, 4, 5, 0.1]
#
# min2 = nums2[0]
# for el2 in nums2:
#     if el2 < min2:
#         min2 = el2

# print(min2)
#
# minimal(nums1)
# minimal(nums2)
#
# func = lambda x, y: x * y
# res = func(5, 2)
# print(res)
#
# data = input("Enter your text: ")
#
# file = open('data/text.txt', 'a')
#
# file.write('\n' + data + "\n")
#
# file.close()
#
# file = open('data/text.txt', 'r')

# print(file.read())
#
# for line in file:
#     print(line, end="")
#
# file.close()
#
# try:
#     x = int(input('Enter a number: '))
#     x += 5
#     print(x)
# except ValueError:
#     print('Enter a number, please')

# x = 0
# while x == 0:
#     try:
#         x = int(input('Enter a number: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Enter a number, please!')
#
# try:
#     x = 5 / 0
#     x = int(input())
# except ZeroDivisionError:
#     print("Division by zero")
# except ValueError:
#     print("Value Error")
# else:
#     print("Else")
# finally:
#     print("Finally")

# try:
    # file = open("text.txt", 'r')
    # file.read()
    # file.close()
# except FileNotFoundError:
#     print("File Not Found")
# finally:
#     file.close()
#
# try:
#     with open('text.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File Not Found")
#
# import time
#
# time.sleep(4)
# print("Hello World")


# import datetime as dt, sys, os, platform
# import math
# print(dt.datetime.now().time())
# print(sys.path)
# print(os.name)
# from math import sqrt as s, ceil
# print(platform.system())
# print(ceil(s(25)))
#
# import mymodule as my
# print(my.name)
# my.hello()
#
# from mymodule import add_three_numbers as add
# print(add(5, 3, 0))
#
# import cowsay as c
# c.cow("Hello World")

# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(self.name, self.age, "Happy? - ", self.isHappy)
#
# cat1 = Cat()
# cat1.set_data('Murzik', 25, True)
# cat1.name = "Murzik"
# cat1.age = 25
# cat1.isHappy = True
#
# cat2 = Cat()
# cat2.set_data('Vasya', 35, False)
# cat2.name = "Vasya"
# cat2.age = 35
# cat2.isHappy = False
#
# print(cat1.name)
# print(cat2.name)
# print(cat1.age)
# print(cat2.age)
#
# cat1.get_data()
# cat2.get_data()
#
#
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def __init__(self, name = None, age = None, isHappy = None):
#         self.set_data(name, age, isHappy)
#         self.get_data()
#     def set_data(self, name = None, age = None, isHappy = None):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print("My name is", self.name, "I`m", self.age, "years old.", "Am I Happy? That`s -", self.isHappy)
#
# cat1 = Cat()
# cat1.set_data()
#
# cat2 = Cat('Vasya', 35, False)
# cat2.set_data('Vasya', 35, False)

# cat1.get_data()
# cat2.get_data()
#
# class Building:
#     year = None
#     city = None
#
#     def __init__(self, year, city):
#         self.year = year
#         self.city = city
#
#     def get_info(self):
#         print("Year:", self.year, " City:", self.city)
#
# class School(Building):
#     pupils = 0
#
#     def __init__(self, year, city, pupils):
#         super(School, self).__init__(year, city)
#         self.pupils = pupils
#
#     def get_info(self):
#         super().get_info()
#         print("Pupils:", self.pupils)
#
# class House(School):
#     pass
#
# class shop(Building):
#     pass
#
# school = School(2020, 'Tampa', 5000)
# school.get_info()
# house = House(2011, 'Tampa', 51)
# house.get_info()
# shop = Building(2005, 'Tampa')
# shop.get_info()

import webbrowser

# def validator(func):
#     def wrapper(url):
#         if "." in url:
#             func(url)
#         else:
#             print("Wrong URL")
        # func(url)
        # print("text posle funkcii")
#     return wrapper
#
# @validator
# def open_url(url):
#     webbrowser.open(url)
#
# open_url('https://google.com')

