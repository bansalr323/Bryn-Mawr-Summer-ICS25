#Loops: 


#While Loops:
x = 0 
while x < 5: 
    print(x)
    x = x + 1 

x = 1
while x <= 10: 
    if x % 2 == 0: 
        print(f"{x} is even.")
    elif x % 2 == 1: 
        print(f"{x} is odd.")
    x = x + 1 

x = 1
while x <= 100: 
    if x % 3 == 0: 
        print(f"{x} is divisible by 3.")
        x = x + 1 

#For loops: 
fruits = ["oranges", "apples", "mangoes", "cherries", "grapes"]
for fruit in fruits: 
    if fruit == "cherries" or fruit == "grapes":
        print(f"{fruit} is a small fruit")
    elif fruit == "apples" or fruit == "oranges" or fruit == "mangoes": 
        print(f"{fruit} is a large fruit")

nums = [23,13,45,40,87,35,63,22,9,1,50,27,95,100,21,28,38,80,29,53,16,32,60,65,79,8,66,7,70,4,99,78,88,10,46,25,47,93,83,36,56,91,97,96,2,57,26,54,55,98,51,37,17,49,69,72,59,64,77,94,24,82,30,31,39,43,76,92,52,74,11,84,58,67,34,12,41,68,81,85,19,20,44,18,15,14,61,42,3,86,48,75,6,62,89,73,90,71,5,33]
total = 0 
for num in nums: 
    total = total + num 
print(f"Sum of nums: {total}") 
amt = len(nums)
avg = total/amt
print(f"The average of the numbers is {avg}.")

#Range 
nums = list(range(100))
print(nums) 
nums = list(range(5))
print(nums) 

mylist = [5, 7, 1, 3, 6, 8, 2, 10]
nums = list(range(len(mylist)))
print(nums) 

total = 0 
for i in range(len(mylist)): 
    total = total + mylist[i]

print(total)
total = 0 
for num in mylist: 
    total = total + num 
print(total) 

mylist = [1,2,3,4]
for num in mylist: 
    num = num + 2 
print(mylist) 

mylist = [1,2,3,4]
for i in range(len(mylist)): 
    mylist[i] = mylist[i] + 2 
print(mylist)


#Concurrent Lists:  
fruits = ["orange", "mango", "grapes"]
price = [1.25, 1.50, 2.25] 

print("Welcome to our store")
for i in range(len(fruits)): 
    print(f"Fruit Name: {fruits[i]}")
    print(f"Fruit Price: {price[i]}") 


#More strings: 
code = "aabbbabbabababbabbabbababababbabbabbabbaabbaaababaababaaabaaababababababaaaabab"
total_a = 0 
total_b = 0 

for char in code: 
    if char == "a": 
        total_a = total_a + 1 
    elif char == "b": 
        total_b += 1 
print(f"Total a's: {total_a}, Total b's: {total_b}") 

str1 = "hello"
str2 = "world"
print(str1 + str2)
print(str2 + str1) 

strcopy = "" 
for char in str1: 
    strcopy = strcopy + char 
    print(strcopy)