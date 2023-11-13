from ScreenBaseModule import ScreenBase
from BackgroundModule import Background
from ButtonModule import Button
from GameEndScreenModule import GameEndScreen
import globals
import pygame
from func1 import *
from special_card import *
from AI_logic import *
from StackAnimationModule import *
from CardAnimationModule import *

#[3]Game Start Screen: 
# UI: (photo of the player, 
# user draw card from stack animation, 
# user play card animation,
# user mouse hover animation): Jiayao Song

# rest of the UI: Xiaochi,Ce Liu, Ranjith, Yuchen Zhou

# Logic/AI: Xiaochi, Ce Liu, Ranjith

#Jiayao Song - Idea: 
# 1、when mouse hover the card, the y postion of the card will -10
# 2、when user draw card from the stack, there will be an animation
# 3、when user play a card, there will be an animation (known two points and calculate a line)
# 4、the photo of the player will light up in that player's turn



class GameMainPlayScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        
        #get photos of player from Matching screen
        self.player_photo_list = globals.player_photo_list
        self.player_photo_list[0].startPoint = (0.03*globals.screen_current_width,0.8*globals.screen_current_height)
        self.player_photo_list[1].startPoint = (0.03*globals.screen_current_width,0.04*globals.screen_current_height)
        self.player_photo_list[2].startPoint = (0.9*globals.screen_current_width,0.04*globals.screen_current_height)
        self.player_photo_list[3].startPoint = (0.9*globals.screen_current_width,0.8*globals.screen_current_height)
        
        #setup the animations
        self.stack_animation = StackAnimation()
        self.stack = False
        self.play_card_animation = CardAnimation('images/Back.png',(5,5),(8,8))
        self.user_card_to_play = None
        self.play_card = False
        
        #change all photos to disable state
        for player_photo in self.player_photo_list:
            player_photo.image = pygame.transform.scale(player_photo.image_original_disable,(player_photo.width,player_photo.height))
           

    def draw(self,surface):
        # Blitting essential Images
        surface.blit(globals.img.bg, (0, 0))
        surface.blit(globals.img.back, (10, 10))
        surface.blit(globals.img.card_back, (340, 240))
        try:
            surface.blit(pygame.image.load("./images/" + globals.ess.current[1] + str(globals.ess.current[0]) + ".png"), (580, 240))
        except:
            surface.blit(pygame.image.load("./images/" + globals.ess.current[1] + ".png"), (580, 240))

        # Mouse click Check
        if pygame.mouse.get_pressed()[0]==1:
            m = pygame.mouse.get_pos()  # Fetching mouse click location
            # Card click operations
            if globals.ess.player_playing:  
                if 850 < m[0] < 916 and 500 < m[1] < 565:  # UNO button
                    globals.ess.uno[0] = True
                if 775 < m[0] < 840 and 505 < m[1] < 570:  # End turn button
                    globals.ess.player_playing = False
                for i in range(625, 625 - 50 * len(globals.ess.player_list[0]), -50):  # Detecting the card clicked by user
                    if i < m[0] < i + 50 and 470 < m[1] < 585:
                        if not globals.ess.played:
                            #(Jiayao-idea3)   
                            self.play_card = True #going to animation
                            self.user_card_to_play = globals.ess.player_list[0][int((625 - i) / 50)]
                            try:
                                self.play_card_animation.image = pygame.image.load("./images/" + self.user_card_to_play[1] + str(self.user_card_to_play[0]) + ".png")
                            except:
                                self.play_card_animation.image = pygame.image.load("./images/" + self.user_card_to_play[1] + ".png")
                            
                            self.play_card_animation.start = (i-35,-470) #get start vector
                            self.play_card_animation.end = (580,-240) #get end vector
                            
                            #calculating #x = (b-y)/a
                            self.play_card_animation.a = (-240+470)/(580-(i-35)) 
                            self.play_card_animation.b = -240-(self.play_card_animation.a*580)

                #take one new card
                if 340 < m[0] < 425 and 240 < m[1] < 355:
                    if globals.ess.drawn==False:
                        #(Jiayao-idea2)
                        self.stack = True #going to animation
                    

            # Post black card operation, New color picker
            if globals.ess.choose_color:
                if 395 < m[0] < 440 and 390 < m[1] < 450:  # Red Button
                    globals.ess.choose_color = False
                    globals.flag = play_this_card_2(globals.ess, "Red")
                if 450 < m[0] < 495 and 390 < m[1] < 450:  # Green Button
                    globals.ess.choose_color = False
                    globals.flag = play_this_card_2(globals.ess, "Green")
                if 505 < m[0] < 550 and 390 < m[1] < 450:  # Blue Button
                    globals.ess.choose_color = False
                    globals.flag = play_this_card_2(globals.ess, "Blue")
                if 560 < m[0] < 605 and 390 < m[1] < 450:  # Yellow Button
                    globals.ess.choose_color = False
                    globals.flag = play_this_card_2(globals.ess, "Yellow")
        
        # Checking for winner
        for i in globals.ess.player_list:
            if len(i) == 0:
                globals.win_dec = True
                globals.ess.winner = globals.ess.player_list.index(i)
                globals.current_screen = GameEndScreen()
        
        #(Jiayao-idea2) #check if the draw card from stack animation is finished
        if self.stack:
            if self.stack_animation.move_finish==False:
                self.stack_animation.move(surface,470)
            if self.stack_animation.move_finish==True:
                #use function when animation finish
                take_from_stack(globals.ess)
                self.stack_animation.adding = 0
                self.stack_animation.image_alpha = 255
                self.stack_animation.move_finish = False
                self.stack = False

        #(Jiayao-idea3) #check if the play card animation is finished
        if self.play_card:
            if self.play_card_animation.get_move_finish()==False:               
                self.play_card_animation.move(surface,240,470)
            if self.play_card_animation.get_move_finish()==True:
                #use function when animation finish
                globals.flag = play_this_card(globals.ess, self.user_card_to_play)
                self.play_card_animation.adding = 0
                self.play_card_animation.image_alpha = 255
                self.play_card_animation.move_finish = False
                self.play_card = False

        text = pygame.font.Font(globals.fnt.joe_fin, 20).render(globals.ess.information, True, (255, 238, 46))
        surface.blit(text, [340, 210])

        for i in range(len(globals.ess.player_list[1])):
            surface.blit(globals.img.card_back_l, (40, 315 - 30 * i))
        for i in range(len(globals.ess.player_list[2])):
            surface.blit(globals.img.card_back_i, (380 + 30 * i, 20))
        for i in range(len(globals.ess.player_list[3])):
            surface.blit(globals.img.card_back_r, (845, 190 + 30 * i))
        for i in range(len(globals.ess.player_list[0])):
            m = pygame.mouse.get_pos()

            #(Jiayao-idea1) mouse hover interaction
            if (590 - 50 * i) + 35 < m[0] < (590 - 50 * i) + 85 and 470 < m[1] < 585:
                surface.blit(
                    pygame.image.load("./images/" + globals.ess.player_list[0][i][1] + str(globals.ess.player_list[0][i][0]) + ".png"),
                    (590 - 50 * i, 460))
            else:
                surface.blit(
                    pygame.image.load("./images/" + globals.ess.player_list[0][i][1] + str(globals.ess.player_list[0][i][0]) + ".png"),
                    (590 - 50 * i, 470))

        if globals.ess.choose_color:
            surface.blit(globals.img.red, (395, 390))
            surface.blit(globals.img.green, (450, 390))
            surface.blit(globals.img.blue, (505, 390))
            surface.blit(globals.img.yellow, (560, 390))

        # Play Flow
        if globals.ess.player_playing ==True:  # Player is playing
            globals.ess.information = ""
            if not globals.ess.drawn and not globals.ess.played:  # Checking for previous special card overheads
                    if globals.ess.current[0] == '+2' and globals.ess.special_check == 0:  # Draw 2
                        for _ in range(2):
                            try:
                                globals.ess.player_list[0].append(globals.ess.deck1.pop())
                            except:
                                globals.ess.deck1, globals.ess.deck2 = globals.ess.deck2, globals.ess.deck1
                                random.shuffle(globals.ess.deck1)
                                globals.ess.player_list[0].append(globals.ess.deck1.pop())
                        globals.ess.special_check = 1
                        globals.ess.player_playing = False

                    elif globals.ess.current[0] == '+4' and globals.ess.special_check == 0:  # Draw 4
                        for _ in range(4):
                            try:
                                globals.ess.player_list[0].append(globals.ess.deck1.pop())
                            except:
                                globals.ess.deck1, globals.ess.deck2 = globals.ess.deck2, globals.ess.deck1
                                random.shuffle(globals.ess.deck1)
                                globals.ess.player_list[0].append(globals.ess.deck1.pop())
                        globals.ess.special_check = 1
                        globals.ess.player_playing = False

            #player1 photo light up #(Jiayao-idea4)
            self.player_photo_list[0].image = pygame.transform.scale(self.player_photo_list[0].image_original_active,(self.player_photo_list[0].width,self.player_photo_list[0].height))
            self.player_photo_list[1].image = pygame.transform.scale(self.player_photo_list[1].image_original_disable,(self.player_photo_list[1].width,self.player_photo_list[1].height))
            self.player_photo_list[2].image = pygame.transform.scale(self.player_photo_list[2].image_original_disable,(self.player_photo_list[2].width,self.player_photo_list[2].height))
            self.player_photo_list[3].image = pygame.transform.scale(self.player_photo_list[3].image_original_disable,(self.player_photo_list[3].width,self.player_photo_list[3].height))

            surface.blit(globals.img.done, (775, 505))
            surface.blit(globals.img.uno_button, (850, 500))

        else: #AI is playing
            if globals.ess.play_lag == 140:  # Implementing Lag between 2 players actions
                globals.disp = False
                globals.pen_check = False

                # Getting current playing players index
                set_curr_player(globals.ess, True)

                # Checking if it's players turn
                if globals.ess.position == 0:
                    globals.ess.uno[0] = False
                    globals.ess.player_playing = True

                else:
                    # Reinitialising player flags
                    globals.ess.played = False
                    globals.ess.drawn = False

                    # Making the bot play
                    AI_card_logic(globals.ess)

                globals.ess.play_lag = 0  # Resetting lag

            else:
                if globals.win_dec and globals.ess.play_lag == 70:  # Winner declare lag
                    globals.ess.play_mode = globals.pm.win

                if not globals.pen_check:  # Penalty check algorithm
                    if globals.ess.position != -1 and len(globals.ess.player_list[globals.ess.position]) == 1 and not globals.ess.uno[
                        globals.ess.position]:  # Penalty
                        for j in range(4):
                            if globals.ess.position != j:
                                globals.ess.player_list[globals.ess.position].append(globals.ess.player_list[j].pop())
                                break

                        globals.ess.information = "Penalty!"
                        globals.ess.uno[globals.ess.position] = True
                    globals.pen_check = True

                globals.ess.play_lag += 1

                if not globals.disp:
                    globals.disp = True

                # Active player graphic line
                if (globals.ess.position + globals.ess.direction_check) % 4 == 1:
                    #player2 photo light up #(Jiayao-idea4)
                    self.player_photo_list[1].image = pygame.transform.scale(self.player_photo_list[1].image_original_active,(self.player_photo_list[1].width,self.player_photo_list[1].height))
                    self.player_photo_list[0].image = pygame.transform.scale(self.player_photo_list[0].image_original_disable,(self.player_photo_list[0].width,self.player_photo_list[0].height))
                    self.player_photo_list[2].image = pygame.transform.scale(self.player_photo_list[2].image_original_disable,(self.player_photo_list[2].width,self.player_photo_list[2].height))
                    self.player_photo_list[3].image = pygame.transform.scale(self.player_photo_list[3].image_original_disable,(self.player_photo_list[3].width,self.player_photo_list[3].height))

                elif (globals.ess.position + globals.ess.direction_check) % 4 == 2:
                    #player3 photo light up #(Jiayao-idea4)
                    self.player_photo_list[2].image = pygame.transform.scale(self.player_photo_list[2].image_original_active,(self.player_photo_list[2].width,self.player_photo_list[2].height))
                    self.player_photo_list[1].image = pygame.transform.scale(self.player_photo_list[1].image_original_disable,(self.player_photo_list[1].width,self.player_photo_list[1].height))
                    self.player_photo_list[0].image = pygame.transform.scale(self.player_photo_list[0].image_original_disable,(self.player_photo_list[0].width,self.player_photo_list[0].height))
                    self.player_photo_list[3].image = pygame.transform.scale(self.player_photo_list[3].image_original_disable,(self.player_photo_list[3].width,self.player_photo_list[3].height))
                elif (globals.ess.position + globals.ess.direction_check) % 4 == 3:
                    #player4 photo light up #(Jiayao-idea4)
                    self.player_photo_list[3].image = pygame.transform.scale(self.player_photo_list[3].image_original_active,(self.player_photo_list[3].width,self.player_photo_list[3].height))
                    self.player_photo_list[1].image = pygame.transform.scale(self.player_photo_list[1].image_original_disable,(self.player_photo_list[1].width,self.player_photo_list[1].height))
                    self.player_photo_list[2].image = pygame.transform.scale(self.player_photo_list[2].image_original_disable,(self.player_photo_list[2].width,self.player_photo_list[2].height))
                    self.player_photo_list[0].image = pygame.transform.scale(self.player_photo_list[0].image_original_disable,(self.player_photo_list[0].width,self.player_photo_list[0].height))
    
        #(Jiayao-idea4)
        self.player_photo_list[0].draw(surface)
        self.player_photo_list[1].draw(surface)
        self.player_photo_list[2].draw(surface)
        self.player_photo_list[3].draw(surface)
