# import traceback

# try: 
#     raise Exception('This is the error message')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt')

# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# print(ages)
# assert ages[0] <= ages[-1]


# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}

# def switchLights(stoplight):

#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'
#         assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

# switchLights(mission_16th)


import logging

logging.basicConfig(level=logging.DEBUG, format =' %(asctime)s - %(levelname)s - %(message)s')

