# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# This is a Domino, u can flip me, u can print me, u can get me, u can look if i a trump.

import numpy as np 

class DOMINO:
    def __init__(self, s1, s2):
        self._s1 = s1
        self._s2 = s2
    def GET(self,):
        return f'{self._s1}{self._s2}'
    def FLIP(self,):
        temp = self._s1
        self._s1 = self._s2
        self._s2 = temp
    def ACE(self,):
        return self._s1 == self._s2
    def SUIT(self,TRUMP = None):
        if TRUMP != None:
            if str(TRUMP) in self.GET():
                return TRUMP
        return max(self._s1,self._s2)
    def BEAT(self,):
        beats = [1,2,3,4,5,6]
        if self.__ACE():
            beats.remove(self._s1)
            return beats
        else:
            beats = np.array(beats)
            beats = beats[beats < min(self._s1,self._s2)]
            return list(beats)
    
if __name__ == '__main__':
    
    hand  = [DOMINO(2,1),DOMINO(3,3),DOMINO(6,2)]
    
    def is_ace(x):
        return int(x.ACE())
    def get_suit(x,TRUMP = None):
        return x.SUIT(TRUMP)
    
    assert sum([1 if i == 2 else 0 for i in list(map(get_suit,hand,[2]*len(hand)))]) == 2
    assert sum(map(is_ace,hand)) == 1




