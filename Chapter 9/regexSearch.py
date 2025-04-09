import os, re

directory = 'C:/Users/Abdul-Qawi/Documents/The Code/python/automating-stuff-with-python/Chapter 9/sampleDir'
pattern = input("Enter a regex pattern: ")

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        file = open(file_path, 'r')
        content = file.read()
        matches = re.findall(pattern, content)
        file.close() 

        if matches :
            print(f"Matches found in {file_path}")
        else:
            print ('No matches!')

        