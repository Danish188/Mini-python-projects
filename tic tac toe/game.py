# -*- coding: utf-8 -*-
"""
game file

@author: Danish Elahi
"""
import math
import time
from players import computerPlayer , humanPlayer

class ticTacToe():
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.currentWinner = None
    
    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + ' | '.join(row) + ' |')
            
    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3 , (j+1)*3)] for j in range(3)]
        for row in numberBoard:
           print('|' + ' | '.join(row) + ' |')

    def availableMoves(self):
        return [i for i , spot in enumerate(self.board) if spot == " "]
    
    def emptySquare(self):
        return " " in self.board
    
    def numEmptySquares(self):
        return self.board.count(" ")
    
    def makeMove (self , square , letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square , letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self , square , letter):
        rowIndex = math.floor(square / 3)
        row = self.board[rowIndex*3 : (rowIndex+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        colIndex = square % 3
        column = [self.board[colIndex+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal = [self.board[i] for i in [0 , 4 , 8]]
            if all([spot == letter for spot in diagonal]):
                return True
            diagonal2 =  [self.board[i] for i in [2 , 4 , 8]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
    
def play(game , xPlayer , oPlayer , printGame=True):
    if printGame:
        game.printBoardNums()
        
    letter = "O"
    
    while game.emptySquare():
        if letter == "X":
            square = xPlayer.getMove(game)
        else:
            square = oPlayer.getMove(game)
            
        if game.makeMove(square , letter):
            if printGame:
                print(letter + f'make a move to sqare {square}')
                game.printBoard()
                print("")
            
            if game.currentWinner:
                if printGame:
                    print(letter + ' wins! ')
                return letter
                
            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(0.10)
        
    if printGame:
        print('it\'s a tie')
            
if __name__ == '__main__':
    X = humanPlayer('X')
    O = computerPlayer('O')
    t = ticTacToe()
    play(t , O , X , printGame=True)
    