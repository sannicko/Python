# bool
int
str
float
#pass by value
myValue = 5
mySecondValue = myValue
myValue = 10
myNonWholeNumber = 10.5
myTrue = False
x = "abcd"
dict
list
tuple
#pass by reference
tree = {
	"color_of_leaves":"green",
	"age": 10
}
print tree["color_of_leaves"]
copy_of_tree = tree
tree["age"] = 15
print copy_of_tree
#			0		1		2		3
# myList = ("Minh", "AJ", "Chris", "Ghezal")
# myList[1] = "Anthony"
myList = ["Minh", "AJ", "Chris", "Ghezal"]
(myList[0], myList[1]) = (myList[1], myList[0])
x = 5
print len(myList)
def instruction1(name1, name2="Minh", name3):
	print name1
	print name2
	print name3
instruction1()