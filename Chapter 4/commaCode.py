# spam = ['apples', 'bananas', 'tofu', 'cats']

# def commaCode(list):
#     for i in range(len(list)-1):
#         print(list[i] + ', ', end ='')
#     print('and' + ' ' + list[-1])


# commaCode(spam) 

#Coin flip streaks

# import random 
# numberOfStreaks = 0
# for experimentNumber in range(10000):
#     coinFlips = []
#     for i in range(100):
#         coinFlips.append(random.randint(0,1))
#     streak = 0
#     for i in range(len(coinFlips)-1):
#         if coinFlips[i] == coinFlips[i+1]:
#             streak += 1
#         else:
#             streak = 0
#         if streak == 6:
#             numberOfStreaks += 1
#             break   
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))
    

#Character Picture Grid

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# for x in range(len(grid[0])):
#     for y in range(len(grid)):
#         print(grid[y][x], end ='')
#     print()