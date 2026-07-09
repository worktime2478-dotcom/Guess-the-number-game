
# Guess the number

print("I am introducing you my first game which is made with the help of Python and the name of this game is ->")

print("GUESS THE NUMBER","\n you have only five attemts let's check your luck .")


import random

target = random.randint(1, 100)
range = 0
attempts = 4

while range < 5 :
    usr = input("enter a number b/w 1 to 100 or quit(Q) =")
    if (usr == "Q"):
        break
    usr = int(usr)
    if (usr > 100 or usr < 0) :
        print("your entered no. is invalid ")
        break 
    if usr == target:
        print("Congrats you won the match,\n your entered no. is matched")
        break
    elif usr > target :
        print("your entered no. is greater than the target ")
    elif usr < target :
        print("your entered no. is smaller than the target")
    print(attempts,"attmpts remaining")

    range += 1
    attempts -= 1

print(f"your target is {target}")
print("_________<GAME OVER>__________")
