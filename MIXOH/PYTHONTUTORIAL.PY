# print("Mykhailo Shkilniuk")
# print('1----')
# print('2|||||')
# print('3*|' * 10)

# print("    **    **")
# print("   *  *  *  *")
# print("  *    **    *")

# price = 10
# rating = 4.9
# name = "Mykhailo"
# is_published = False
# print(price)

# full_name = 'John Smith'
# age = 20
# is_new = True
# print(full_name, age, "Is new patiant:", is_new)

# name = input('What is your name? ')
# print('Hi ' + name)

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name + " likes " + color)

# birth_year = input("Birth year: ")
# age = 2024 - int(birth_year)
# print(age)

# weight = input("What is your weight (in pounds)? ")
# print("Your weight is", float(weight) * 0.453592, "kg.")

# name = "Jennifer"
# print(name[1:-1])
#
# first = "John"
# last = "Smith"
# message = first + ' [' + last + '] is a coder'
# msg = f"{first} [{last}] is a coder"
# print(message)
# print(msg)

# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("o"))
# print(course.replace("Beginners", "Absolute Beginners"))
# print("Python" in course)

# x = 10 + 3 * 2
# print(x)
# exponentiation 2 ** 3
# multiplication or division
# addition or substraction

# import math
#
# x = -2.9
# print(round(x))
# print(abs(x))

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It`s a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It`s a cold day")
#     print("Wear warm clothes")
# else:
#     print("It`s a lovely day")
#     print("Enjoy your day")

# price_of_house = 1000000
# good_credit = True
#
# if good_credit:
#     down_payment = 0.1 * price_of_house
#     # print("Your down payment is $", down_payment)
# else:
#     down_payment = 0.2 * price_of_house
#     # print("Your down payment is $", down_payment)
# print(f"Your down payment is: ${down_payment}")

# has_high_income = True
# has_good_credit = False
#
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# else:
#     print("NOT eligible for loan")

# has_high_income = False
# has_good_credit = True
#
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
# else:
#     print("NOT eligible for loan")

# has_high_income = True
# has_good_credit = True
# has_criminal_record = False
#
# if has_high_income and has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
# else:
#     print("NOT eligible for loan")

# temperature = 30
#
# if temperature > 30:
#     print("It`s a hot day")
# else:
#     print("It`s not a hot day")

# name = input("Enter your name: ")
# length_name = len(name)
# if length_name < 3:
#     print("Name must be at least 3 characters")
# elif length_name > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good!")


# weight = int(input("Weight: "))
# lbs_or_kg = input("(L)bs or (K)g: ")
#
# if lbs_or_kg == "L" or lbs_or_kg == "l":
#     print("You are ", 0.45 * weight, " kg")
# elif lbs_or_kg == "K" or lbs_or_kg == "k":
#     print("You are ", weight / 0.45, " pounds")
# else:
#     print("Are your weight in Kg or Lbs?")

# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
#
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# elif unit.upper() == "K":
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")
# else:
#     print("Is your weight in Kg or Lbs?")


# n = 1
# while n <= 10:
#     print("*" * n)
#     n += 1
# print("Done")
#
# n = int(input("Guess a number: "))
#
# while n != 9:
#     print("Try again!")
#     l = int(input("Guess number: "))
#     while l != 9:
#         print("Try again! You have last chance!")
#         k = int(input("Guess number: "))
#         if k != 9:
#             print("You lost")
#         else:
#             print("You win")
#         break
#
# print("You win")

# secret_number = 9
# guess_counter = 0
# guess_limit = 3
# while guess_counter < guess_limit:
#     guess = int(input("Guess a number: "))
#     guess_counter += 1
#     if guess == secret_number:
#         print("Congratulations! You won!")
#         break
#     if guess_counter == guess_limit - 1:
#         print("You have last chance!")
# else:
#     print("Sorry, you lost!")

# command = input("> ")
#
# if command.upper() == "start":
#     print("Car started... Ready to go!")
# elif command.upper() == 'stop':
#     print("Car stopped...")
# elif command.upper() == 'quit':
#     print("Game is over...")
# else:
#     print("I don`t understand that...")


# command = ""
# started = False
# stopped = False
# while True:
#     command = input("> ").lower()
#     if command == 'start':
#         if started:
#             print("Car is already started...")
#         else:
#             started = True
#             print("Car started... Ready to go!")
#     elif command == 'stop':
#         if not started:
#             print("Car is already stopped...")
#         else:
#             started = False
#             print("Car stopped...")
#     elif command == 'help':
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == 'quit':
#         print("Game is over...")
#         break
#     else:
#         print("Sorry, I don`t understand that...")


# for item in range(0, 105, 5):
#     print(item)


# prices = [10, 20, 30, 50]
# total = 0
# for item in prices:
#     total += item
# print(f"Total: {total}")


# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     print(item * "x")

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)


# names = ["Mykhailo", "Svitlana", "Fieliks", "Solomiia", "Robert"]
# names[0] = "Jon"
# print(names[0:])

# numbers = [2, 90, 155, 1, 55, 200, 2.55, 5.7, 999, 4, 5]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 20
# print(matrix[0][1])

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [2, 5, 3, 7, 5, 8, 9, 22, 55]
# numbers.append(20)
# numbers.insert(0, 999)
# numbers.remove(5)
# numbers.pop()
# print(numbers.index(5))
# print(numbers)
# print(2 in numbers)
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# print(numbers2)

# numbers = [2, 5, 3, 7, 5, 8, 9, 22, 55, 2, 2, 2, 3, 3, 5, 5, 6, 6, 8, 8, 9]
# uniq = []
# for item in numbers:
#     if item not in uniq:
#         uniq.append(item)
# print(uniq)

# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# print(customer["name"])

# phone_number = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
#     "0": "Zero"
# }
# output = ""
# for ch in phone_number:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)


# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)": "🙂",
#     ":(": "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user("Jack", "Silver")
# greet_user("Michael", "Smith")
# print("Finish")

# def square(number):
#     return number * number
#
#
# result = square(3)
# print(result)


# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "🙂",
#         ":(": "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))


# try:
#     age = int(input("Age: "))
#     income = 2000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be 0.")
# except  ValueError:
#     print("ValueError. Enter a number please.")



