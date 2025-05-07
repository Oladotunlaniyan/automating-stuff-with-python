# import csv 
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# exampleData 

# exampleData[0][0]
# exampleData[0][1]
# exampleData[1][1]
# exampleData[6][1]

import csv 

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Hello, world!'])

