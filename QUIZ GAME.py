import time

def NewGame():
    game = True
    while game:
        print("Welcome to my quiz game!")
        question = 1
        guesses = []
        correct_answer = 0

        for i in questions:
            print(i)
            for x in options[question - 1]:
                print(x)
            guess = input("A, B, C, D: ").upper()
            guesses.append(guess)
            correct_answer += CheckAnswer(questions.get(i), guess)
            question += 1
            time.sleep(0.5)
            if question == 5:
                time.sleep(0.5)
                ShowScore(correct_answer, guesses)
                time.sleep(0.5)
                while game:
                    game = PlayAgain()

def CheckAnswer(answer, guess):
    if guess == answer:
        print("Correct!")
        return 1
    elif guess != answer:
        print("Wrong!")
        return 0

def ShowScore(correct_answer, guesses):
    print("Results: ")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i) + " ",end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
            print(i + " ", end="")
    print()
    final_score = int(correct_answer/len(questions)*100)
    time.sleep(0.5)
    print("Score = " + str(final_score) + "%")
def PlayAgain():
    user_input = input("Do you want to play again? (Yes or No)").lower()
    if user_input == "yes":
        return NewGame()
    elif user_input == "no":
        return False
    else:
        print("Only Yes or No!")
        return True

questions = {
    "What is my name?": "C",
    "What is my birth year?": "D",
    "Is the Earth round?": "A",
    "Is the Sun bright?": "B",
}

options = [
    ["A. Daniel", "B. Maron", "C. Jorge Andrei", "D. Mark Jhun"],
    ["A. 1985", "B. 1969", "C. 2005", "D. 2006"],
    ["A. Yes", "B. No", "C. Hindi", "D. Diko alam"],
    ["A. No", "B. Yes", "C. Diko alam", "D. No"]]

NewGame()