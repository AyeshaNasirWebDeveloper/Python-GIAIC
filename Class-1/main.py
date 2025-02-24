#py --version
#python --version
#python3 --version

# These are the commands to run the code or Simply click on run buttono

# Variables
name = "Ayesha Nasir"
age = 1
print(name , age)

sentence = "Hello World"
print(sentence.upper())
print("Hello Everyone by String")

#Variables with types
instituteName : str = "Governor Initiative for Artificial Intelligence and Computing"
print("GIAIC stands for:", instituteName)

# function
def mainFunc():
    print("Hello World from Ayesha Nasir")

var_str = "Hello There!"
print(var_str)    

############################################    Data Types    ######################################################

# Multi Line String 
#String
id_card:str = """
Name : Ayesha Nasir
Father Name: M.Nasir
Age: 20
"""
print(id_card)

#Integer
num: int = 32
print(num)

#Float
floatNum : float = 5.5
print(floatNum)

#Boolean
isTrue: bool = True
isFalse: bool = False
print(isTrue)
print(isFalse)

#List : in the form of Array
# POstive & Negative Indexding
fruit: list[str] = [
    "apple", "banana"
] 
print(type(fruit))
print(fruit)
#Positive Indexing
print(fruit[0])
# Nagative Indexing
print(fruit[-1])

#Tuple is Immuttable Data type
tupleData:tuple=["apple", "cherry"]
print(tupleData)
print(tupleData[0])
print(tupleData[1])
print(tupleData[-1])

#Dictionary is the form of Object
user_data : dict[str, str] = {
    "name": "Ayesha",
    "Father Name": "M.Nasir"
}

# None
fullName:None = None
print(fullName)


#Condional Statement
if age >= 18:
    print("You are Eligible!")
elif age >= 6: 
    print("You are not Eligible!")
else: print("You are Under Age")