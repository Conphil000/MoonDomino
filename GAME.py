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
        
        trump = 7 if trump == None else trump
        
        is_ace = [i.ACE() for i in moves]
        is_trump = [i.TRUMP(trump) for i in moves]
        is_suit = [str(lead_suit) in i.GET() for i in moves]
        
        # ace_trump > trump > ace > max_suit
        
        check_me = [(i,j,k) for i,j,k in zip(is_ace,is_trump,is_suit)]
        
        cond1 = [1 if i[0] and i[1] else 0 for i in check_me] # Ace Trump is Played
        cond4 = [1 if i[1] else 0 for i in check_me] # A Trump has been played.
        
        cond2 = [1 if i[0] and i[2] else 0 for i in check_me] # Ace of Suit is Played
        cond3 = [1 if i[2] else 0 for i in check_me]
        
        # Ace Trump
        if sum(cond1) == 1:
            # This means that someone played the ace trump, they will win.
            return cond1.index(1)
        
        # Any Trump
        if sum(cond4) == 1: # One Person played a trump 
            return cond4.index(1)
        elif sum(cond4) > 1: # More that one person played a trump
            t_idx = [int(i.GET().replace(str(trump),'')) if j else -999 for i,j in zip(moves,is_trump)]
            return t_idx.index(max(t_idx))
        
        # Ace Suit
        # print(check_me)
        if sum(cond2) == 1: # Someone played the ace of suit
            return cond2.index(1)
        
        # Someone played a lower Suit
        # print([i.GET().replace(str(lead_suit),'') if j else -999 for i,j in zip(moves,cond3)])
        
        t_idx = [int(i.GET().replace(str(lead_suit),'')) if j else -999 for i,j in zip(moves,cond3)]
        return t_idx.index(max(t_idx))
    
    def RESET_GAME(self,):
        [i.RESET_HAND() for i in self._players]
    def RANDOM_GAME(self,starter = 0,set_trump = None):
        self._starter = starter
        self._turn = starter
        
        moves = []
        
        player_moves = [-1] * len(self._players)
        player_pts = [0] * len(self._players)
        trump = set_trump
        
        while sum(player_pts) < 7:
            # print(self._turn)
            # print([i.GET() for i in self._players[self._turn].PLAYABLE()])
            
            m1 = self.RANDOM_MOVE(self._players[self._turn].PLAYABLE())
            self._players[self._turn].KILL(m1)
            
            player_moves[self._turn] = m1
            
            print(f'Player {self._turn+1} leads with {m1.GET()}')
            
            self._turn = self.CYCLE_TURN(self._turn)
            
            suit_lead = m1.SUIT()
            
            m2 = self.RANDOM_MOVE(self._players[self._turn].PLAYABLE(suit_lead))
            self._players[self._turn].KILL(m2)
            
            player_moves[self._turn] = m2
            
            self._turn = self.CYCLE_TURN(self._turn)
            
            m3 = self.RANDOM_MOVE(self._players[self._turn].PLAYABLE(suit_lead))
            self._players[self._turn].KILL(m3)
           
            player_moves[self._turn] = m3
            
            # print(suit_lead)
            # print([i.GET() for i in player_moves])
            
            # print('Winner IDX')
            # print([i.GET() for i in [m1,m2,m3]])
            # print(self.HAND_WINNER([m1,m2,m3],suit_lead,None))
            moves.append([i.GET() for i in player_moves])
            self._turn = self.HAND_WINNER(player_moves,suit_lead,trump)
            print(f'Player {self._turn + 1} wins with {player_moves[self._turn].GET()}.')
            player_pts[self._turn] += 1
            
        # # Check for Winner
        
        print(moves)
        # print(suit_lead)
        print(player_pts)
        g1.RESET_GAME()
        return player_pts
    
if __name__ == '__main__':
    
    deck1 = DECK()
    
    player = HAND()
    player.ADD_HAND(deck1[:7])
    
    player.KILL(player.PLAYABLE()[0])
    player._hand
    
    deck = DECK()
    
    for i in [0,1,2]:
        random.Random(123).shuffle(deck)
    
    def show_deck(deck):
        return [i.GET() for i in deck]
    
    show_deck(deck)
    
    players = [HAND(),HAND(),HAND()]
    
    players[0].ADD_HAND(deck[:7])
    players[1].ADD_HAND(deck[7:14])
    players[2].ADD_HAND(deck[14:21])
    
    bone = deck[21]
    
    g1 = GAME(players.copy(),bone)
    
    assert g1.HAND_WINNER([DOMINO(3,3),DOMINO(2,2),DOMINO(1,5)], 1, None) == 2
    assert g1.HAND_WINNER([DOMINO(3,3),DOMINO(2,2),DOMINO(1,5)], 3, None) == 0
    assert g1.HAND_WINNER([DOMINO(3,5),DOMINO(1,1),DOMINO(3,3)], 3, None) == 2
    
    assert g1.HAND_WINNER([DOMINO(5,5),DOMINO(5,3),DOMINO(1,1)], 1, 5) == 0
    assert g1.HAND_WINNER([DOMINO(6,4),DOMINO(4,3),DOMINO(2,2)], 4, None) == 0
    assert g1.HAND_WINNER([DOMINO(3,3),DOMINO(2,2),DOMINO(1,5)], 3, 2) == 1
    
    for i in players:
        print(i.HAND(True))
    print('and bone',[bone.GET()])
    print()
    print('Try a not so random game.')
    print()
    
    assert g1.RANDOM_GAME() == [1,5,1]
    
    assert g1.RANDOM_GAME(1) == [1,2,4]
    
    assert g1.RANDOM_GAME(2) == [1,2,4]
    
    out = {}
    for i in [0,1,2]:
        for j in [1,2,3,4,5,6]:
            out[f'{i}{j}'] = max(g1.RANDOM_GAME(i,j))
            
    assert g1.RANDOM_GAME(2,6) == [2,0,5]
    
    
    
    
    

    












