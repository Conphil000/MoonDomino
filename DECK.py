# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:57:58 2022

@author: Conor
"""

from DOMINO import DOMINO

def DECK(start = 1):
    if start in [0,1]:
        deck = []
        for s1 in range(start,7):
            for s2 in range(start,s1+1):
                deck.append(DOMINO(s1,s2))
        if start != 0:
            deck.append(DOMINO(0,0))
        return deck
    else:
        raise ValueError('Choose 0/1 for start.')
    
    # def DEAL(self,):
    #     deck = self.DECK()
    #     self.DRAW(deck)
        
    

if __name__ == '__main__':
    
    d1 = DECK(0)
    d2 = DECK(1)
    
    assert len(d2) == 22
    assert len(d1) == 28
    
    try:
        d3 = DECK(8)
    except ValueError:
        pass