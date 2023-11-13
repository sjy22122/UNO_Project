import random
from special_card import *

def AI_card_logic(message):
    """Bot logic"""
    message.information = ""
    message.uno[message.position] = False
    message.check = 0
    if (message.current[0] == '+2' or message.current[0] == '+4') and message.special_check == 0:
        handle24(message, int(message.current[0][1]))
        message.played_check = 1
    else:
        check = 0
        for item in message.player_list[message.position]:
            if message.current[1] in item or message.current[0] in item:
                AI_play_card(message, item)
                if item[1] == 'Black':
                    handle_black(message, item)
                message.player_list[message.position].remove(item)
                set_curr_player(message, False)
                check = 1
                break
        if check == 0:
            black_check = 0
            for item in message.player_list[message.position]:
                if 'Black' in item:
                    message.information = "%s plays %s" % (message.bot_map[message.position], item[0] + " " + item[1])
                    handle_black(message, item)
                    message.player_list[message.position].remove(item)
                    black_check = 1
                    break
            if black_check == 0:
                if len(message.deck1) > 0:
                    new_card = (message.deck1.pop())
                else:
                    random.shuffle(message.deck2)
                    message.deck1 = message.deck2
                    message.deck2.clear()
                    new_card = (message.deck1.pop())
                message.information = "%s draws a card" % message.bot_map[message.position]
                if new_card[1] == 'Black':
                    message.information = "%s plays %s" % (message.bot_map[message.position], new_card[0] + " " + new_card[1])
                    handle_black(message, new_card)
                elif new_card[1] == message.current[1] or new_card[0] == message.current[0]:
                    AI_play_card(message, new_card)
                else:
                    message.player_list[message.position].append(new_card)
        if len(message.player_list[message.position]) == 1:
            probability = random.randint(0, 1)
            if probability == 1:
                message.uno[message.position] = True
                message.information = "%s shouted UNO!" % message.bot_map[message.position]
def AI_play_card(message, card):
    """AI出牌"""
    message.special_check = 0
    message.deck2.append(card)
    message.current = card
    message.information = "%s plays card %s" % (message.bot_map[message.position], card[1] + " " + card[0])