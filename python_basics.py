# variables
x = 7  # 7 is an int data type
y = "7" # 7 is a string 

# casting
z = int(y)   # 7 has been casted as an int

# arithmetic op + - / * 
c = x + z # 14
print(c)  

# to get the type of a variable or object   type()
print(type(c)) #int
print(type(y)) #str

# elements in python are case sensitive a-zA-Z0-9
a = "4"  # sort 4 then sally
b = 4 # sort sally then 4
A = "Sally"
print(a)  #4
print(A)  #sally
print(a)  #4

# variable naming rules
myvar = "philip" # string var
_myvar = "philip"  # hidden string var
#  1_myvar = "philip"   # invalid cannot start with a number
myvar_1 = "philip" # valid contain numbers but not in position 1

# variable names: underscore_case
# Class Names: Title Case
# Field Name: lowercase

# multiple variables at one time
x, y, z = 7, 3, 4
print(x+y+z) #14

a, b = "philip", 21
print( a + " is " + str(b) + " years old.")