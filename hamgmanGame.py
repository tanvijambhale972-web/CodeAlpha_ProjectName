import random
words=["beauty", "brain", "harleydavidson" , "paper" , "technology"]
word=random.choice(words)
guessed=["_"]*len(word)
attempts=6
guessed_letters=[]

print("welcome to our simple hangman game")
print("guess the word")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\n enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter only alphabet letters:")
        continue

    if guess in guessed_letters:
        print("\n you have already guessed this letter")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("correct")

        for i in range(len(word)):
            if word[i]== guess:
                guessed[i]=guess
    else:
        attempts-=1
        print("wrong! attemps left: ",attempts)
    print(" ".join(guessed))
if "_" not in guessed:
    print("congragulationss! you winn buddy!!!")
    print("the word was: ",word)
else:
    print("better luck buddy! more chances to win")
    print("the word was: ",word)
