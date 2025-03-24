# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

# def printTable(tableData):
#     colWidths = [0] * len(tableData)

#     for i in range(len(tableData)):
#         colWidths[i] = max(len(item) for item in tableData[i])
    
#     numRows = len(tableData[0])
#     numCols = len(tableData)

#     for i in range(numRows):
#         for j in range(numCols):
#             print(tableData[j][i].rjust(colWidths[j]), end=' ')
#         print()

# printTable(tableData)


import zombiedice;
zombiedice.demo()

