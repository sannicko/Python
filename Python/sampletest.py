dog = ("Canis Familiaris", "dog", "carnivore", 12)
print dog[2]
print dog [0]
print dog
for data in dog:
    print data
dog = dog + ("domestic",)
print dog
dog = dog[:3] + ("man's best friend",) + dog[4:] #Deleting one item and replacing it with other. Slice.
print dog
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 1 * math.pi * r
    a = math.pi * r * r
    return (c, a)
print get_circle_area
# import language
# print language.translate(dog)

# DICTIONARIES
weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation

capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print weekend["Sun"]
print capitals["svk"]

# for loop to access all keys and values in a dictonary:
#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data

# Nested Dictionaries
context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }
for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"

#Lists from Dictionary
#It's possible to create lists from dictionaries by using the methods items(), keys() and values(). As the name implies the method keys() creates a list, which consists solely of the keys of the dictionary. While values() produces a list consisting of the values. items() can be used to create a list consisting of 2-tuples of (key, value)-pairs:
data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
#['house', 'red', 'cat']
print data.values()
#['Haus', 'rot', 'Katze']

#Dictionaries from Lists
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_specialities = zip(countries, dishes)
print country_specialities

#Converting a variable into a real dictionary with the function dict()

country_specialities_dict = dict(country_specialities)
print country_specialities_dict





