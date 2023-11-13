import random
from func1 import *

def handle24(ob, n):
    """Handles +2 and +4 cards"""
    for i in range(n):
        if len(ob.deck1) != 0:
            card_name = ob.deck1.pop()
            ob.player_list[ob.position].append(card_name)
        else:
            tmp = ob.deck2
            ob.deck2 = ob.deck1
            ob.deck1 = tmp
            random.shuffle(ob.deck1)
            card_name = ob.deck1.pop()
            ob.player_list[ob.position].append(card_name)
    ob.information = "{} Draws {} cards".format(ob.bot_map[ob.position], n)
    ob.special_check = 1

def handle_black(ob, item):
    """Handles black cards"""
    ob.special_check = 0
    ob.deck2.append(item)
    ob.current = peek(ob.deck2)
    new_color = random.choice(ob.color)  
    ob.information = "{} plays {} {}, new color is {}".format(ob.bot_map[ob.position], item[0], item[1], new_color)
    ob.current = (ob.current[0], new_color)
