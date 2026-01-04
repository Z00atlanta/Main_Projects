print("Welcome to my quiz :)")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Well then! Let's play! ")
score  = 0

answer = input("What does CPU stand for?")
if answer.lower()== "central processing unit" :
    print("CORRECT!")
    score += 1
else:
    print("incorrect...")


answer = input("What does OMG stand for?")
if answer.lower() == "oh my god" :
    print("CORRECT!")
    score += 1
else:
    print("incorrect...")


answer = input("What does TTYL stand for?")
if answer.lower() == "talk to you later" :
    print("CORRECT!")
    score += 1
else:
    print("incorrect...")


    answer = input("What does LYK stand for?")
if answer.lower() == "letting you know" :
    print("CORRECT!")
    score += 1
else:
    print("incorrect...")


print("You got a " + str(score) + " out of 4 questions correct!")
print("You got a " + str((score/4) * 100) + "%.")
