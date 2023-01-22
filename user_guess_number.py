import random

def guessNumber(x):
    randomNumber = random.randint(1, x)
    guess = 0
    count = 0
    while guess != randomNumber:
        guess = int(input("Enter a Number : "))
        if guess < randomNumber:
            print("Your guess is lower than the actual number!")
        elif guess > randomNumber:
            print("Your guess is higher than the actual number!")
        count += 1
    
    print (f"You have guessed the Number {randomNumber} correctly.")
    print (f"You tried {count} times!")

if __name__ == '__main__':
    guessNumber(10)
