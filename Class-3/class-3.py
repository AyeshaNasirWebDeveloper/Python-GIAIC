# Strings

# Single Quotes
roll_no='12345'
print(roll_no)
print(type(roll_no))

# Double Quotes
name="Ayesha"
print(name)
print(type(name))

# Triple Quotes / Multiline Strings
description=""" 
This is a long description
that can span multiple lines.
"""
print(description)
print(type(description))

# String Concatenation
name="Ayesha"
age=20
greeting="Hello, my name is " + name + " and I am " + str(age) + " years old."
print(greeting)

# String Formatting
name="Ayesha"
age=17
greetings=f"Hello Everone! my name is {name} and I am {age} years old."
print(greetings)

# String Repetition
# \n is used for new/next line
repeat_string="Hello World! \n" * 3
print(repeat_string)

# Escape Sequence Characters in Python
# Escape sequences are used to insert characters that are illegal in a string.

# \n is used for new/next line
# \t is used for tab space
# \\ is used for backslash
# \' is used for single quote
# \" is used for double quote
# \r is used for carriage return
# \b is used for backspace
# \f is used for form feed
# \a is used for bell/alert
# \v is used for vertical tab
# \ooo is used for octal value
# \xhh is used for hexadecimal value
# \N{name} is used for Unicode character
# \Uxxxxxxxx is used for Unicode character
# \uXXXX is used for Unicode character
print("Hello World! \nThis is a new line.")
print("Hello World! \tThis is a tab space.")
print("Hello World! \\ This is a backslash.")
print("Hello World! \' This is a single quote.")
print("Hello World! \" This is a double quote.")
print("Hello World! \r This is a carriage return.")
print("Hello World! \b This is a backspace.")
print("Hello World! \f This is a form feed.")
# print("Hello World! \a This is a bell/alert.")
# print("Hello World! \v This is a vertical tab.")
# print("Hello World! \ooo This is an octal value.")
# print("Hello World! \xhh This is a hexadecimal value.")
# print("Hello World! \N{name} This is a Unicode character.")
# print("Hello World! \Uxxxxxxxx This is a Unicode character.")
# print("Hello World! \uXXXX This is a Unicode character.")

# Example of escape sequence
escape_sequence="Hello World! \n\tThis is a tab space. \\ Backslash"
print(escape_sequence)

# String Type Casting
age:int=20
height:float=5.2
name:str="Ayesha"
print("My name is " + name + "and I am " + str(age) + " years old and my height is " + str(height) + " feet.")

# formatting using format() method
# format() method is used to format the string.
print("My name is {} and I am {} years old and my height is {} feet.".format(name, age, height))
# using index in format() method
print("My name is {0} and I am {1} years old and my height is {2} feet.".format(name, age, height))

# fstrings (f-strings) are used to format the string.
# f-strings are used to format the string.
print(f"My name is {name} and I am {age} years old and my height is {height} feet.")

# %s	String	"Hello, %s" % "Alice" → "Hello, Alice"
# %d	Integer (Decimal)	"Age: %d" % 25 → "Age: 25"
# %c	Character	"Letter: %c" % 'A' → "Letter: A"
# %f	Floating-point	"Pi: %f" % 3.14159 → "Pi: 3.141590"
# %.nf	Floating-point with n decimal places	"%.2f" % 3.14159 → "3.14"
print("My name is %s and I am %d years old and my height is %.2f feet." % (name, age, height))

# % operator is used for string formatting.
name: str = 'John'
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000 # 70.536000

#uncomment to see type
#print(type((name, first_letter, age, my_weight)))

# using % operator
my_string: str = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.''' % (name, first_letter, age, my_weight)
print(my_string)

my_string = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %.2f Kg.''' % (name, first_letter, age, my_weight) # Dont forget period %.2f
print(my_string)

# indexing
# String indexing is used to access the individual characters of a string.
# In Python, indexing starts from 0.
# Positive indexing starts from 0 to n-1, where n is the length of the string.
# Negative indexing starts from -1 to -n, where n is the length of the string.


# Positive indexing
# 0 1 2 3 4 5 6 7 8 9 10
# H e l l o   W o r l d !
# Example of positive indexing
string="Hello World!"
print(string[0]) # H
print(string[1]) # e
print(string[11]) # !

# Negative indexing
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# H e l l o   W o r l d !
# Example of negative indexing
print(string[-1]) # !
print(string[-2]) # d
print(string[-11]) # H

print(string[-12]) # IndexError: string index out of range
print(string[12]) # IndexError: string index out of range
print(string[0:5]) # Hello
print(string[6:11]) # World
print(string[0:]) # Hello World!
print(string[:5]) # Hello
print(string[6:]) # World!
print(string[:]) # Hello World!
print(string[::]) # Hello World!
print(string[::2]) # Hlo ol!d
print(string[::3]) # Hoo!
print(string[::-1]) # !dlroW olleH
print(string[::-2]) # !lo olH
print(string[::-3]) # !l oH
print(string[::-4]) # !oH

# String Methods
# String methods are used to perform operations on strings.
# String methods are case-sensitive.

# length of string
# len() function is used to get the length of a string.
print(len(string)) # 12

# count() function is used to count the number of occurrences of a substring in a string.
# count() function is case-sensitive.
print(string.count("o")) # 2

# Upper() function is used to convert a string to uppercase.
print(string.upper()) # HELLO WORLD!

# Lower() function is used to convert a string to lowercase.
print(string.lower()) # hello world!

# Swapcase() function is used to convert a string to swapcase.
# Swapcase means to convert uppercase letters to lowercase and lowercase letters to uppercase.
print(string.swapcase()) # hELLO wORLD!
new_string="Hello World!"
print(new_string.capitalize()) # Hello world!
print(new_string.title()) # Hello World!
print(new_string.swapcase()) # hELLO wORLD!
print(new_string.strip()) # Hello World!
print(new_string.lstrip()) # Hello World!
print(new_string.rstrip()) # Hello World!
print(new_string.replace("Hello", "Hi")) # Hi World!
print(new_string.split()) # ['Hello', 'World!']
print(new_string.split("o")) # ['Hell', ' W', 'rld!']
print(new_string.split("o", 1)) # ['Hell', ' World!']
print(new_string.split("o", 2)) # ['Hell', ' W', 'rld!']
print(new_string.join(["Ayesha", "Nasir"])) # AyeshaHello World!Nasir
print(new_string.find("o")) # 4
print(new_string.find("o", 5)) # 7
print(new_string.find("o", 8)) # -1
print(new_string.index("o")) # 4
print(new_string.index("o", 5)) # 7
print(new_string.index("o", 8)) # ValueError: substring not found
print(new_string.rfind("o")) # 7
print(new_string.rfind("o", 5)) # 7
print(new_string.rfind("o", 8)) # -1
print(new_string.rindex("o")) # 7
print(new_string.rindex("o", 5)) # 7
print(new_string.rindex("o", 8)) # ValueError: substring not found
print(new_string.startswith("Hello")) # True
print(new_string.startswith("World")) # False
print(new_string.endswith("!")) # True
print(new_string.endswith("World")) # False
print(new_string.endswith("World!")) # True
print(new_string.endswith("Hello")) # False
print(new_string.endswith("Hello World!")) # True
print(new_string.endswith("Hello World")) # False

my_string: str = 'Hello! World'

# split into a list of words
words: str = my_string.split()
print("my_string.split()    = ", words)

words = my_string.split(" ") # Space as a delimiter
print('my_string.split(" ") = ',words)

words = my_string.split("l") # Splitting using 'l' as the delimiter
print('my_string.split("l") = ', words)


