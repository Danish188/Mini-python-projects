"""
Rock Paper Scissor

@author: Danish Elahi
"""
import random

r = 'rock'
p = 'paper'
s = 'scissor'

def winner(user , computer):
    # logic to declare the winner
    if ((user == p and computer == r) 
        or (user == s and computer == p)
        or (user == r and computer == s)):
        return True
# main logic of game
def playGame():
    
    play_again = True
    
    count_won = total_rounds = 0
    
    while play_again == True:
    # get decision of user
        userInput = input("What you wanna choose? \n Rock : r \n Paper : p \n Scissor : s \n Enter your choice: ").lower()
        
        if userInput == 'r':
            userInput = 'rock'
            
        elif userInput == 'p':
            userInput = 'paper'
            
        elif userInput == 's':
            userInput = 'scissor'
            
        # create random decision   
        computerGuess = random.choice([r, p, s])
        
        if computerGuess == userInput:
            print("Your Choose : " , userInput)
            print("Opponent Choose : " , computerGuess)
            print("it\'s a tie!")
          
        elif winner(userInput , computerGuess):
            print("Your Choose : " , userInput)
            print("Opponent Choose : " , computerGuess)
            count_won = count_won+1
            print("You Won!")
        
        else:
            print("Your Choose : " , userInput)
            print('Opponent Choose : ' , computerGuess)
            print('You Lost')
            
        #ask user if he wants to play again
        if_play = input("Do you want to play again (y/n): ").lower()
        total_rounds = total_rounds+1
        
        if if_play == "n":
            play_again = False
            print('You Played ', total_rounds , ' times')
            print('You Won ', count_won , ' times')
            print('Thanks for playing, you played well:)')
            
        elif if_play == "y":
            play_again = True
        
        else:
            print('Invalid Argument!')

if __name__ == "__main__":
    playGame()