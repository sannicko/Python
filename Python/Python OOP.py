class User(object):
    name = "Anna"
anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
user2 = User("Rick Propas", "rick@rick.com")
print user1.name
print user1.logged
print user1.email
print user2.name
print user2.logged
print user2.email

class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
user1 = User("Anna Propas", "anna@anna.com")
user2 = User("Rick Propas", "rick@rick.com")
print user1.name
print user1.logged
print user1.email
print user2.name
print user2.logged
print user2.email