"""
List items are ordered, changeable, and allow duplicate values.
the first item has index [0]

 Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value
"""
# https://www.w3schools.com/python/python_lists_methods.asp

thislist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets


# ******** Access Items ********
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # -1 ,[2:5]

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
# ******** add Item ********
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")

thislist.append("orange")

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #you can add any iterable object (tuples, sets, dictionaries etc.).

# ******** Change Item ********
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant", "watermelon"]
# ******** remove Item ********
thislist.remove("banana") #If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist.pop(1)  #If you do not specify the index, the pop() method removes the last item.
del thislist[0]
del thislist 
thislist.clear()
"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
        *Set items are unchangeable, but you can remove and/or add items whenever you like.
     Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
# ******** Loop Through a List  ********
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

for i in range(len(thislist)):
  print(thislist[i]) 

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1  

[print(x) for x in thislist] 
[x for x in thislist]
newlist = [x for x in thislist if "a" in x]
newlist = [x for x in thislist if x != "apple"] 
newlist = [x if x != "banana" else "orange" for x in thislist] 

# ******** sort  ********
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist = [100, 50, 65, 82, 23]
thislist.sort()
thislist.sort(reverse = True)
thislist.reverse()
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

# method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

# ******** copy  ********
mylist = thislist.copy()

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)

mylist = thislist[:]


# ******** Join Two Lists  ********
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

for x in list2:
  list1.append(x)

list1.extend(list2)  

# ******** Methods  ********
fruits = ['apple', 'banana', 'cherry']
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count("cherry")
x = points.count(9)

x = fruits.index("cherry") 




