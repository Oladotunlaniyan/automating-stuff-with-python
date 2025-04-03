import pyinputplus as pyip

#inputStr()
#inputNum()
# 
# 
# 

# response = pyip.inputNum()
# response = input('Enter a number: ')

# response = pyip.inputInt(prompt = 'Enter a number: ')

# print(response)

# response = pyip.inputNum('Enter num: ', min=4)
# response = pyip.inputNum('>', min=4, lessThan=6)

# response = pyip.inputNum('Enter num: ')
# response = pyip.inputNum(blank=True)


# response = pyip.inputNum(limit=2)

# response = pyip.inputNum(timeout=10)

# response =  pyip.inputNum(limit=2, default='N/A')

# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

# response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])


# def addsUpToTen(numbers):
#     numbersList = list(numbers)

#     for i, digit in enumerate(numbersList):
#         numbersList[i] = int(digit)

#     if sum(numbersList) != 10:
#         raise Exception('The digits must add up to 10, not %s'%(sum(numbersList)))
#     return int(numbers)


# response = pyip.inputCustom(addsUpToTen)