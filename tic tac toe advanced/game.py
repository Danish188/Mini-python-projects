import math
import time

from player import humanPlayer , smartComputer
 
class ticTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.countWinner = None
    
    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + " | ".join(row) + ' |')
            
    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3 , (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + " | ".join(row) + ' |')
    
    def availableMoves(self):
        return [i for i , spot in enumerate(self.board) if spot == ' '] 
   
    def emptySquares(self):
        return " " in self.board
    
    def numEmptySquare(self):
        return self.board.count(" ")
    
    def makeMove(self , square , letter):
        if self.board[square] == ' ':
            self.board[square] == letter
            if self.winner(square , letter):
                self.countWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False
    
    
def play(game , xPlayer , oPlayer , printGame = True):
    if printGame == True:
        game.printBoardNums()
        
    letter = 'O'
    
    while game.emptySquares():
        if letter == 'X':
            square = xPlayer.getMove(game)
        else:
            square = oPlayer.getMove(game)
        if game.makeMove(square , letter):
            if printGame:
                print(letter + f' make a move to square {square}')
                game.printBoard()
                print(" ")
                
            if game.countWinner:
                if printGame:
                    print(letter + ' wins!')
                return letter            
            letter = 'O' if letter == 'X' else 'X'
            
        time.sleep(0.1)
        
    if printGame:
        print('its a tie!')
        
if __name__ == '__main__':
    x_player = smartComputer('X')
    o_player = humanPlayer('O')
    t = ticTacToe()
    play(t, x_player, o_player, printGame=True)