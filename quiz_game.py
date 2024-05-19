print("Welcome to my computer quiz!!")
score = 0

playing = input("Do you want to play? (yes/no): ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")

# Define questions and answers
questions = [
    "What does APU stand for? ",
    "What does ILS stand for? ",
    "What does VOR stand for in aviation? ",
    "What does MFD stand for? ",
    "What does ATC stand for? ",
    "What does TCAS stand for? "
]

correct_answers = [
    "Auxiliary Power Unit",
    "Instrument Landing System",
    "VHF Omni-directional Range",
    "Multi-Function Display",
    "Air Traffic Control",
    "Traffic Collision Avoidance System"
]

# Iterate through questions
for i in range(len(questions)):
    answer = input(questions[i])
    if answer.lower() == correct_answers[i].lower():
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

# Print final score
print("Your Score is " + str(score) + "/" + str(len(questions)))
