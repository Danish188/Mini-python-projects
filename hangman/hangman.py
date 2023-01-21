from wordlist import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  

def hangman():
    word = get_valid_word(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    
    lives=10
    
    while len(wordLetters) > 0 and lives > 0  :
        
        print('You have ' , lives , ' left')
        print('And you have used these letters' , ' '.join(usedLetters))
        
        wordList = [letter if letter in usedLetters else '_' for letter in word]
        print("Current word : ", ' '.join(wordList)) 
        
        userInput = input("Guess a letter : ").upper()
        if userInput in alphabet - usedLetters:
            usedLetters.add(userInput)
            if userInput in wordLetters:
                wordLetters.remove(userInput)
            else:
                lives = lives-1
                print("Letter is not in word.")
        elif userInput in usedLetters:
            print("You have already used this character! Try another .")
        else:
            print('invalid character! Try again.')
            
    if lives == 0:
        print("You loose!")
        print("The word was : " , word)
    else:
        print("You guessed the word " , word , '!!')

if __name__ == "__main__":
    hangman()