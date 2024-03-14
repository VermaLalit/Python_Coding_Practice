#1. using lambda function 
str1 = "lalit verma pithora haluwasia"  # Time Complexity: O(n) and space complexity O(n)
print(" ".join(map(lambda str1:str1[:-1] + str1[-1].upper(),str1.title().split())))

#2. using slicing and upper(),split() methods 

str1 = "lalit verma pithora haluwasia" 
res = []
for i in str1.split():   # Time Complexity: O(n) and space complexity O(n)
    x = i[0].upper() + i[1:-1] + i[-1].upper()
    res.append(x)
print(" ".join(res))  

# 3. using loop + title() + split() + upper() + strip() (Slicing)

str1 = "lalit verma pithora haluwasia"   # Time Complexity: O(n) and space complexity O(n)
str2 = ""
for i in str1.title().split():
    str2 += i[:-1] + i[-1].upper() + " "
print(str2)
print(str2.strip())    # To removing space at the end