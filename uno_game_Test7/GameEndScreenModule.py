from ScreenBaseModule import ScreenBase
from BackgroundModule import Background
import globals
import pygame

#[4]End Game Screen: Yuchen Zhou
#used the variables from classes.py
#transfer variables from other screens

#My Idea: 
# 1、print the winner
# 2、calculate the all the scores and print them
# 3、print the photo of winner on the blackboard
# 4、add an new image (design refine)

class GameEndScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.background = Background('images/background.png')

        #get the photos and names of a list of players
        self.player_photo_list = globals.player_photo_list
        self.player_list = globals.player_list

        self.objects.append(self.background)
        
        #points of each player
        i=0
        score = 0
        score_1 = 0
        score_2 = 0
        score_3 = 0
        numSet = set([str(i) for i in range(10)])
        
        for cards in globals.ess.player_list[0]:
            for card in cards:
                if card[0] in numSet:
                    score += int(card[0])
                elif card[0] in ['Skip','Reverse','+2']:
                    score += 20
                elif card[0] == 'Wild':
                    score += 50
                else:
                    pass
        self.p1_points = score 

        for cards in globals.ess.player_list[1]:
            for card in cards:
                if card[0] in numSet:
                    score_1 += int(card[0])
                elif card[0] in ['Skip','Reverse','+2']:
                    score_1 += 20
                elif card[0] == 'Wild':
                    score_1 += 50
                else:
                    pass
        self.p2_points = score_1 

        for cards in globals.ess.player_list[2]:
            for card in cards:
                if card[0] in numSet:
                    score_2 += int(card[0])
                elif card[0] in ['Skip','Reverse','+2']:
                    score_2 += 20
                elif card[0] == 'Wild':
                    score_2 += 50
                else:
                    pass
        self.p3_points = score_2

        for cards in globals.ess.player_list[3]:
            for card in cards:
                if card[0] in numSet:
                    score_3 += int(card[0])
                elif card[0] in ['Skip','Reverse','+2']:
                    score_3 += 20
                elif card[0] == 'Wild':
                    score_3 += 50
                else:
                    pass
        self.p4_points = score_3

        for player_photo in self.player_photo_list:
            player_photo.image = pygame.transform.scale(player_photo.image_original,(player_photo.width,player_photo.height))

        #get the photo of the winner
        self.winner_photo = self.player_photo_list[globals.ess.winner]
        self.winner_photo.startPoint = (0.03*globals.screen_current_width,0.8*globals.screen_current_height)

    def draw(self,surface):
        super().draw(surface)

        # Setting up appropriate information
        if globals.ess.winner == 0:
            self.string = "Nice! You've won!"
        else:
            self.string = "%s has won!" % globals.ess.bot_map[globals.ess.winner]

        #Rendering and blitting
        surface.blit(globals.img.win, (0, 0))
        surface.blit(globals.img.again,(450,100))

        text = pygame.font.Font(None, 50).render(
             self.string, True, (255, 238, 46))
        surface.blit(text, [100, 95])
        
        #print all the scores on the screen
        self.string = str(self.p1_points)
        text = pygame.font.Font(None, 40).render(
             self.string, True, (255, 238, 46))
        surface.blit(text, [200, 200])

        self.string = str(self.p2_points)
        text = pygame.font.Font(None, 40).render(
             self.string, True, (255, 238, 46))
        surface.blit(text, [200, 250])

        self.string = str(self.p3_points)
        text = pygame.font.Font(None, 40).render(
             self.string, True, (255, 238, 46))
        surface.blit(text, [200, 300])

        self.string = str(self.p4_points)
        text = pygame.font.Font(None, 40).render(
             self.string, True, (255, 238, 46))
        surface.blit(text, [200, 350])

        self.string_1 = "P1"
        text_1 = pygame.font.Font(None, 40).render(
             self.string_1, True, (255, 238, 46))
        surface.blit(text_1, [100, 200])

        self.string_1 = "P2"
        text_1 = pygame.font.Font(None, 40).render(
             self.string_1, True, (255, 238, 46))
        surface.blit(text_1, [100, 250])

        self.string_1 = "P3"
        text_1 = pygame.font.Font(None, 40).render(
             self.string_1, True, (255, 238, 46))
        surface.blit(text_1, [100, 300])

        self.string_1 = "P4"
        text_1 = pygame.font.Font(None, 40).render(
             self.string_1, True, (255, 238, 46))
        surface.blit(text_1, [100, 350])
        
        self.string_1 = "Score"
        text_1 = pygame.font.Font(None, 40).render(
             self.string_1, True, (255, 238, 46))
        surface.blit(text_1, [200, 150])

        self.winner_photo.draw(surface)


    