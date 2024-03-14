#1. Access each element in a list in Python using a Loop And Tuple Unpacking
original_list_of_tuples = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]   # Time Complexity: O(n) and Space Complexity : O(1)
new_val = 5
for i in range(len(original_list_of_tuples)):
    x,y,z = original_list_of_tuples[i]
    original_list_of_tuples[i] = (new_val,y,z)
print(original_list_of_tuples)

#2. Update List in Python using For Loop

def updated_list_of_tuples(original_list_of_tuples,index,value):
    new_list = []
    for tup in original_list_of_tuples:
        temp_list = list(tup)
        temp_list[index] = value
        new_tuple = tuple(temp_list)
        new_list.append(new_tuple)
    return new_list
original_list_of_tuples = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]  # Time Complexity: O(n) and Space Complexity : O(n)
index = 1
value = 5
print(updated_list_of_tuples(original_list_of_tuples,index,value))

#3. Update each element in the Tuple List using List Comprehension

test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]  # Time complexity O(1) and Space complexity O(1)
add_ele = 4
res = [tuple(add_ele + j for j in tup) for tup in test_list]
print(res)

#4. Update each element in tuple list in Python using Map() + Lambda + List Comprehension

test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]   # Time Complexity O(n) and Space Complexity O(n)
add_ele = 4
res = [tuple(map(lambda x : x + add_ele,tup)) for tup in test_list]
print(res)

#5. update each element in the Tuple List using the Extend() Method   

test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]   # Time Complexity O(n) and Space Complexity O(n)
test_list1 = [(4, 8, 3), (6, 2, 4)]
test_list.extend(test_list1)
print(test_list)

#6. Update a value in a list of Tuples using Slicing and Concatenation

test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]  # Time Complexity O(n) and Space Complexity O(n)
new_elements = (5,7,2)
index_to_update = 1
test_list = test_list[:index_to_update] + [new_elements] + test_list[index_to_update+1:]
print(test_list)
