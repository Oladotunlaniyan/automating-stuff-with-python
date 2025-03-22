# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# print(myCat['size'])


# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True: 
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

# spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#     print(v)

# What does v represent?
# v is a loop variable that stores each value from the dictionary spam during each iteration.
# spam.values() returns all the values in the dictionary.
# On each iteration, v takes one of those values.

# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')


# spam = {'name': 'Zophie', 'age': 7}

# # if 'color' not in spam:
# #     spam['color'] = 'black'

# # print(spam.get('color'))

# spam.setdefault('color', 'black')
# print(spam)
# spam.setdefault('color', 'white')
# print(spam)

# import pprint

# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# pprint.pprint(count)

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

spam = {'cat': 100}
print(spam['cat'])
print(spam.values())
print(spam.keys())