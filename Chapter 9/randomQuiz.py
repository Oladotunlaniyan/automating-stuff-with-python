#! python3

#randomQuizGenerator.py - Creates quizzes with questions and answers in
#random order, along with the answer key 

import random

#The quiz data. Keys are states and values are their capitals.

capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoeni', 
             'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

for quizNum in range(35):
    #Create the quiz and answer key files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w') 
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    
    #Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    #Shuffle the order of the states. 
    states = list(capitals.keys())
    random.shuffle(states)
    
    #Loop through all 50 states, making a question for each
    for questionNum in range(50):

        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}.{  answerOptions[i]}\n")
        
        quizFile.write('\n')

        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")

    quizFile.close()
    answerKeyFile.close()