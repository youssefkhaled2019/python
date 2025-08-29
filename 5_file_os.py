"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists




"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

# Note: Make sure the file exists, or else you will get an error.

f = open("demofile.txt", "rt")


# ************read***************
f = open("demofile.txt")
print(f.read()) 
print(f.readline())
f.close() 

with open("demofile.txt") as f:
  print(f.read()) 
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# print(f.read(5)) 

with open("demofile.txt") as f:
  for x in f:
    print(x) 
# **********write / append*****************    
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
# ************rmove***************    

import os
os.remove("demofile.txt") 


# Check if File exist:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 

# To delete an entire folder, 
# Note: You can only remove empty folders.
os.rmdir("myfolder") 
