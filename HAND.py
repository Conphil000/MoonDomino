# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 22:10:53 2022

@author: Conor
"""
import random
class HAND:
    def __init__(self,):
        self._hand = []
        self._usable = []
    def ADD(self,DOMINO):
        self._hand.append(DOMINO)
        self._usable.append(1)
    def USABLE(self,):
        usable = []
        for i in range(0,len(self._usable)):
            if self._usable[i] == 1:
                usable.append(self._hand[i])
        return usable
    def KILL(self,DOMINO):
        for i in range(0,len(self._hand) ):
            if self._hand[i] == DOMINO:
                self._usable[i] = 0
    
if __name__ == '__main__':
    from DOMINO import DOMINO
    
    hand = HAND()
    
    
    for i in range(0,7):
        hand.ADD(DOMINO(random.randint(1, 6),random.randint(1, 6)))
    play = hand.USABLE()[3]
    print([i.GET() for i in hand.USABLE()])
    hand.KILL(play)
    print(f'i kill {play.GET()}')
    assert len(hand.USABLE()) == 6
    print([i.GET() for i in hand.USABLE()])

    

        