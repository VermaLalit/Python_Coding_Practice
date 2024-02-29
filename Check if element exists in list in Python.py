# Check if element exists in list in Python

# 1. using in operator and if else statement

list1 = [1,2,3,4,5]
element = 2
if element in list1:
        print(f'Yes given element exists in given list')
else:
        print(f'No given element does not exists in given list')

# 2. using in operator and for loop

list1 = [1,2,3,4,5]
element = 2
for i in list1:
        if i == element:
                print("Yes given element exists in given list")
        else:
                continue
        
# 3. using in operator and range() and for loop

list1 = [1,2,3,4,5]
element = 4
for i in range(len(list1)):
        if list1[i] == element:
                print('Yes given element {0} exists in given list {1}'.format(element,list1))
        else:
                continue

# 4. using while loop

list1 = [1,2,3,4,5]
element = 2
n = len(list1)
i = 0
while n > 0:
        if list1[i] == element:
                print('Yes given element exists in the given list')
                n -= 1
                i += 1
        else:
                n -= 1
                i +=1

# 5. using count()

list1 = [1,2,3,4,5]
element = 3
el_count = list1.count(element)
if el_count > 0 :
        print("Yes given element exists in the given list")
else:
        print('No given element does not exists in the given list')

# 6. using Counter()

from collections import Counter
list1 = [1,2,3,4,5]
element = 2
frequency = Counter(list1)
print(frequency)
if frequency[element] >0:
        print("Yes given element exists in the given list")
else:
        print("given element does not exists in the given list")

# 7. using try except block

def element_found(a,b):
        try:
            a.index(b)
            return True
        except ValueError:
                return False

list1 = [1,2,3,4,5]
element = 1
print(element_found(list1,element))
        