import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "strawberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while True:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts += 1
            print("Incorrect guess. Attempts left:", max_attempts - attempts)
            if attempts >= max_attempts:
                print("You've run out of attempts! The word was:", word)
                break
        
        print(display_word(word, guessed_letters))
        
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
