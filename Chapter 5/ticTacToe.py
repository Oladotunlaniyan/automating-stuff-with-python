# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# turn = 'X'

# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '.Move on which space ?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
# printBoard(theBoard)

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}

# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought

# print('Number of things being brought:')
# print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

# Chess Dictionary Validator

# board = {'1h:':'bking', '6c':'wqueen', '2g':'bbishop', '5h':'bqueen', '3e':'wking'}

# def isValidChessBoard(board):
#     if 'bking' not in board.values() or 'wking' not in board.values():
#         return False
#     if len.board > 16:
#         return False
#     bCount = 0
#     wCount = 0
#     for piece in board.values():
#         if piece[0] == 'b':
#             bCount += 1
#         if piece[0] == 'w':
#             wCount += 1
#     if bCount > 16 or wCount > 16:
#         return False    
#     for space in board.keys():
#         if int(space[0]) > 8 or int(space[0]) < 1:
#             return False
#         if space[1] not in 'abcdefgh':
#             return False
#     return True

# print(isValidChessBoard(board))


# Fantasy Game Inventory

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
            print(str(v) + ' ' + k)
    item_total += v
    print('Total number of items: ' + str(sum(inventory.values())))

# displayInventory(inventory)


# List to Dictionary Function for Fantasy Game Inventory

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin','ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)