# Programmers:  Hazel Osborne
# Course:  CS151, Zelalem Yalew
# Due Date: 9/25/2024
# PA Assignment 1
# Problem Statement: This program is designed to play out an interactive story
# Data In: Favorite ice cream flavor, Name, Q1, Q2b, Q2a, Q3
# Data Out:  Win or Lose

#Introduce Game to User
print("Welcome to Hazel's Quest for the perfect Ice Cream!!"
      " Make sure to match your answers to the prompt exactly!! Capitalization matters!")

#Prompt user to enter their name
player_name = input("Enter player name: ")

#Prompt user to enter their favorite ice cream flavor
favorite_flavor = input ("Enter favorite Ice Cream flavor: ")

#Define bad_flavor

if favorite_flavor != "Pistachio":
    bad_flavor = "Pistachio"
else:
    bad_flavor = "Butterscotch"

#Prompt user to enter info for q1
print("You're in the mall and start craving an ice cream. Where do you go? The hallway? or outside?")

q1 = float(input("Enter a number below 5 for the hallway, Enter a number above 5 for outside:  "))

#Check q1 value
if q1 < 5:
    print("You see 2 doors. What do you do?")

    # Ask for q2a input
    q2a = int(input("Enter 1 to open door 1, Enter 2 to open door 2, Enter 3 to leave:  "))

   #Check q2a value
    if q2a == 1:
        print("You found an ice cream shop!! You can either ask the worker for ice cream politely or rudely, what do you do?")
        q3 = str(input("Enter 'rude' to be rude, Enter 'polite' to be polite: "))

        #Check q3 value
        if q3 == "polite":
            print("Congrats!! You got", favorite_flavor,"Ice Cream!! Your favorite!!")

        elif q3 == "rude":
            print("You got Ice Cream! But because you were rude to the worker, they gave you", bad_flavor, "flavor instead! :( Try Again!!")

#Check q2a value
    elif q2a == 2:
        print("You found an ice cream shop!! You ordered", favorite_flavor,""
                             ", your favorite flavor but when you got it, you dropped it an slipped! :( Try Again!!")

    else:
        print("You leave the hallway and fail to get ice cream. :( Try again!!")

#Check q1 value
elif q1 > 5:
    print("You walk outside! You can either go to an unmarked stall, or an alley way.")
    q2b = str(input("Type 'Alley' to go to the alleyway or 'Stall' to go to the stall:  "))


#Check q2b value
    if q2b == "Alley":
        print("You went into the alley and got scared by a gang of cats!"
              " You were so shaken; you went home without ice cream. :( Try again!!")

    elif q2b == "Stall":
        print("You went to the unmarked stall, and it was an ice cream stall!! You politely ask the worker for your favorite flavor,"
              "", favorite_flavor, ", and they give it to you!! Yay!!")

#Check q1 value

else:
    print("Hey! Don't try to cheat the system!! Pick a number above or below five. If not, no ice cream for you!!")

#Thank player for playing.
print("Thanks for playing,", player_name,"!")