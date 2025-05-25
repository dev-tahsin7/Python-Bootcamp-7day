# Syntax
# variable_name = open("filename", "mood")

# file creation:
first_file = open("text.txt", "x")

# Appending
with open("text.txt", "a") as x:
    x.write("Hello World!")

with open("text.txt", "a") as y:
    y.write("I am your boss!")

# Writing:
with open("text.txt", "w") as a:
    a.write("Overwrite")

# Read
read_variable = open("text.txt")
print(read_variable.read())

"""
import os 
os.remove("filename") >> to remove/ delete the file
"""
