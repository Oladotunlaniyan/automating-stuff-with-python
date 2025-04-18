# #! python3 
# # mapIt.py - Launches a map in the browser using an address from the 
# #command line or clipboard

# import webbrowser, sys, pyperclip

# if len(sys.argv) > 1:
#     #Get address from command line. 
#     address = ' '.join(sys.argv[1:])
# else:
#     #Get address from clipboard  
#     address = pyperclip.paste()

# webbrowser.open('https://www.google.com/maps/place/' + address)


import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()

# res.status_code == requests.codes.ok

# len(res.text)
# print(res.text[:250])

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()