import random 
guess = int()

while guess not in ('0', '1'):
    print('Guess the coin toss! Enter heads(1) or tails(0): ')
    guess = input()
toss = random.randint(0,1)

if int(guess) == toss:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess =  input()
    if guess in ('0', '1') and int(guess) == toss:
        print('You got it')
    else:
        print('Nope. You are really bad at this game.')