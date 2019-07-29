# Dictionay consists of keys and value. Every key is unique and every key is used to access the value associated with it.

dic = {'I': 'am Joker', 'Goku': 'is the strongest', 'Naruto': 'is a Ninja', 'Python': 'is a snake. :P'}

print(dic)
print(dic['Python'])

for key,value in dic.items():
    print(key, value)



'''
Some methods of Dictionary are as follows
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and values
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''