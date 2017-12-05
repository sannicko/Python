# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
# for num in range (1000):
#     print(num)

for num in range (1000):
    if num % 2 == 1:
     print(num)    


# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for x in range (5,1000000):
    c = x * 5
    print (c)


# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
aTotal = 0
for i in range (len(a)):
    aTotal += a[i]
    print(aTotal)

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
average = sum(a)/len(a)
print average