# Understanding Data Types

text:str = "Hello World"
numbers: int = 10
decimal_value: float = 10.5
boolean: bool = True
collection_of_data: list[int] = [1,2,3,4,5]  # Positive & Negative Indexing
immutable_collection_of_data: tuple[int, str,float] = (1,"Hello Dear!", 3.14) # It is immutable
object_data: dict [str, [str, int]] = {"name": "Ayesha Nasir", "age": 19} #It is in the object form Key and Value pairs
print(object_data["name"]) 
unique_values: set[int] = {1,1,12,33,45,55,2,3,3} # Its returns unordered/ordered data and remove duplications #Mutable
print(unique_values)
unique_value: frozenset[int] = {1,1,12,33,45,55,2,3,3} # Its returns unordered/ordered data and remove duplications #Immutable
print(unique_value)
numbers_list:list[int] = range(1,20) # it is usually used in the loops 
print(numbers_list) #returns 1 to 20

for num in range(1,20):
    list_of_numbers: list[int] = []
    list_of_numbers.append(num)
    print(list_of_numbers) #returns 1 to 19 because it is in the loop

# byte_data
#  Open an image file in binary mode
# with keyword is used for resource management file ki jitni files hai usko programmetically 
# open take 2 parameters 
# with open("image.jpg", "rb") as source_file:
#     data = source_file.read()

# # 
# with open("image.jpg", "rb") as target_file:
#     data = target_file

#ASCII Values
print(chr(65)) #A
print(chr(99)) #C

#ID
a= 6
b = a
print(id(a))
print(id(b))
b = 7
print(id(b))

#Type Casting
#Default type is Str
c = 8 # Implicit Casting
print(type(c)) #int 
c = str(c) #Explicit Casting
print(type(c)) #str

d:int= 5
if type(d) == int:
    print("d is integer")
else:
    print("d is not integer")

# Best Practice
# isinstance  type check krta hai
# Takes two parameters
# kya comapre krna hai?
# kis say compare krna hai?
# it returns True / False
# by default type bhi check krta hai
f:int = 8
print(isinstance(f,int)) #True
print(isinstance(f, str)) #False
print(isinstance(f, float)) #False 

#Operators
#Arithmetic Operators
# +
# -
# *
# / 
# %  Returns Remainder 
# // (floor division) Number ko round kr k nichay wala dega decial khatam krdega
# ** Exponenciation 
# 2 **3 = 2 x 2 x 2 =8

#Comparison Operator
# == Equal to type and value both check krta hai
# != Not Equal to
# > Greater than
# < Less than
# >= Greater than or Equal to
# <= Less than or Equal to

# Logical Operator
# not operator Value Reverse
# and operator Value True if both values are True
# or operator Value True if any of the values are True

# Assignment Operator
# = Value assign krta hai
# += Add and assign
# -= Subtract and assign

# Identity Operator
# is operator Value check krta hai
# is not 
a = True
print(a is True)

# MemberShip Operator
# in operator check krta hai k 
names: list[str]= ["Ayesha", "Nasir", "Mehmoona"]
result = "Ayesha" in names
result1 = "Ayesha" in names
print(result) #True
print(result1) #False

# Line continuation (`\`) allows printing a statement over multiple lines, improving code readability without breaking the string.
# print("The list of \
# keywords is : ")

# printing all keywords at once using "kwlist()" 
# print(keyword.kwlist) #39 Keywords

#nagtive Operator
# x = 5
# y = -x  # y is now -5
# print("y = ", y)

# Zipping Method
x , y , z = 2, 3.5, "Ayesha"
print(x,y,z) #2 3.5 Ayesha
# x:int, y:float, z:str
# print(x,y,z) #TypeError: 'str' object is not iterable