# name = 'Carol'
# age = 3000

# if name == 'Alice':
#     print('Hi,Alice')
# elif age < 12:
#     print('You are not Alice, kiddo')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire')
# elif age > 100:
#     print('You are not Alice, grannie')
# else:
#     print('You are neither Alice nor a little kid')

# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1
#     print(spam)

# while True:
#     print('Please type your name')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')

# while True:
#     print('Who are you ?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
#     print('Access granted.')

# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times ('+ str(i) + ')')

# total = 0
# for num in range(101):
#     total = total + num
#     print(total)

# print('My name is')
# i=0
# while i < 5:
#     print('Jimmy Five Times ('+ str(i) + ')')
#     i = i + 1

# for i in range(0, 10, 2):
#     print(i)

# for i in range(5, 1, -1):
#     print(i); 

# import random
# for i in range(5):
#     print(random.randint(1, 10))    

# import sys

# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')


# import random
# secretNumber = random.randint(1, 20)
# print ('I am thinking of a number between 1 and 20.')
# print('You have 6 guesses to get it right.')
# print('Take a guess.')
# for guessesTaken in range(1,7):
#    guess = int(input())
#    if guess < secretNumber:
#         print('Your guess is too low.')
#    elif guess > secretNumber:
#         print('Your guess is too high.')
#    else: 
#         break
#    if guess == secretNumber:
#         print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
#    else:
#         print('Nope. The number I was thinking of was ' + str(secretNumber))


# import random, sys


# print('ROCK, PAPER, SCISSORS')

# # These variables keep track of the number of wins, losses, and ties.
# wins = 0
# losses = 0
# ties = 0

# while True: #The main game loop
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True: #The player input loop
#         print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit() #Quit the program
#         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#                 break #Break out of the player input loop
#         print('Type one of r, p, s, or q.')

#     #Display the player's move  
#     if playerMove == 'r':
#         print('ROCK versus...')
#     elif playerMove == 'p':
#         print('PAPER versus...')
#     elif playerMove == 's':
#         print('SCISSORS versus...')
#     #`Display what the computer chose
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print('PAPER')
#     elif randomNumber == 3:
#         computerMove = 's'
#         print('SCISSORS')

#     #Display and record the win/loss/tie
#     if playerMove ==  computerMove:
#         print('It is a tie!')
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print('You lose!')
#         losses = losses + 1
    

i = 1
while i >= 1 and i <= 10:
    print (i)
    i = i + 1