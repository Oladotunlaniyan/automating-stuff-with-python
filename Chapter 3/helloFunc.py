# def hello():
#     print ('Howdy!')
#     print ('Howdy!!!')
#     print ('Hello there.')

# hello() 
# hello()
# hello()

# def hello(name):
#     print ('Hello ' + name)

# print(name)
# hello('Alice')
# hello('Bob')

# def sayHello(name):
#     print('Hello, ' + name)
# sayHello('Al')


# import random

# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'

# print(getAnswer(random.randint(1,9)))

# spam = print('Hello!')
# None == spam

# print('cats', 'dogs', 'mice', sep=',')

# def a():
#     print('a() starts')
#     b()
#     d()
#     print('a() returns')  

# def b():
#     print('b() starts')
#     c()
#     print('b() returns')

# def c():
#     print('c() starts')
#     print('c() returns')

# def d():
#     print('d() starts')
#     print('d() returns')

# a()

# def spam():
#     eggs = 31337
# spam()
# print(eggs)

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     # print(ham)
#     eggs = 0

# spam()

# def spam():
#     eggs = 'spam local'
#     print(eggs) # prints 'spam local'

# def bacon():
#     eggs = 'bacon local'
#     print(eggs) # prints 'bacon local'
#     spam()
#     print(eggs) # prints 'bacon local'

# eggs = 'global'
# bacon()
# print(eggs) # prints 'global'

# def spam():
#     global eggs 
#     eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs)

# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')

# print(spam(2))
# print(spam(12))
# print(spam(0))

# import time, sys
# indent = 0
# indentIncreasing = True

# try: 
#     while True: # The main program loop.
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) 
#         if indentIncreasing:
#             indent = indent + 1
#             if indent == 20:
#                 indentIncreasing = False
#         else:
#             indent = indent - 1 
#             if indent == 0:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit 