import re

def validPassword(password_str):
    passwordRegex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$')
    mo = passwordRegex.search(password_str)


print('Enter your password :')

mo = input()

if validPassword(mo):
    print('Your password is strong.')
else:
    print('Your password is weak. Please choose a stronger password.')

