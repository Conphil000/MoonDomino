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
    def __init__(self,hands,bone = None):
        self._players = hands
        if bone != None:
            self._bone = bone
            
    @staticmethod
    def CYCLE_TURN(turn):
        if turn == 0:
            return 1
        elif turn == 1:
            return 2
        else:
            return 0
    @staticmethod
    def RANDOM_MOVE(moves):
        return random.Random(123).choice(moves)
    @staticmethod
    def HAND_WINNER(moves,lead_suit,trump = None):
        if trump == None:
            
            ace = [i.ACE() for i in moves]
            
            if sum(ace):
                idx = ace.index(True)
                if str(lead_suit) in moves[idx].GET():
                    print(f'Ace {lead_suit} found')
                    return idx
                
            keep = [i.GET().replace(str(lead_suit),'') if str(lead_suit) in i.GET() else -999 for i in moves]
            
            # print()
            idx = keep.index(str(max([int(i) for i in keep])))
            
            # print(keep,idx)
            return idx
        else:
            
            raise NotImplementedError
    
    def RANDOM_GAME(self,starter = 0):
        self._starter = starter
        self._turn = starter
        
        moves = []
        player_moves = [-1] * len(self._players)
        player_pts = [0] * len(self._players)
        trump = None
        
        while sum(player_pts) < 7:
            # print(self._turn)
            
            # print([i.GET() for i in self._players[self._turn].PLAYABLE()])
            
            m1 = self.RANDOM_MOVE(self._players[self._turn].PLAYABLE())
            self._players[self._turn].KILL(m1)
            moves.append(m1.GET())
            player_moves[self._turn] = m1
            
            self._turn = self.CYCLE_TURN(self._turn)
            
            suit_lead = m1.SUIT()
            
            m2 = self.RANDOM_MOVE(self._players[self._turn].PLAYABLE(suit_lead))
            self._players[self._turn].KILL(m2)
            moves.append(m2.GET())
            player_moves[self._turn] = m2
            
            self._turn = self.CYCLE_TURN(self._turn)
            
            m3 = self.RANDOM_MOVE(self._players[self._turn].PLAYABLE(suit_lead))
            self._players[self._turn].KILL(m3)
            moves.append(m3.GET())
            player_moves[self._turn] = m3
            
            print(suit_lead)
            print([i.GET() for i in player_moves])
            
            # print('Winner IDX')
            # print([i.GET() for i in [m1,m2,m3]])
            # print(self.HAND_WINNER([m1,m2,m3],suit_lead,None))
            self._turn = self.HAND_WINNER([m1,m2,m3],suit_lead,trump)
            print(f'Player {self._turn + 1} Wins.')
            player_pts[self._turn] += 1
            
        # # Check for Winner
        
        print(moves)
        print(suit_lead)
        print(player_pts)
        
    
if __name__ == '__main__':
    
    deck = DECK()
    
    for i in [0,1,2]:
        random.Random(123).shuffle(deck)
    
    def show_deck(deck):
        print([i.GET() for i in deck])
    
    show_deck(deck)
    
    players = [HAND(),HAND(),HAND()]
    
    players[0].SET_HAND(deck[:7])
    players[1].SET_HAND(deck[7:14])
    players[2].SET_HAND(deck[14:21])
    bone = deck[21]
    
    g1 = GAME(players,bone)
    
   
    
    for i in players:
        show_deck(i.USABLE())
        
    print('and bone',bone.GET())
    print()
    print('Try a not so random game.')
    print()
    g1.RANDOM_GAME()
    
    # random.shuffle(deck.copy()) # Always will get the same deck.
    
    # show_deck(d1)
    
    
    
    # game = GAME([HAND(),HAND(),HAND()])
    
    
    # game.DEAL()
    
    

    












