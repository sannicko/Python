import random
def coin(tosses):
    print "Starting the program..."
    for i in range (0,tosses):
        toss = random.randint(0, 1)
    if toss == 1:
        print "Got", toss , ".... It's a head!"
    else:
        print "Got", toss , ".... It's a tail!"
    print "Ending the program, thank you!"
coin(1)
