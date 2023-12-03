# -*- coding: utf-8 -*-
"""
players file

@author: Danish Elahi
"""
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
    
    def getMove(self , game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. input move (0-9): ')
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid squere. try again')      
        return val
    
class computerPlayer(player):
    def __init__(self , letter):
        super().__init__(letter) 
            
    def getMove(self , game):
        square = random.choice(game.availableMoves())
        return square

                    