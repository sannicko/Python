student = {'name': 'Nickolas', 'age': 3000, 'country of birth': 'Colombia', 'language': 'Python' }
def dictionary_values(dic):
    for key, value in dic.iteritems():
        print "My" + " " + key + " " + "is" + " " + str(value)
print dictionary_values(student)