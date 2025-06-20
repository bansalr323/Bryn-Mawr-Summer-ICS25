check = True 


while check == True: 
    word = input("Enter your word (type quit if you want to quit): ").lower().strip().split()
    word = "".join(word)
    strcopy = ""
    for char in word: 
        strcopy = char + strcopy 
    if word == strcopy: 
        print("This is a palindrome!") 
    elif word == "quit":
        break
    else: 
        print("This is not a palindrome!") 