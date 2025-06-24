#Reviewing Concurrent Lists: 
entrees = ["Steak", "Pasta", "Grilled Shrimp"]
prices = [25, 18, 19]

for i in range(len(entrees)): 
    print(f"Entree: {entrees [i]} Price: {prices[i]}") 


#Dictionaries: 


entrees = {"Steak": 25, "Pasta": 18, "Grilled Shrimp": 19}
print("- - -")
print(entrees) 
print(entrees["Steak"])

#.keys():
print("Steak")
keys = list(entrees.keys()) 
print(keys) 

#Adding to the Dictionary: 
entrees["Lobster"] = 60 
print(entrees["Lobster"]) 
print(entrees)


mydict = {1: 15, "Hello": "World", 2.5: 10, 3: "Olive Garden"}
print(mydict)  

'''mydict2 = {[1,2,3,4]: "Hello World"}
print(mydict2) 
#Won't work because mutable objects can't be keys.''' 

#Dictionaries with Lists: 
mylist = [1,2,3,4]
mydict2 = {} 
mydict2 ["List"] = mylist 
print(mydict2) 
print(mydict2["List"][1]) 

student = {"Name": "John Smith", "Grade Level": 9, "Email": "SmithJ@BrynMawrSchool.org"}
grades = {"English": 65, "Math": 100, "Social Studies": 85, "Biology": 70}
student["Grades"] = grades 
print(student["Grades"]["English"])

mydict3 = {"Hello": "World"}
mydict4 = {"Mylist": [1,2,3,4]} 
mydict3["subdict"] = mydict4 
print(mydict3["subdict"]["Mylist"][1]) 

print("- - -") 
print(entrees) 
entrees.pop("Lobster")
print(entrees) 

entrees["Ribs"] = 18 
print(entrees) 

#For Loops with Dictionaries 
print("- - - -") 
for item in entrees: 
    print(item) 

for item in entrees: 
    print(entrees[item]) 

print("Using values():") 
for item in entrees.values(): 
    print(item) 

print("Raising prices:") 
for item in entrees: 
    entrees[item] += 5 
print(entrees) 


#Functions: 

#Built-ins: 
print(dir("__builtins__"))

def hello(): 
    print("Hello world") 
hello() #Just use this one
print(hello) #Will just tell you its adress in memory
print(hello()) #An extra print outside of the function itself will give you weird behavior

def hello(name): 
    print(f"Hello, {name}.") 
hello("Tim Cheese") 
hello("John Pork")
#parameter = name 
#arguments = Tim Cheese, John Pork, or any string 

def mean(nums): 
    average = 0
    for num in nums:
        average += num 
    average = average/len(nums)
    return average 
    #3.0

print("With Return") 
numbers = [1,2,3,4,5]
avg = (mean(numbers))
print(avg) 
numbers2 = [1,8,25,65,100,250]
avg2 = mean(numbers2)
print(avg2)

def example(num):
    if num % 5 == 0: 
        print("Hello! 5") 
        return 
    if num % 3 == 0: 
        print("Hello! 3") 
        return 
    else: 
        print("No, thanks!")
        return
    
example(5)
example(6) 
example(7)
example(15)