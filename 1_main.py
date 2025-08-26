
x = 200
print(isinstance(x, int))  #return a boolean
# print(type(x)==int)
a,b,c=map(int,input().split(" "))
# --------------------------------------
#This is a comment
"""
This is a comment
written in
more than just one line
"""
# --------------------------------------
# >>> python --version
# python hello.py 
# !pip --version 
# --------------------------------------
import sys
print(sys.version)


# import platform
# x = platform.system()
# x = dir(platform)
# print(x) 

# ------------------[Variables]--------------------
x = 4       # x is of type int

x = 35e3
y = 12E4
z = -87.7e100

x = 3+5j
y = 5j
z = -5j

x = "Sally" # x is now of type str

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 


print(type(x))



# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	    NoneType


x = "Hello World" 	                            #str 	
x = 20 	                                        #int 	
x = 20.5 	                                    #float 	
x = 1j            #3+5j               	        #complex 	 #c.real ,c.imag 
x = ["apple", "banana", "cherry"] 	            #list 	
x = ("apple", "banana", "cherry") 	            #tuple 	
x = range(6) 	                                #range 	
x = {"name" : "John", "age" : 36} 	            #dict 	
x = {"apple", "banana", "cherry"} 	            #set 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	
x = True 	                                    #bool 	
x = b"Hello" 	                                #bytes 	
x = bytearray(5) 	                            #bytearray 	
x = memoryview(bytes(5)) 	                    #memoryview 	
x = None 	                                    #NoneType
# z = -87.7e100   # 35e3 12E4
# ---------------------
x = str("Hello World")                         	#str 	
x = int(20) 	                                #int 	
x = float(20.5) 	                            #float 	
x = complex(1j) 	                            #complex 	
x = list(("apple", "banana", "cherry")) 	    #list 	
x = tuple(("apple", "banana", "cherry"))    	#tuple 	
x = range(6) 	                                #range 	
x = dict(name="John", age=36)               	#dict 	
x = set(("apple", "banana", "cherry")) 	        #set 	
x = frozenset(("apple", "banana", "cherry")) 	#frozenset 	
x = bool(5)                                 	#bool 	
x = bytes(5)                                	#bytes 	
x = bytearray(5)                            	#bytearray 	
x = memoryview(bytes(5)) 	                    #memoryview
# --------------------------------------
# Camel Case        Each word, except the first, starts with a capital letter:
myVariableName = "John" 
# Pascal Case       Each word starts with a capital letter:
MyVariableName = "John" 
# Snake Case        Each word is separated by an underscore character:
my_variable_name = "John" 


# --------------------------------------
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

x = 5
y = "John"
print(x, y)  #print(x + y)  error

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 
bool()
complex()
type(x)
# -------------------bool-------------------
#  True , False
print(10 > 9)
print(10 == 9)
print(10 < 9) 

# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False: 
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) 



# ------------------global--------------------

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 
# -------------------random-------------------

import random
print(random.random()) #between 0-1 size one element float
print(random.randint(1,20)) #between a-1b size one element int
print(random.uniform(1,20))#between a-1b size one element float

print(random.randrange(10)) 
print(random.randrange(1, 10))  #randrange(start, stop=None, step=1) size one element  int  EX: randrange(0,20,2) retutn even
print(random.randrange(0,20,2))

print(random.choice(['a','b','c']))#choice('sweet home alabama')# get one elment
 
print(random.sample(range(200) ,10))#print 10 utem reandon integer

items = [1,2,3,4,5,6]
random.shuffle(items)#Shuffle list x in place, and return None.
print(items)#[3, 6, 1, 5, 4, 2]
# ------------------if-else--------------------
# a == b   a != b
# and  ,or , not a > b
# Note:  a != b  ,and,or,not,, and == &    ,, or== |            Continue   break  is None ,is not None

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b") 
# if a > b and c > a:print("Both conditions are True")
# if a > b or a > c:print("At least one of the conditions is True")
# if not a > b:print("a is NOT greater than b")

print("A") if a > b else print("B") 

print("A") if a > b else print("=") if a == b else print("B") 

if b > a:
  pass
# **************************
15 < a < 30 

x=None
if x is None:
    print("None")
elif x is not None:
    print("not None")

x=5
y=7
if (x==2) & (y==3):#and
    print("None")
elif (x==2) | (y==3):#or
    print("not None")


# ------------------match--------------------
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _: #Default Value Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
    print("Looking forward to the Weekend")


day = 4
match day:
  case 1 | 2 | 3 | 4 | 5: #Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")




month = 5
day = 4
match day: #You can add if statements in the case evaluation as an extra condition-check:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")



# ----------------while ----------------------
# break continue
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



# i = 1
# while i < 6:
#   print(i)
#   if i == 2:
#     print(i)
#     continue
#   if i == 3:
#     print(i)
#     break
#   i += 1 
# else:
#   print("i is no longer less than 6")  

# --------------------for------------------
# break continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) 

for x in range(2, 30, 3):
  print(x)  
else:
  print("Finally finished!")   


# for x in fruits:
#   if x == "banana":
#     break
#   if x == "apple":
#     continue
#   print(x)



for x in [0, 1, 2]:
  pass  



# print(sum([k for k in range(20)]))
# newlist = [ x**3 for x in range(12)]
#           [3*x for x in [y**2 for y in range(10)]]
# newlist = [x for x in fruits if "a" in x]
# newlist = [x for x in fruits if x != "apple"]   #??
# newlist  = [i for i in range(20) if i%3 ==0  and i %2 ==0 ]
# newlist = [[0 for i in range(5)] for j in range(7)]
# newlist = [x if x != "banana" else "orange" for x in fruits]  #??
# newlist = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]



# grades  = {"ahmed":35 ,"mona":40 ,"mena":37 }
# for a in grades : print(a)# output -> ahmed  mona mena
# for a in grades.items() : print(a)# output -> ('ahmed', 35) ,('mona', 40),('mena', 37)
# for a,b in grades.items() : 
# for a in grades.keys() : 
# for a in grades.values() : 
#-------------------------------
# for index,val in enumerate(grades,3) : 
#-------------------------------
# students =  ["ahmed","ramy","ramy","mena"]
# grades = [25,33,66,95,444]
# for i,a in zip(students,grades) : 
#  print("student" + i + " got " + str(a) + "degree"  )

#--------------------- [public function] ---------------------

# #dir(m) for show all premter and verible  import math as m 
# sorted
# list(reversed([1,23]))
# del #delete
# chr(10) #\n
# bin(3) #0b11
# oct(8)#001000 => [001][000]
# ord('a')#97
# abs(-20)  #20
# divmod(102,2) #(51, 0)
# pow(2,3) #8
# min(5, 10, 25)
# max(5, 10, 25)
# round(1.25) #1
# -----------------Functions---------------------
# **************************
def my_function(country = "Norway"):
  print(country + " Refsnes")
my_function("Emil")
my_function()
# **************************
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") 
# **************************
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 
# **************************
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes") 
# **************************
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
# **************************
def myfunction():
  pass
# **************************
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)
my_function(3) 
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)
my_function(x = 3)
# But when adding the , / you will get an error if you try to send a keyword argument:
def my_function(x, /): #ERROR
  print(x)
my_function(x = 3) 
# **************************
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)
my_function(x = 3) 
# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)
my_function(3) 
# But with the *, you will get an error if you try to send a positional argument:
def my_function(*, x):#ERROR
  print(x)
my_function(3) 
# **************************
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8) 
# **************************

# ----------------Recursion----------------------
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
# ----------------lambda ----------------------
# note:Use lambda functions when an anonymous function is required for a short period of time.

x = lambda a : a + 10
print(x(5)) 
# **************************
x = lambda a, b : a * b
print(x(5, 6)) 
# **************************
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 
# **************************
# Why Use Lambda Functions?
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
# **************************
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# ------------------ try-except---------------------
# IOError , ValueError , ImportError , EOFError , KeyboadInterrupt

try:
  print(x)
except:
  print("An exception occurred") 
# **************************
try:
  print(x)
except NameError: #NameError and another for other errors
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# **************************

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except ZeroDivisionError as err:
    print("Error message is:", err)  
except:
  print("Something else went wrong")   
finally : 
    print ("end")

# **************************
try:
  print("Hello")
except:
  print("Something went wrong")
else: #You can use the else keyword to define a block of code to be executed if no errors were raised:
  print("Nothing went wrong")
# **************************
try:
  print(x)
except:
  print("Something went wrong")
finally:#The finally block, if specified, will be executed regardless if the try block raises an error or not.
  print("The 'try except' is finished") 
# **************************

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")  
finally:                                     #The finally block, if specified, will be executed regardless if the try block raises an error or not.
  print("The 'try except' is finished")  


# **************************
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 
# **************************
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed") 

try:
  raise Exception("Sorry, no numbers below zero")  #??  
except:
  print("Something went wrong")
# **************************





# -----------------string---------------------
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_strings_methods.asp
# https://www.w3schools.com/python/python_string_formatting.asp
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

a = "Hello, World!"
print(a[1])

txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 
print(a.replace("H", "J")) 
print(a.split(",")) # returns ['Hello', ' World!'] 



txt = "We are the so-called \"Vikings\" from the north." 
# \' 	  Single Quote 	
# \\  	Backslash 	
# \n 	  New Line 	
# \r 	  Carriage Return 	
# \t  	Tab 	
# \b  	Backspace 	
# \f 	  Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value

price = 36,tax = 0.25,fruit = "apples"
def myconverter(x):
  return x * 0.3048
txt = f"My name is John, I am {price}"
txt = f"The price is {price:.2f} dollars"
txt = f"The price is {20 * 59} dollars" 
txt = f"The price is {price + (price * tax)} dollars" 
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
txt = f"I love {fruit.upper()}"
txt = f"The plane is flying at a {myconverter(30000)} meter altitude" 
# **************************
txt = f"The price is {price:,} dollars" 

# :< 	  Left aligns the result (within the available space)
# :> 	  Right aligns the result (within the available space)
# :^ 	  Center aligns the result (within the available space)
# := 	  Places the sign to the left most position
# :+ 	  Use a plus sign to indicate if the result is positive or negative
# :- 	  Use a minus sign for negative values only
# :  	  Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :, 	  Use a comma as a thousand separator
# :_ 	  Use a underscore as a thousand separator
# :b 	  Binary format
# :c 		Converts the value into the corresponding Unicode character
# :d 	  Decimal format
# :e 	  Scientific format, with a lower case e
# :E 	  Scientific format, with an upper case E
# :f 	  Fix point number format
# :F 	  Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g 		General format
# :G 		General format (using a upper case E for scientific notations)
# :o 	  Octal format
# :x 	  Hex format, lower case
# :X 	  Hex format, upper case
# :n 		Number format
# :% 	  Percentage format
# **************************
txt = "The price is {} dollars"
print(txt.format(price))
quantity = 3,itemno = 567,price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
txt = "His name is {1}. {1} is {0} years old."
print(myorder.format(quantity, itemno, price))
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
# **************************

"%s %f %d"%('ddddd',22.2,202255)




# -----------------input---------------------
a,b,c=map(int,input().split(" "))
# **************************
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!") 
# --------------------------------------
