import re

def validPassword(password_str):
    passwordRegex = re.compile(r'[A-Z][a-z][0-9]\d{8,}')
    mo = passwordRegex.search(password_str)


    print('Enter your password :')

    mo = input()

    if mo  