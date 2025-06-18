#Boolean Values and Conditionals
var1 = True 
if var1 == True: 
    print("Hello World") 

var2 = False 
if var2 == True: 
    print("Hello 2") 
print("Hello 3")

var3 = 5 
if var3 == 5: 
    print("Hello 4) ")
if var3 > 4:
    print("Hello 4") 
print("Hello 5")

num = int(input("Enter your number: "))
if num % 2 == 1: 
    print(f"{num} is an odd number.")
else:
    print(f"{num} is an even number.") 

print("Checking if a number is divisible by 5 or 2") 
num = int(input("Enter your number: "))
if num % 5 == 0: 
    print(f"{num} is divisible by 5") 
if num % 2 == 0: 
    print(f"{num} is divisible by 2") 
else: 
    print(f"{num} is not divisible by 5 or 2")

print("Welcome to our Baltimore Sports Program: ")
print("1. Football") 
print("2. Baseball") 
option = input("Enter the sport you would like to know the Baltimore team for: ")
if option == "Football": 
    print("Baltimore Ravens") 
elif option == "Baseball":
    print("Baltimore Orioles")
else: 
    print("No valid option for that sport")


#Strings 

#.lower(), .upper(), and .strip()
text = "HELLO WORLD"
text = text.lower()
print(text)

text = "hello world"
print(text)
text = text.upper()
print(text)  

print("Test menu: ") 
print("1. hello") 
print("2. world") 
option = input("Enter option: ").lower().strip()
if option == "hello": 
    print("hello") 
elif option == "world": 
    print("world")

#Adding Strings .join()
str1 = "hello"
str2 = "world"
print(str1 + " " + str2) 

newstr = " ".join(str2)
print(newstr)

#.find()
index = str1.find("l")
print(index)


#Lists 
fruits = ["mangos", "bananas", "apples", "strawberries", "grapes"]
print(fruits) 
print(fruits[3])
fruits[3] = "raspberries"
print(fruits[3])
print(fruits) 
fruits.append("strawberries") 
fruits.insert(3, "strawberries")
print(fruits) 

mylist = [2,3,4,"Ria Bansal", True]
'''print(mylist) 
mylist.remove("Ria Bansal")
print(mylist)
mylist.pop(3)
print(mylist)'''
print(mylist[-1]) 
print(mylist[-2])
option = int(input("Which object of your list would you like to access?: "))
print(mylist[option])
print(mylist[0] + mylist[2])

mylist2 = [10, 15, 20, 55]
mylist3 = mylist + mylist2 
mylist.extend(mylist2)
print(mylist)
mylist.pop(-1)
print(mylist)
print(mylist3) 

print("confusing example")
num1 = 5 
num2 = num1 
num2 = num2 + 5 
print(num2) 
print(num1) 

mylist = [1,2,3]
mylist2 = mylist
mylist2.append(4)
print(mylist)
print(mylist2) 
mylist2 = mylist.copy() 
mylist2.append(4) 
print(mylist) 
print(mylist2)
