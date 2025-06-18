nums = [] 


print("Welcome to our calculator:") 
print("1. addition") 
print("2. subtraction") 
print("3. multipliction") 
print("4. division") 
print("5. modular division") 
option = input("Enter the operation: ").lower().strip()


if option == "addition": 
    num1 = int(input("Enter num1: ")) 
    num2 = int(input("Enter num2: ")) 
    nums.append(num1)
    nums.append(num2) 
    sum = nums[0] + nums[1]
    nums.append(sum)
    print(f" The sum of {nums[0]} and {nums[1]} is {nums[2]}.")

elif option == "subtraction":
        num3 = int(input("Enter num3: ")) 
        num4 = int(input("Enter num4: ")) 
        nums.append(num3)
        nums.append(num4)
        difference = nums[0] - nums[1]
        nums.append(difference)
        print(f"The difference of {nums[0]} and {nums[1]} is {nums[2]}.")

elif option == "multiplication":
    num5 = int(input("Enter num5: ")) 
    num6 = int(input("Enter num6: ")) 
    nums.append(num5)
    nums.append(num6)
    product = nums[0] * nums[1]
    nums.append(product)
    print(f"The product of {nums[0]} and {nums[1]} is {nums[2]}.")

elif option == "division":
    num7 = int(input("Enter num7: ")) 
    num8 = int(input("Enter num8: ")) 
    nums.append(num7)
    nums.append(num8)
    quotient= nums[0]/nums[1]
    nums.append(quotient)
    print(f"The quotient of {nums[0]} and {nums[1]} is {nums[2]}")

elif option == "modular division":
    num9 = int(input("Enter num9: ")) 
    num10 = int(input("Enter num10: ")) 
    nums.append(num9)
    nums.append(num10)
    remainder = nums[0] % nums[1]
    nums.append(remainder)
    print(f" The remainder of {nums[0]} / {nums[1]} is {nums[2]}.")

else: 
    print("This is not a valid operation.")