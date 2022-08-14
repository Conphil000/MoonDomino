# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:37:37 2022

@author: Conor
"""

from HAND import HAND
from DOMINO import DOMINO
from DECK import DECK
import random



class GAME:
    def __init__(self,hands):
        self._players = hands 
    def RANDOM_GAME(self,):
        pass
    
if __name__ == '__main__':
    
    deck = DECK()
    
    for i in [0,1,2]:
        random.Random(123).shuffle(deck)
    
    def show_deck(deck):
        print([i.GET() for i in deck])
    
    show_deck(deck)
    
    random.seed(10)
    
    # random.shuffle(deck.copy()) # Always will get the same deck.
    
    # show_deck(d1)
    
    
    
    # game = GAME([HAND(),HAND(),HAND()])
    
    
    # game.DEAL()
    
    

    












