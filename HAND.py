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
    def HAND(self,):
        return [i for i in self.USABLE()]
    def STARTER_HAND(self,):
        return [i.GET() for i in self._hand]
    def PLAYABLE(self, lead = None):
        if lead == None:
            lead = 7
        t1 = [i for i in self.HAND() if str(lead) in i.GET()]
        if len(t1) > 0:
            return t1
        else:
            return self.HAND()
    def PLAY(self,DOMINO):
        self.KILL(DOMINO)
    def SET_HAND(self,hand):
        self._hand = hand
        self._usable = len(hand)*[1]
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
    print(hand.HAND())
    print()
    
    # Let's say someone played the 32, This is a 3 in this case. Trump is a 5.
    print('New Hand')
    hand2 = HAND()
    hand2.ADD(DOMINO(1,6))
    hand2.ADD(DOMINO(1,3))
    hand2.ADD(DOMINO(3,6))
    hand2.ADD(DOMINO(3,4))
        
    def show_deck(deck):
        print([i.GET() for i in deck])
        
    print(show_deck((hand2.HAND())))
    print('If 3 is lead you could play')
    print(show_deck(hand2.PLAYABLE(3)))
    assert len(hand2.PLAYABLE(3)) == 3
    print(show_deck(hand2.HAND()))
    print('If 5 is lead you could play')
    print(show_deck(hand2.PLAYABLE(5)))
    assert len(hand2.PLAYABLE(5)) == 4
    print(show_deck(hand2.HAND()))
    print('If 6 is lead you could play')
    print(show_deck(hand2.PLAYABLE(6)))
    assert len(hand2.PLAYABLE(6)) == 2
    
    


        