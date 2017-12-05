import random
# testing the random module
# value = random.randint(1, 6)
# print(value)

# greetings = ['Hello', 'Hi', 'Hola', 'Ciao', 'Howdy']
# value = random.choice(greetings)
# print(value + ', Nick!')
def grade(scores):
    print "Scores and Grades"
    for i in range (0, scores):
        score = random.randint(60, 101)
        if score >= 60 and score <=69:
         print "score:", score, "; Your grade is D"
        elif score >= 70 and score <=79:
            print "score:", score, "; Your grade is C"
        elif score >= 80 and score <=89:
            print "score:", score, "; Your grade is B"
        elif score >= 90 and score <=100:
            print "score:", score, "; Your grade is A"
    print "END of the program. Bye!"
grade(15)