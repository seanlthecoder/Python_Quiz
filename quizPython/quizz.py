print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:")
score = 0

answer = input("Who directed 'Inception'? ")

if answer.lower() == "christopher nolan":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What was the last film Christopher Nolan directed? ")

if answer.lower() == "oppenheimer":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("Which Batman film is Nolan's best? ")

if answer.lower() == "the dark knight":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("Who played Bane in 'The Dark Knight Rises'? ")

if answer.lower() == "tom hardy":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " %.")
