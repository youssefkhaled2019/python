"""
What is OOP?
    OOP stands for Object-Oriented Programming.
    Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

Advantages of OOP
    Provides a clear structure to programs
    Makes code easier to maintain, reuse, and debug
    Helps keep your code DRY (Don't Repeat Yourself)
    Allows you to build reusable applications with less code

"""


# ========================= Classes/Objects =========================
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    #  mysillyobject.name = name
    # mysillyobject.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
print(p1) 
print(p1.myfunc())

p1.age = 40 #You can modify properties 
del p1.age 
del p1 

class Person:
  pass

# ========================= Inheritance=========================

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname() 

class Student(Person):
  pass  # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Student("Mike", "Olsen")
x.printname() 
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

class Student(Person):
  def __init__(self, fname, lname):
    pass
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)   
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:csda.r
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019 

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
#   def printname(self):
#     print("2-",self.firstname, self.lastname)    

x = Student("Mike", "Olsen", 2019) 



# ========================= Iterators =========================

"""
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
"""

# [Iterator] vs [Iterable]
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

# Iterator
# ***********
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
# ***********
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# ***********
# We can also use a for loop to iterate through an iterable object:
# The for loop actually creates an iterator object and executes the next() method for each loop.
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x) 

mystr = "banana"
for x in mystr:
  print(x) 
# ***********  
"""
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""
# Create an Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

# StopIteration
"""
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
To prevent the iteration from going on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
"""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# ========================= Polymorphism =========================
"""
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
"""

x = "Hello World!"
x = ("apple", "banana", "cherry")
x  =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(x)) 

"""
Class Polymorphism
    Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
    For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
"""
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()



"""
Inheritance Class Polymorphism
What about classes with child classes with the same name? Can we use polymorphism there?
Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

"""  
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

"""
Child classes inherits the properties and methods from the parent class.
In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
Because of polymorphism we can execute the same method for all classes.
"""