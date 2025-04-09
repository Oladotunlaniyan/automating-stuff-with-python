import re, os

input_file = open('./madlibs_input.txt', 'r')
content = input_file.read()
input_file.close()

placeholders = re.findall(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b', content)

for word in placeholders: 
    replacement = input(f"Enter a {word.lower()}: ")
    content = content.replace(word, replacement, 1)

print("\n Here is your Mad Libs result:\n")
print(content)

output_file = open('mad_libs.txt', 'w')
output_file.write(content)
output_file.close()

print("\nYour Mad Libs story has been saved to 'madlibs_result.txt'.")