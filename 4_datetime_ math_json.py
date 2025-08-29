#======================= datetime =============================
import datetime

x = datetime.datetime.now() # 2025-08-29 19:46:25.637180
print(x) 
print(x.year)
print(x.strftime("%A")) 
print(x.strftime("%B")) 

x = datetime.datetime(2020, 5, 17) #2020-05-17 00:00:00
print(x) 

"""
# https://www.w3schools.com/python/python_datetime.asp
Directive 	                        Description 	                                    Example
%a 	                                Weekday, short version 	                            Wed 	
%A 	                                Weekday, full version 	                            Wednesday 	
%w 	                                Weekday as a number 0-6, 0 is Sunday 	            3 	
%d 	                                Day of month 01-31 	                                31 	
%b 	                                Month name, short version 	                        Dec 	
%B 	                                Month name, full version 	                        December 	
%m 	                                Month as a number 01-12 	                        12 	
%y 	                                Year, short version, without century 	            18 	
%Y 	                                Year, full version 	                                2018 	
%H 	                                Hour 00-23 	                                        17 	
%I 	                                Hour 00-12 	                                        05 	
%p 	                                AM/PM 	                                            PM 	
%M 	                                Minute 00-59 	                                    41 	
%S 	                                Second 00-59 	                                    08 	
%f 	                                Microsecond 000000-999999 	                        548513 	
%z 	                                UTC offset 	                                        +0100 	
%Z 	                                Timezone 	                                        CST 	
%j 	                                Day number of year 001-366                      	365 	
%U 	                    Week number of year, Sunday as the first day of week, 00-53 	52 	
%W 	                    Week number of year, Monday as the first day of week, 00-53 	52 	
%c 	                        Local version of date and time 	Mon Dec 31 17:41:00         2018 	
%C 	                                Century 	                                        20 	
%x 	                                Local version of date 	                            12/31/18 	
%X 	                                Local version of time 	                            17:41:00 	
%% 	                                A % character 	                                    % 	
%G 	                                ISO 8601 year 	                                    2018 	
%u 	                                ISO 8601 weekday                                    (1-7) 	1 	
%V 	                                ISO 8601 weeknumber (01-53) 	                    01


"""
print("%%",x.strftime("%%"))


#======================= math =============================
x = min(5, 10, 25)
y = max(5, 10, 25)
x = abs(-7.25)
x = pow(4, 3)

import math

x = math.sqrt(64)
x = math.ceil(1.4)
y = math.floor(1.4)
math.pi
print(x) 

#======================= json =============================
import json 
# *******************************
# Convert from JSON to Python:
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 
# *******************************
# Convert from Python to JSON:
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y) 
# *******************************
# Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 
"""
# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
Python 	JSON
dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null
"""


# **************************************
# The example  prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
# The json.dumps() method has parameters to make it easier to read the result:
print( json.dumps(x, indent=4))
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print( json.dumps(x, indent=4, sort_keys=True))