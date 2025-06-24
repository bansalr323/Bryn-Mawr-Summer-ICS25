mushrooms = []
check = True 

while check == True: 
    option = input("Enter mushroom weight, or STOP to end: ")
    if option == "STOP": 
        check = False  
    elif int(option) < 1: 
        print("Weight must be bigger than zero!") 
    else: 
        mushrooms.append(int(option))

big_mushroom = 0 
small_mushroom = 0 
medium_mushroom = 0 

for size in mushrooms: 
    if size > 1000: 
        big_mushroom += 1 

    elif size < 100: 
        small_mushroom += 1 

    else:
        medium_mushroom += 1 
print(f"There were {small_mushroom} small mushrooms, {medium_mushroom} medium mushrooms, and {big_mushroom} large mushrooms.")

        





