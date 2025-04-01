#Pattern matching with regular expressions

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False 
#     if text[3] != '-':
#         return False 
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False 
#     return True


# # print('415-555-4242 is a phone number:')
# # print(isPhoneNumber('415-555-4242'))
# # print('Is Moshi moshi a phone number ?')
# # print(isPhoneNumber('Moshi moshi'))

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
# print('Done')


# import re 

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
# print(mo.group())
# print(mo.groups())

# phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is (415) 555-4242.')
# print(mo.group())

#  In regular expressions, the following characters have special meanings:

# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )


# re.compile(r'\(Parentheses\)')

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))
# print(mo.group())

# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# mo1.group()
# mo2 = batRegex.search('The Adventures of Batwoman')
# mo2.group()

# print(mo1.group())
# print(mo2.group())

# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My number is 415-555-4242')
# mo2 = phoneRegex.search('My number is 555-4242')

# print(mo1.group())
# print(mo2.group())  

# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# mo2 = batRegex.search('The Adventures of Batwoman')
# mo3 = batRegex.search('The Adventures of Batwowoman')
# print(mo1.group())
# print(mo2.group())
# print(mo3.group())

# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batwoman')
# mo2 = batRegex.search('The Adventures of Batwowoman')
# mo3 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
# print(mo2.group())  
# print(mo3.group())

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242')

# print(mo.group(0))
# print(mo.group(1))
# print(mo.group(2))

# numRegex = re.compile(r'[A-Z][a-z]*\sWatanabe')

# mo = numRegex.search('Qawi Watanabe')

# newRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)
# mo = newRegex.search('Alice eats baseballs.')

# print(mo.group())


# print(mo)

# xmasRegex = re.compile(r'\d+\s\w+')
# mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(mo)

# vowelRegex = re.compile(r'[^aeiouAEIOU]')
# print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))


# beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.search('Hello World!'))
# print(beginsWithHello.search('He said Hello.'))

# endsWithNumber = re.compile(r'\d$')
# print(endsWithNumber.search('Your number is 42'))
# print(endsWithNumber.search('Your number is forty two'))

# wholeStringIsNum = re.compile(r'^\d+$')
# print(wholeStringIsNum.search('1234567890'))
# print(wholeStringIsNum.search('12345xyz67890'))
# print(wholeStringIsNum.search('12  34567890'))

# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat'))

# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))

# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# noNewlineRegex = re.compile('.*')
# noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

# newlineRegex = re.compile('.*', re.DOTALL)
# mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# print(mo)

''' 
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.'''

# regex1 = re.compile('Robocop')
# regex2 = re.compile(r'ROBOCOP', re.I)
# regex3 = re.compile(r'rob0cop', re.IGNORECASE)
# regex4 = re.compile('robocop')

# print(regex1.search('Robocop').group())


# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
