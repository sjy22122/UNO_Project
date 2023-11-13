import itertools
import random
import pygame
from StackAnimationModule import *

def peek(s):
    """Peek"""
    return s[-1]


def create(ob):
    """Dealing the cards"""
    a = ('0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9',
         '+2', '+2', 'Skip', 'Skip', 'Reverse', 'Reverse')
    ob.deck1 = list(itertools.product(a, ob.color))  # Deck created
    for _ in range(4):  # Adds special black cards to decks
        ob.deck1.append(('Wild', 'Black'))
        ob.deck1.append(('+4', 'Black'))
    random.shuffle(ob.deck1)  # Shuffles deck

    while peek(ob.deck1) in [('Wild', 'Black'), ('+4', 'Black'), ('Skip', 'Red'), ('Skip', 'Green'),
                             ('Skip', 'Blue'), ('Skip', 'Yellow'), ('Reverse', 'Red'), ('Reverse', 'Green'),
                             ('Reverse', 'Blue'), ('Reverse', 'Yellow'), ('+2', 'Red'), ('+2', 'Green'),
                             ('+2', 'Blue'), ('+2', 'Yellow')]:  # First card cannot be special card
        random.shuffle(ob.deck1)

    ob.deck2.append(ob.deck1.pop())  # Shifts first card to played deck
    ob.current = peek(ob.deck2)  # Peek from played deck

    for j in range(4):  # Deals cards to player
        for _ in range(7):
            ob.player_list[j].append(ob.deck1.pop())

    # ob.player_list[0] = [('Wild', 'Black'), ('+4', 'Black'), ('Skip', 'Red'), ('Reverse', 'Green'), ("+2", "Blue")]


def set_curr_player(ob, default):
    """Decides next player"""
    if ob.current[0] == 'Reverse' and ob.special_check == 0:
        ob.direction_check *= -1  # Direction reversed
        ob.special_check = 1  # Special card status inactive
    if ob.current[0] == 'Skip' and ob.special_check == 0:
        ob.special_check = 1
        ob.position = (ob.position + ob.direction_check) % 4

    if default:
        ob.position = (ob.position + ob.direction_check) % 4


def re_initialize(ob):
    """Reinitialize all the game variables and flags"""
    ob.message = ""  # To print message
    ob.winner = -1
    ob.player_playing = False
    ob.play_lag = -1
    ob.player_list = [[], [], [], []]
    ob.deck1 = list()
    ob.deck2 = list()
    ob.direction_check = 1  # Flag to check direction of play
    ob.position = -1  # Position counter
    ob.special_check = 0  # Flag to check status of special card
    ob.current = tuple()
    ob.drawn, ob.played, ob.choose_color = False, False, False
    ob.uno = [True] * 4
    ob.easy = True

    # Dealing the cards
    create(ob)



def take_from_stack(ob):
    """Draw card from stack by user"""
    if not ob.drawn:
        try:
            ob.player_list[0].append(ob.deck1.pop())
        except:
            ob.deck1, ob.deck2 = ob.deck2, ob.deck1
            random.shuffle(ob.deck1)
            ob.player_list[0].append(ob.deck1.pop())
        finally:
            ob.drawn = True


def play_this_card(ob, card):
    """Play card by user"""
    if not ob.played:
        if (card[0] == ob.current[0] or card[1] == ob.current[1]) and (card[0] not in ('+4', 'Wild')):
            ob.played, ob.drawn = True, True
            ob.deck2.append(card)
            ob.current = peek(ob.deck2)
            ob.player_list[0].remove(ob.current)
            ob.special_check = 0
            set_curr_player(ob, False)
            
        if card[1] == 'Black':
            ob.played, ob.drawn = True, True
            ob.choose_color = True
            ob.player_list[0].remove(card)
            ob.deck2.append(card)
            
    return True

def play_this_card_2(ob, color):
    """Post color selection"""
    ob.deck2[-1] = (ob.deck2[-1][0], color)
    ob.current = peek(ob.deck2)
    ob.special_check = 0
    return True
