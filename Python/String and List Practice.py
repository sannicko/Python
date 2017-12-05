# sample .find() function:
string = "a,b,c,d"
print string.find ("d")

# sample .replace() function:
sentence = "Today is Tuesday, a good day to be happy"
sentence = sentence.replace("Tuesday", "Friday")
print sentence

# sample min and max
z = [1000000,10,99999999,100,100000,1000,10000]
print z
print min(z)
print max(z)

# sample first and last
z = [2,4,6,8,10,12,"Day"]
print z [0], z[len(z)-1]

array = "It is a heavy object","actual", "blue",[2,3,4]
print array [0], array[len(array)-1]
print len (array)

# sample new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print sorted (x)
x.sort()
print x
listone = x[:len(x)/2]
print "list one", listone
listtwo = x[len(x)/2:]
print "list two", listtwo
listtwo.insert(0,listone)
print listtwo

