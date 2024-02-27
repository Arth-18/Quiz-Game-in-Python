print("Welcome to my first python project and a small computer quiz!")

playing = input("Hey, Do you Want to play this game 😃? ")

if playing.upper() != "YES":
    quit()

print("okay lets play")
score = 0

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    print("You Are Correct🥳")
    score += 1
else:
    print("Opps! Sorry Try Again🤞")


answer = input("What is the capital of Canada? ")
if answer.lower() == "ottawa":
    print("You Are Correct🥳")
    score += 1
else:
    print("Opps! Sorry Try Again🤞")


answer = input("What is the capital of Kenya? ")
if answer.lower() == "nairobi":
    print("You Are Correct🥳")
    score += 1
else:
    print("Opps! Sorry Try Again🤞")


print("Congratulaton! You Got " +str(score) + " Question Correct!" )
print("You Got " +str(score/3*100) + " %." )