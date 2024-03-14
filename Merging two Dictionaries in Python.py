#1. using update()  --> By using the method update() in Python,
#  one list can be merged into another. But in this, the second list is
# merged into the first list and no new list is created. It returns None. 

dict1 = {"a":1,"b":2,"c":3,"d":4}    # time complexity O(1) and space complexity O(1)
dict2 = {"e":5,"f":6,"g":7,"h":8}
dict1.update(dict2)
print(dict1)

#2. using merge operator (|)

def merge_dicts(a,b):         # time complexity O(1) and space complexity O(n)
    dict3 = a | b
    return dict3
dict1 = {"a":1,"b":2,"c":3,"d":4}
dict2 = {"e":5,"f":6,"g":7,"h":8}
print(merge_dicts(dict1,dict2))

#3. using for loop and keys()

dict1 = {"a":1,"b":2,"c":3,"d":4}    # time complexity O(n + ) and space complexity O(n)
dict2 = {"e":5,"f":6,"g":7,"h":8}
for i in dict2.keys():
    dict1[i] = dict2[i]
print(dict1)

#4. using unpack operator

def Merge(dict1, dict2):
	res = {**dict1, **dict2}
	return res
	
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

#5. Merge Two Dictionaries in Python Using dict constructor.

def merg_dict(dict1,dict2):
     merged_dict = dict1.copy()
     merged_dict.update(dict2)
     return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
print(merg_dict(dict1,dict2))
