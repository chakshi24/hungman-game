import random #This is used to randomly choose an item from a list [] or basically a sequence.

def hangman():
    words = ['apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig', 'grape']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
            print_hangman(tries)
        else:
            print("Correct guess!")
            print_word(word, guessed_letters)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You won!")
            break

    if tries == 0:
        print("You lost. Better luck next time!")
        print(f"The word was: {word}")

def print_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print("_", end=' ')
    print()

def print_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
        '''
    ]
    print(stages[tries])

hangman()
