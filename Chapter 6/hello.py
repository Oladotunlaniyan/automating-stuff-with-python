# 

# spam = "That is Alice's cat."
# print(spam)


# spam = 'Say hi to Bob\'s mother.'
# # print(spam)
# # print("Hello there!\nHow are you\nI\'m doing fine.")

# print (r'That is Carol\'s cat')


# print('''Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary and extortion.

# Sincerely,      
# Bob''')

"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

# spam = 'Hello, World!'
# fizz = spam[0:5]
# print(fizz)

# 'Hello' in 'Hello World!'

# name = 'Al'
# age = 4000

# print('My name is %s. I am %s years old.' %(name, age))

# print(f'My name is {name}. Next year I will be {age + 1}')


# Useful String Methods

# spam = 'Hello, World!'
# spam = spam.upper()
# spam1 = spam.lower()

# print(spam)

# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feel great too')
# else:
#     print('I hope the rest of your day is good.')

# spam = 'Hello, World!'
# spam = spam.islower()

# # isalpha() Returns True if the string consists only of letters and is not blank
# # isalnum() Returns True if the string consists only of letters and numbers and is not blank
# # isdecimal() Returns True if the string consists only of numeric characters and is not blank
# # isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
# # istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters


# print(spam)


# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')

# while True:
#     print('Select a new password(letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')

# print('Hello, World!'.startswith('Hello'))
# print('Hello, World!'.endswith('World!'))

# print(','.join(['cats', 'rats', 'bats']))
# print(' '.join(['My', 'name', 'is', 'Simon']))

# print('My name is Simon'.split())

# print('My name is Simon'.split('m'))

# spam = '''Dear Alice, 
# How have you been? I am fine.
# There is a container in the fridge
# that is labeled "Milk Experiment."

# Please do not drink it.
# Sincerely,
# Bob'''

# print(spam.split('\n'))

# spam = 'Hello wordl!'.partition('w')
# print(spam)

# spam = 'Hello'.rjust(10, '-')
# print(spam)
# spam1 = 'Hello'.ljust(10, '*')
# print(spam1)



# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies':8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)


# spam = '    Hello World    '
# spam = spam.strip()
# print(spam)
# spam1 = spam.lstrip()
# print(spam1)
# spam2 = spam.rstrip()
# print(spam2)

# import pyperclip
# pyperclip.copy('Hello, World!')
# print(pyperclip.paste())

spam = 'Hello, world!'

print('-'.join('There can be only one.'.split()))
# print(spam[0:5])
# print(spam[5])
# print(spam[3:])