# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 22:10:53 2022

@author: Conor
"""
import random

class HAND:
    def __init__(self,):
        self._hand = {}
        
    def ADD_HAND(self,HAND):
        self._hand = dict(zip(HAND,[True]*len(HAND)))
        
    def ADD_DOMINO(self,DOMINO): # Maybe will be used for Adding Bone?
        self._hand[DOMINO] = True
        
    def USABLE(self,):
        usable = []
        for i in self._hand:
            if self._hand[i]:
                usable.append(i)
        return usable
    
    def KILL(self,DOMINO):
        if isinstance(DOMINO,str):
            raise NotImplementedError
            for i in self._hand:
                if i.GET() == DOMINO:
                    self._hand[i] = False
        else:
            self._hand[DOMINO] = False
            
    def PLAY(self,DOMINO):
        self.KILL(DOMINO)
        
    def HAND(self,string = False):
        if string:
            return [i.GET() for i in self._hand.keys()]
        else:
            return list(self._hand.keys())
    
    def PLAYABLE(self, lead = None):
        if lead == None:
            lead = 7
            
        play = []
        
        for i,j in self._hand.items():
            if j:
                if str(lead) in i.GET():
                    play.append(i)
                    
        if len(play) > 0:
            return play
        else:
            return [i for i,j in self._hand.items() if j == True]
        
if __name__ == '__main__':
    from DOMINO import DOMINO
    
    hand = HAND()
    
    for i in range(0,7):
        hand.ADD_DOMINO(DOMINO(random.randint(1, 6),random.randint(1, 6)))
        
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
    hand2.ADD_DOMINO(DOMINO(1,6))
    hand2.ADD_DOMINO(DOMINO(1,3))
    hand2.ADD_DOMINO(DOMINO(3,6))
    hand2.ADD_DOMINO(DOMINO(3,4))
        
    def show_deck(deck):
        return [i.GET() for i in deck]
        
    print((hand2.HAND(True)))
    print('If 3 is lead you could play')
    print(show_deck(hand2.PLAYABLE(3)))
    assert len(hand2.PLAYABLE(3)) == 3
    print((hand2.HAND(True)))
    print('If 5 is lead you could play')
    print(show_deck(hand2.PLAYABLE(5)))
    assert len(hand2.PLAYABLE(5)) == 4
    print((hand2.HAND(True)))
    print('If 6 is lead you could play')
    print(show_deck(hand2.PLAYABLE(6)))
    assert len(hand2.PLAYABLE(6)) == 2
    
    


        