import random

num_digits = 3
max_guess = 5

def main():
    print('''
          Bagels , a deductive logic game.
          I am thinking of a {}-digit with no repeated digits.
          Try to guess what it is. Here are some clues:
          when i say       what it means
          Pico             1 digit is correct but in wrong place
          Fermi            1 digit is correct and in the correct place
          Bagels           No digit is correct
          
          for example if the digit was 243 and your guess was 843 than
          the clues will be Fermi Pico
          '''.format(num_digits))
    
    while True:
        secret_num = getSecretNum()
        print("I have thought up a number.")
        print("You have {}-guesses to get it!".format(max_guess))
        
        num_guesses = 1
        while num_guesses <= max_guess:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print("guess #{}:".format(num_guesses))
                guess = input("> ")
            clues = getClues(guess , secret_num)
            print(clues)
            num_guesses+=1
            
            if guess == secret_num:
                break
            if num_guesses == max_guess:
                print("You ran out of guesses!")
                print("The answer was {}.".format(secret_num))
        print("Do you want to play again?")
        if not input("> ").lower().startswith('y'):
            break
    print('Thanks for playing!')
    
    
def getSecretNum():
    num = list('0123456789')
    random.shuffle(num)
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(num[i])
    return secret_num

def getClues(guess , secret_num):
    if guess == secret_num:
        return "You got it!"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    
    else:
        clues.sort()
        return ' '.join(clues)  
    
if __name__ == '__main__':
    main()