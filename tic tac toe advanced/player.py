import math
import random

class player():
    def __init__(self , letter):
        self.letter = letter
    def getMove(self , game):
        pass
    
class humanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        validSquare = False
        val = True
        while not validSquare:
            square = input(self.letter + ' turn. :')
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid square!')
        return val
                
class smartComputer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game):
        if len(game.availableMoves()) == 9:
            square = random.choice(game.availableMoves())
        else:
            square = self.minmax(game , self.letter)['position']
        return square
    
    def minimax(self , state , player):
        max_player = self.letter
        otherPlayer = 'O' if player == 'X' else 'X'
        
        if state.countWinner == otherPlayer:
            return {'position':None , 'score':1*(state.numEmptySquare() + state.numEmptySquare()+1)}
        
        elif not state.emptySquares():
            return {'position':None , 'score':0}
        
        if player == max_player:
            best = {'position':None , 'score': -math.inf}
            
        else:
            best = {'position':None , 'score': math.inf}
            
        for possibleMove in state.availableMoves():
            state.makeMove(possibleMove , player)
            simScore = self.minmax(state , otherPlayer)
            
            state.board[possibleMove] = ' '
            state.currentWinner = None
            simScore['position'] = possibleMove
            
            if player == max_player:
                if simScore['score'] > best['score']:
                    best = simScore
            else:
                if simScore['score'] < best['score']:
                    best = simScore
        return best
                