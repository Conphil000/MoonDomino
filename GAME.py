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
        print([i.GET() for i in moves])
        print(check_me)
        print(sum([1 if i[0] and i[1] else 0 for i in check_me]))
        print(sum([1 if i[1] and i[2] else 0 for i in check_me]))
        print(sum([1 if i[2] else 0 for i in check_me]))
        
        
        # [1 if i[1] for i in check_me]
        
        if trump == None:
            ace = [i.ACE() for i in moves]
            
            if sum(ace) > 0:
                idx = ace.index(True)
                print(idx)
                if str(lead_suit) in moves[idx].GET():
                    # print(f'Ace {lead_suit} found')
                    return idx
                
            keep = [i.GET().replace(str(lead_suit),'') if str(lead_suit) in i.GET() else -999 for i in moves]
            
            # print()
            idx = keep.index(str(max([int(i) for i in keep])))
            
            # print(keep,idx)
            return idx
        else:
            raise NotImplementedError
            # ace = [i.ACE() for i in moves]
            # trumps = [i.TRUMP(trump) for i in moves]
            # print(trumps)
            # if sum(trumps) > 0:
                
            #     print([i.GET() if j else -999 for i,j in zip(moves,trumps)])
                
            #     pass
                
            
            
            # if sum(ace) > 0:
            #     idx = ace.index(True)
            #     if (str(lead_suit) in moves[idx].GET()) and (sum(trump) == 0):
            #         pass
            
            
            
            
            
    
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
            
            # print(suit_lead)
            # print([i.GET() for i in player_moves])
            
            # print('Winner IDX')
            # print([i.GET() for i in [m1,m2,m3]])
            # print(self.HAND_WINNER([m1,m2,m3],suit_lead,None))
            self._turn = self.HAND_WINNER([m1,m2,m3],suit_lead,trump)
            print(f'Player {self._turn + 1} Wins.')
            player_pts[self._turn] += 1
            
        # # Check for Winner
        
        print(moves)
        # print(suit_lead)
        print(player_pts)
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
    
    g1 = GAME(players,bone)
    
    assert g1.HAND_WINNER([DOMINO(3,3),DOMINO(2,2),DOMINO(1,5)], 1, None) == 2
    assert g1.HAND_WINNER([DOMINO(3,3),DOMINO(2,2),DOMINO(1,5)], 3, None) == 0
    
    assert g1.HAND_WINNER([DOMINO(3,5),DOMINO(1,1),DOMINO(3,3)], 3, None) == 0
    
    assert g1.HAND_WINNER([DOMINO(5,5),DOMINO(5,3),DOMINO(1,1)], 1, 5) == 0
    
    assert g1.HAND_WINNER([DOMINO(3,3),DOMINO(2,2),DOMINO(1,5)], 3, 2) == 0
    
    for i in players:
        print(i.HAND(True))

    print('and bone',[bone.GET()])
    print()
    print('Try a not so random game.')
    print()
    
    assert g1.RANDOM_GAME() == [3,1,3]
    
    
    
    # random.shuffle(deck.copy()) # Always will get the same deck.
    
    # show_deck(d1)
    
    
    
    # game = GAME([HAND(),HAND(),HAND()])
    
    
    # game.DEAL()
    
    

    












