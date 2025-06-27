import random 

def intro():
    print(" ")
    print("Ok then, let's get started!")
    print(" ") 
    print("You are the famous - Detective Sally! You have escaped the evil society - VILE as a little kid.")
    print("You used to have friends there like Lightning (her real name was Lucy) but she betrayed you and so you knew you had to escape and stop these villans.")
    print("If you don't know about VILE there's not much I can tell you because (they are a top secret society).") 
    print("However I can tell you that they are up to no good especially with the new headmastress Mrs. Villy.")
    print(" ") 
    print("Time is running out! Our first mission starts now: ")

def country_deciding_menu(): 
    print(" ") 
    print("You have 2 options: ") 
    print("1. Go to Indonesia and defeat Mr. Vile who is planning to meet up with Mrs. Villy and together they will make VILE stronger (not good!).")
    print("2. Go to Japan. VILE is planning on stealing all the toys from the shops, making all the businesses there go bankrupt!")
    country_choice = input("Which option do you choose?: ") 
    return country_choice

def passport_deciding_menu(): 
    print(" ") 
    print("You have 2 options: ") 
    print("1. Take the passport")
    print("2. Don't take the passport.")
    passport_choice = input("Which option do you choose?: ") 
    return passport_choice

passport_dict = {"Kelly": "(200,97)", "Ryan": "(200074, 198005)", "Josh": "(9000, 130)"} 

def following_or_not_menu(): 
    print(" ")
    print("1. Follow")
    print("2. Or not follow")
    follow_choice = input("Which option do you choose?: ")
    return follow_choice 

def facing_MrVile_menu(): 
    print(" ")
    print("1. Stay and fight")
    print("2. Run away")
    facing_MrVile_choice = input("Which option do you choose?: ")
    return facing_MrVile_choice

def catch_thief_or_not_menu(): 
    print(" ")
    print("1. Follow the thief.")
    print("2. Get treatement for your leg.")
    catch_thief_choice = input("Which option do you choose?: ")
    return catch_thief_choice 

def dessert_menu(): 
    print(" ")
    print("1. cake")
    print("2. cookies")
    print("3. ice cream")
    print("4. brownies")
    dessert_choice = input("Which option do you choose?: ") 
    return dessert_choice 

board = [
    [".", ".","."], 
    [".", ".","."],
    [".", ".","."]
]

def printBoard(grid): 
    for row in grid: 
        print("|", end = "")
        for number in row: 
            print(number, end = "|")
        print() 

def challengeInstructions(): 
    print(" ")
    print("Basically for this challenge there is going to be a 3*3 grid. There are 4 spots that are the winning spots. If you guess even just 1 of those spots correctly you win. ")
    print("If you don't guess any of the spots correctly you lose.")
    print("Put the row and column you want to guess into the program.")
    print("An X will be placed in that spot.") 
    print("Ready, Set, Go!")

def createchoices(): 
    choices = [] 
    for i in range(4): 
        choice = (random.randint(0,2), random.randint(0,2)) 
        choices.append(choice)
        return choices

def playChallenge(grid): 
    wins = createchoices()
    tries = 1
    check = True
    while tries <= 4 and check == True:
        print(" ")
        row = int(input("Enter the row you would like to guess (has to be a number from 0-2): "))
        col = int(input("Enter the column you would like to guess (has to be a number from 0-2): "))
        grid[row][col] = "X"
        printBoard(grid)
        if (row,col) in wins:
            print("You win and you have completed a successful mission!")
            check = False
    if tries == 5: 
        print("You lose and have not completed a successful mission.")
       


def invalid_option(): 
    print("This is not a valid option. Please try again.")

def main(): 
    check = True 

    while check == True: 
        print(" ")
        print("Hello! This is a Choose Your Own Adventure Story.")
        print("Are you excited to play?")
        yes_no = input("yes or no?: ").lower().strip()

        if yes_no == "no": 
            print("No! Then why are you here? Go do something else!")
            check = False 

        elif yes_no == "yes": 
            intro()
            country_choice = country_deciding_menu()

            if country_choice.isnumeric() == False:
                invalid_option()
            elif country_choice.isnumeric()== True:

                if int(country_choice) == 1: 
                    print(" ")
                    print("Ok, you have landed in Indonesia, long flight right! However your job is not over yet.")
                    print("When you land in the airport you see this guy in all black and as soon as he sees you he runs away! ")
                    print("You know this is suspicious") 
                    print("You see his passport lying on the ground. You know it's not right to take people's passports, but you were specifically warned that if you don't take it this mission will be a disaster.")
                    passport_choice = passport_deciding_menu()

                    if passport_choice.isnumeric() == False:
                        invalid_option()
                    elif passport_choice.isnumeric()== True:

                        if int(passport_choice) == 1: 
                            print(" ")
                            print("On the passport (for some reason) he wrote the exact coordinates of where he was heading.")
                            print("I searched it up on Google Maps and apparently it was an unrecognized coordinate, which could only mean bad news")
                            print("He also had some names and numbers on the passports.") 
                            print(passport_dict) 
                            print("You had no idea who these people were, but the names seemed to be associated with coordinates.")
                            print("So you know these people must be important.") 
                            print("You decided to follow this guy.")
                            print("However as soon as he turned I realized he was going the wrong way. The opposite of the coordinates. What do you think now should you...") 
                            follow_choice = following_or_not_menu()

                            if follow_choice.isnumeric() == False:
                                invalid_option()
                            elif follow_choice.isnumeric()== True:

                                if int(follow_choice) == 1: 
                                    print(" ")
                                    print("He was trying to trick you! He catches you in the trunk and reports you. You have to fly back to your house and abort the mission.")
                                    check = False 

                                elif int(follow_choice) == 2: 
                                    print(" ")
                                    print("Good job not following Mr. Vile! He was trying to trick you.")
                                    print("You reach VILE even earlier than him (because he took a little detour).")
                                    print("This gives you time to snoop around and you figure out that the names on the passport were his sidekicks.")
                                    print("You block all his sidekicks from his phone.")
                                    print("Then he walks in and he sees you. He knows he is done for, but still Mr. Vile is a fiesty one. He fights you and you end up winning.")
                                    print("Mr. Vile tells Ms. Villy that the mission didn't work. Ms. Villy is so sad she can't be with her husband that VILE is stopped!")
                                    print("If you complete this last challenge your mission will be marked successfully completed.")
                                    challengeInstructions()
                                    playChallenge(board)
                                    check = False

                        elif int(passport_choice) == 2: 
                                print(" ")
                                print("Unfortunately the passport had all the information you needed (including location coordinates)")
                                print("You were about to snatch it, but suddenly the guy in black realized he was missing his passport and snatched it out of your hands.")
                                print("You decided to follow him.")
                                print("He got in his car and while the bellboy was loading the luggage into the trunk you hopped in the trunk too and gave the bellboy $20 to be quiet about it. He agreed.")
                                print("Finally you were at the unknown coordinates")
                                print("It was VILE. There really was a VILE everywhere.")
                                print("You creeped in and listened to the whole phone conversation.")
                                print("Then he hung up.")
                                print("You made a teeny tiny squeal of delight that everything was going as you planned and that's when...he heard you.")
                                print("He turned to you and said he was going to make you take the blame for everything - the whole VILE catastrophe.") 
                                print("He also said you only had two options - take the blame or brainwash")
                                print("I realized I had two other better options...")
                                facing_MrVile_choice = facing_MrVile_menu()

                                if facing_MrVile_choice.isnumeric() == False:
                                    invalid_option()
                                elif facing_MrVile_choice.isnumeric() == True:

                                    if int(facing_MrVile_choice) == 1: 
                                        print(" ")
                                        print("You fought and fought, but Mr. Vile was stronger. You ended up brainwashed.")
                                        check = False 

                                    elif int(facing_MrVile_choice) == 2: 
                                        print(" ")
                                        print("You ran and ran away and since you were in the mountains Mr. Vile couldn't find you - safe right!, but...")
                                        print("A polar bear found you and decided to take you to his cave to hang out with his polar bear buddies. You were forced to party with them for the rest of your life. ")
                                        print("On top of that VILE mystery was left unsolved and your famous title lost")
                                        check = False 

                elif int(country_choice) == 2: 
                            print(" ")
                            print("You have finally landed in Japan, such a long flight!")
                            print("You love sushi so you stop for a bite at the airport.")
                            print("Then you head over to the main shopping area (not just for shopping), but you know that that's where the thief/thieves will most likely be.")
                            print("You see the thief run out of the toy shop, the toy shop owners don't know that he stole, but you see a LOT of stuff in their hands.")
                            print("Suddenly you feel a sharp pang in your leg. Do you...")
                            catch_thief_choice = catch_thief_or_not_menu() 

                            if catch_thief_choice.isnumeric() == False:
                                invalid_option()

                            elif catch_thief_choice.isnumeric()== True:

                                if int(catch_thief_choice) == 1: 
                                    print(" ")
                                    print("You decided to follow the the thief, you follow him and follow him and he keeps stealing stuff.")
                                    print("You decide that enough is enough. You want to fight!")
                                    print("You fight him and he's actually pretty weak. You are able to defeat him!")
                                    print("But right at that moment your leg starts acting up again. You realize you have to get treatment.")
                                    print("And to make it worse at that exact moment the thief escapes.")
                                    print("You are stuck in the hospital for weeks and are not able to catch the thief. Your boss tells your time has run out and that you have to get back home.")
                                    print("Your mission is unsuccessful.")
                                    check = False 
                                    
                                elif int(catch_thief_choice) == 2: 
                                    print(" ")
                                    print("You were lucky that you came to the hospital as quick as you could.")
                                    print("The doctor said that if you stayed in pain for any longer then healing could have taken weeks!")
                                    print("Luckily you caught it early and only have to stay in the hospital for 3 days.")
                                    print("After 3 days you are all better.")
                                    print("You go back to the main shopping square and you see the thief, still stealing toys!")
                                    print("You saw him and he saw me and you started to fight")
                                    print("But then you saw this look in his eyes and realized that he was not doing this for himself that there was a background to the story.")
                                    print("You stopped fighting and asked him what was wrong.")
                                    print("He said that he was doing this because when he was a kid he was sick in the hospital and often did not get the love he needed.")
                                    print("He said that toys was one of the things that cheered him up when he was a kid, but that many kids did not have the money to afford toys with such expensive treatement.")
                                    print("That is when you suggested that they he opens up a charity instead where peoole donate toys to children in hospitals.")
                                    print("Together you and hin were able to create a successful charity and from then on the thief promised he would never steal again.")
                                    print("You guys decided to get desert to celebrate, but weren't sure which desert to get. There was... ")
                                    dessert_choice = dessert_menu() 

                                    if dessert_choice.isnumeric() == False:
                                        invalid_option()

                                    elif dessert_choice.isnumeric()== True:
                                        if int(dessert_choice) == 1: 
                                            print("And you together you enjoyed your slice of cake happily ever after.")
                                            print(" ")
                                            print("But wait we're not done solve this challenge to fully complete the mission!")
                                            challengeInstructions()
                                            playChallenge(board)
                                            check = False 
                                        elif int(dessert_choice) == 2: 
                                            print("And you together you enjoyed your tray of cookies happily ever after.")
                                            print(" ")
                                            print("But wait we're not done solve this challenge to fully complete the mission!")
                                            challengeInstructions()
                                            playChallenge(board)
                                            check = False
                                        elif int(dessert_choice) == 3: 
                                            print("And you together you enjoyed your ice cream happily ever after.") 
                                            print(" ")
                                            print("But wait we're not done solve this challenge to fully complete the mission!")
                                            challengeInstructions()
                                            playChallenge(board)
                                            check = False 
                                        elif int(dessert_choice) == 4: 
                                            print("And you together you enjoyed your tray of brownies happily ever after.")
                                            print(" ")
                                            print("But wait we're not done solve this challenge to fully complete the mission!")
                                            challengeInstructions()
                                            playChallenge(board)
                                            check = False 

        else: 
            invalid_option()

main()


