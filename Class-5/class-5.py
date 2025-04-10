from typing import Union
# union for type
types = Union[int,float,str]
list_items:list[types] = [1, 2, "4", "6", 5.7]

# empty set
new_set: set = set()
 
#  built in modules
#  for getting random numbers
import random
print(random.randint(1,10))

# user defined OR Customer modules
# importing adding module file
import add
# calling the function
add.add(5, 7)

from add import addition
addition()

# its a third party modules
# for APIs
import requests as req
response = req.get("api_link")
print(response.json())

