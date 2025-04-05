# from pathlib import Path
# Path('spam')/'bacon'/'eggs'


# homeFolder = r'C:\Users\Al'
# subFolder = 'spam'

# # print(homeFolder + '\\' + subFolder)
# print('\\'.join([homeFolder, subFolder]))


from pathlib import Path
import os 

# # Path.cwd()

# Path.home()

# Path(r'C:\Useers\Al\spam').mkdir()

# Path.cwd()

# print(Path.cwd().is_absolute())

# print(os.path.abspath('.'))
# print('Hello')
# print(os.path.abspath('.\\Scripts'))

# calcFilePath = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(calcFilePath))
# print(os.path.dirname(calcFilePath))

# p = Path('C:\\Windows\\System32\\calc.exe')
# list(p.glob('*txt'))


# p = Path('spam.txt')
# print(p.write_text('Hello, world!'))
# print(p.read_text)

# helloFile = open(Path.home()/'spam.txt')

# baconFile = open('bacon.txt','w')
# baconFile.write('Hello, world!\n')
# baconFile.close()

# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable.')

# baconFile.close()

# content = open('bacon.txt')
# print(baconFile.read())
# baconFile.close()

# print(content)

# p = Path('bacon.txt')

# print(p.write_text('Hello, woorld!'))

# print(p.read_text())

# helloContent = helloFile.read()

# print(helloContent)


# sonnetFile = open(Path.home()/ 'C:/Users/Abdul-Qawi/Documents/The Code/python/automating-stuff-with-python/Chapter 9/sonnet29.txt')

# print(sonnetFile.readlines())

# baconFile = open('bacon.txt', 'w')
# print(baconFile.write('Hello, world!\n'))

# baconFile.close()

# baconFile = open('bacon.txt', 'a')

# print(baconFile.write('Bacon is not a vegetable.'))

# baconFile.close()

# baconFile = open('bacon.txt', 'a')

# baconFile.write('Bacon is not a vegetable.')

# baconFile.close()

# baconFile = open('bacon.txt')

# content = baconFile.read()

# baconFile.close()

# print(content)

import shelve

# shelfFile = shelve.open('mydata')

# cats = ['Zophie', 'Pooka', 'Simon']

# shelfFile['cats'] = cats
# shelfFile.close()


# shelfFile = shelve.open('mydata')

# print(type(shelfFile))

# shelfFile = shelve.open('mydata')

# print(list(shelfFile.keys()))

# print (list(shelfFile.values()))


# import pprint

# cats = [{'name':'Zophie', 'desc':'chubby'}, {'name': 'Pooka', 'desc':'fluffy'}]

# print(pprint.pformat(cats))