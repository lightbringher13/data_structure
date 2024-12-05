import hangmanStages
print("Let's Play Hangman!!")
print("you have only 6 lives so try to guess the word within 6 attempts! Good luck !!")
word = "vegetable"
guess = []
for i in range(len(word)):
    guess.append("-")
# use join(), " ": sepeartor
print(" ".join(guess))
lives = 6
while lives > 0:
    guessed_letter = input("Guess a letter: ")
    # check if the letter is alphabet
    # check conditions careful or/and
    if len(guessed_letter) > 1 or not guessed_letter.isalpha() or guessed_letter in guess:
        print("only one letter at once")
        print("guess the alphabet. invalid input")
        print("guessed same alphabet")
        continue
    if guessed_letter not in word:
        print(f"you guessed {
            guessed_letter} which is not present in the word. So you lose a life")
        lives = lives - 1
        # use join(), " ": sepeartor
        print(" ".join(guess))
        print(hangmanStages.hangman[lives])
        if lives == 0:
            print("you lose")
    else:
        # keep track of both index,element
        for index, letter in enumerate(word):
            if letter == guessed_letter:
                guess[index] = letter
        # use join(), " ": sepeartor
        print(" ".join(guess))
        if "-" not in guess:
            print("you win")
            break
