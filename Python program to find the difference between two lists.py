#1. Using set operations
list1 = [1,2,3,4,5]
list2 = [4,5,67,78]
set1 = set(list1)
set2 = set(list2)
print(list(set1-set2))

#2. using for loop and in operator
list1 = [1,2,3,4,5]
list2 = [4,5,67,78]
list3 = []
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)

#3. using list comprehension
list1 = [1,2,3,4,5]
list2 = [4,5,67,78]
list3 = [i for i in list1 if i not in list2]
print(list3)
