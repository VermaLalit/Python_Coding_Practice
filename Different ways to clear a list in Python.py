#1. using for loop and pop() --> The pop() method removes and returns the item at the specified index. If no index is provided, it removes and returns the last item in the list.

list1 = [1,2,3,4,5]   # time complexcity  O(n^2) and space complexcity O(1)
print(list1)
for i in range(len(list1)):
    list1.pop()
print(list1)

#2. using clear()
list1 = [1,2,3,4,5]    # time complexcity O(1) and space complexcity O(1)
print(list1)
list1.clear()
print(list1)

#3. by reasinning original list with an empty list.
list1 = [1,2,3,4,5]   # time complexcity O(1) and space complexcity O(1)
print(list1)
list1 = []
print(list1)

#4. using list1 *= 0 or by multiplying the list with 0
list1 = [1,2,3,4,5]   # time complexcity O(1) and space complexcity O(1)
print(list1)
list1 *= 0
print(list1)

#5. using del statement
list1 = [1,2,3,4,5]    # time complexcity O(n) and space complexcity O(1)
print(list1)
del list1[:]
print(list1)

#6. using while loop

list1 = [1,2,3,4,5]    # time complexcity O(n^2) and space complexcity O(1)
print(list1)
while list1:
    list1.pop()
print(list1)

#7. using slicing

list1 = [1,2,3,4,5]    # time complexcity O(n) and space complexcity O(n)
print(list1)
list1 = list1[:0]
print(list1)