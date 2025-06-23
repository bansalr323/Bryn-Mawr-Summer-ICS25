#Nested For Loops:


for i in range (4): 
    for j in range(4): 
        print(f"outer loop: {i}, inner loop: {j}") 

for i in range(1,13): 
    for j in range(1,13): 
        print(i*j, end = " ")
    print() 

entrees = ["Steak", "Pasta", "Roasted Chicken", "Grilled Shrimp"]
sides = ["Fries", "Breadsticks", "Side Salad"] 
print("Wecome to Olive Garden.")
for dish in entrees: 
    for side in sides: 
        print(f"Main Dish: {dish}, Side: {side}") 

for i in range(1,6): 
    for j in range(i):
        print("*", end = " ") 
    print() 


#2D Lists: 
twodlist = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12], 
    [13,14,15,16]
            ] 
print(twodlist[0][1]) 
print(twodlist[0]) 
print(twodlist[1]) 
twodlist.append([17,18,19,20])
print(twodlist) 
#twodlist[0].append(10) 
print(twodlist[0]) 
print(twodlist)

twodlist = [
    [1,2],
    [3,4]
]

print("For Each") 
for row in twodlist: 
    for item in row: 
        print(item)

print("For i,j") 
for i in range(len(twodlist)): 
    for j in range(len(twodlist[0])): 
        #Right now it doesn't matter what index I put inside len(twodlist[])
            if twodlist[i][j] == 2: 
                twodlist[0].append(100) 
            print((twodlist[i][j]))

print("Fixed example: ")
for i in range(len(twodlist)): 
    j = 0 
    while j < len(twodlist[i]): 
        if twodlist[i][j] == 2: 
            twodlist[0].append(100) 
        print(twodlist[i][j]) 
        j = j + 1
