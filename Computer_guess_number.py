import  random

def computerGuess(n):
    low = 1
    high = n
    answer = ''
    while answer != 'c' and low != high:
        # get random number from the computer
        guess = random.randint(low, high)
        # asking if the guess is higher lower or correct
        answer = input(f"The computer guesses the number: {guess} \n is it Higher(h) \n Lower(l) \n Correct(c)?").lower()
        # condition for the program
        if answer == 'h':
            high = guess - 1
        elif answer == 'l':
            low = guess + 1
        elif answer == "c":
            print("Hurraaa!")
        else:
            print("You entered a wrong command!")
            
    print(f'Yes the correct number is {guess}!')

if __name__ =='__main__':
    num = int(input("Enter a number to be guessed : "))
    computerGuess(num)