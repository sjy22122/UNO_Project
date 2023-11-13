import pygame
import globals
import random
from ScreenBaseModule import ScreenBase
from BackgroundModule import Background
from ButtonModule import Button
from TurntableModule import Turntable
from ProfilePhotoModule import ProfilePhoto
from GameMainPlayScreenModule import GameMainPlayScreen

#[2]Game Start Screen: Jiayao Song

#My Idea: 
# 1、the screen should be able to select the numbers of player in a game
# 2、make photos to 6 players, then choose who will play this game by using the turntable
# 3、click the 'add player' button, the turntable will work and pick a player
# 4、each player won't be selected twice
# 5、the photo of the player should show up only after animation of the turntable has been finished
# 6、when 4 players are selected, the 'start' button is active
# 7、when 'start' button is active and clicked, game will start and jump to next screen
# 8、the data from this screen(such as player list, player photo list,..) 
#       should be able to transfer to next screen


class GameMatchingScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.player_count = 0
        x_of_player_profile = globals.screen_current_width * (1-0.5) * 0.5
        y_of_player_profile = globals.screen_current_height * (1-0.4)
        profile_gap_width = 50
        self.rotate_degree = 0
        self.select_list = [] #the degree has been picked
        self.player_list = []

        self.background = Background('./images/background_Game_pureColour.png')
        self.turntable = Turntable('./images/turntable.png',0.45)
        self.add_button = Button(0,250,'./images/button_add_player.jpg',0.3,"center")
        self.add_button_disable = Button(0,250,'./images/button_add_player_disable.png',0.3,"center")
        self.submit_button = Button(0,480,'./images/button_start_mainGame.jpg',0.4,"center")
        self.submit_button_disable = Button(0,480,'./images/button_start_mainGame_disable.png',0.4,"center")
        self.arrow = Button(0,180,'images/arrow.png',0.13,"center")

        self.player1_photo = ProfilePhoto(x_of_player_profile,y_of_player_profile,'./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png',0.22,"")
        self.player2_photo = ProfilePhoto(x_of_player_profile+(self.player1_photo.width*1)+(profile_gap_width*1),y_of_player_profile,'./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png',0.22,"")
        self.player3_photo = ProfilePhoto(x_of_player_profile+(self.player1_photo.width*2)+(profile_gap_width*2),y_of_player_profile,'./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png',0.22,"")
        self.player4_photo = ProfilePhoto(x_of_player_profile+(self.player1_photo.width*3)+(profile_gap_width*3),y_of_player_profile,'./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png','./images/profilePhoto_noPhoto.png',0.22,"")

        self.objects.append(self.background)
        self.objects.append(self.player1_photo)
        self.objects.append(self.player2_photo)
        self.objects.append(self.player3_photo)
        self.objects.append(self.player4_photo)


    def draw(self,surface):
        super().draw(surface)

        if self.player_count <4:
            self.add_button.draw(surface)
            if self.add_button.get_result():
                if self.player_count == 0: #user clicked the 'add' button first time
                    self.rotate_degree = random.randint(0,360)
                    self.select_list.append(self.rotate_degree)
                    degree_of_player = self.select_list[self.player_count]
                    if degree_of_player in range(0,60):
                        self.player_list.append('player1')
                    elif degree_of_player in range(60,120):
                        self.player_list.append('player2')
                    elif degree_of_player in range(120,180):
                        self.player_list.append('player3')
                    elif degree_of_player in range(180,240):
                        self.player_list.append('player4')
                    elif degree_of_player in range(240,300):
                        self.player_list.append('player5')
                    elif degree_of_player in range(300,360):
                        self.player_list.append('player6')
                
                if self.player_count > 0: #user clicked the 'add' button (but it's not the first time)
                    self.rotate_degree = random.randint(0,360)
                    self.select_list.append(self.select_list[self.player_count-1] + self.rotate_degree)
                    degree_of_player = self.select_list[self.player_count] % 360
                    if degree_of_player in range(0,60):
                        self.player_list.append('player1')
                    elif degree_of_player in range(60,120):
                        self.player_list.append('player2')
                    elif degree_of_player in range(120,180):
                        self.player_list.append('player3')
                    elif degree_of_player in range(180,240):
                        self.player_list.append('player4')
                    elif degree_of_player in range(240,300):
                        self.player_list.append('player5')
                    elif degree_of_player in range(300,360):
                        self.player_list.append('player6')
                    
                    #if the player has already been selected, it will pick a new random player 
                    # (until pick the player who has not been selected)
                    while self.player_list[self.player_count] in self.player_list[:self.player_count]:
                        self.rotate_degree = random.randint(0,360)
                        self.select_list[self.player_count] = self.select_list[self.player_count-1] + self.rotate_degree
                        degree_of_player = self.select_list[self.player_count] % 360
                        if degree_of_player in range(0,60):
                            self.player_list[self.player_count] = 'player1'
                        elif degree_of_player in range(60,120):
                            self.player_list[self.player_count] = 'player2'
                        elif degree_of_player in range(120,180):
                            self.player_list[self.player_count] = 'player3'
                        elif degree_of_player in range(180,240):
                            self.player_list[self.player_count] = 'player4'
                        elif degree_of_player in range(240,300):
                            self.player_list[self.player_count] = 'player5'
                        elif degree_of_player in range(300,360):
                            self.player_list[self.player_count] = 'player6'
                 
                self.rotate_degree = self.select_list[self.player_count]
                self.player_count += 1
        else:
            self.add_button_disable.draw(surface)

        self.turntable.draw(surface,self.rotate_degree)
        self.arrow.draw(surface) 

        if self.turntable.rotate_finish: #animation finish, start to print the photo of the player
            if self.player_count == 1:
                if self.player_list[self.player_count-1] == 'player1':
                    self.player1_photo.image_original = pygame.image.load('./images/profilePhoto_player1.png').convert_alpha()
                    self.player1_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player1_disable.png').convert_alpha()
                    self.player1_photo.image_original_active = pygame.image.load('./images/profilePhoto_player1_active.png').convert_alpha()
                    self.player1_photo.image = pygame.transform.scale(self.player1_photo.image_original,(self.player1_photo.width,self.player1_photo.height))
                elif self.player_list[self.player_count-1] == 'player2':
                    self.player1_photo.image_original = pygame.image.load('./images/profilePhoto_player2.png').convert_alpha()
                    self.player1_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player2_disable.png').convert_alpha()
                    self.player1_photo.image_original_active = pygame.image.load('./images/profilePhoto_player2_active.png').convert_alpha()
                    self.player1_photo.image = pygame.transform.scale(self.player1_photo.image_original,(self.player1_photo.width,self.player1_photo.height))
                elif self.player_list[self.player_count-1] == 'player3':
                    self.player1_photo.image_original = pygame.image.load('./images/profilePhoto_player3.png').convert_alpha()
                    self.player1_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player3_disable.png').convert_alpha()
                    self.player1_photo.image_original_active = pygame.image.load('./images/profilePhoto_player3_active.png').convert_alpha()
                    self.player1_photo.image = pygame.transform.scale(self.player1_photo.image_original,(self.player1_photo.width,self.player1_photo.height))
                elif self.player_list[self.player_count-1] == 'player4':
                    self.player1_photo.image_original = pygame.image.load('./images/profilePhoto_player4.png').convert_alpha()
                    self.player1_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player4_disable.png').convert_alpha()
                    self.player1_photo.image_original_active = pygame.image.load('./images/profilePhoto_player4_active.png').convert_alpha()
                    self.player1_photo.image = pygame.transform.scale(self.player1_photo.image_original,(self.player1_photo.width,self.player1_photo.height))
                elif self.player_list[self.player_count-1] == 'player5':
                    self.player1_photo.image_original = pygame.image.load('./images/profilePhoto_player5.png').convert_alpha()
                    self.player1_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player5_disable.png').convert_alpha()
                    self.player1_photo.image_original_active = pygame.image.load('./images/profilePhoto_player5_active.png').convert_alpha()
                    self.player1_photo.image = pygame.transform.scale(self.player1_photo.image_original,(self.player1_photo.width,self.player1_photo.height))
                elif self.player_list[self.player_count-1] == 'player6':
                    self.player1_photo.image_original = pygame.image.load('./images/profilePhoto_player6.png').convert_alpha()
                    self.player1_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player6_disable.png').convert_alpha()
                    self.player1_photo.image_original_active = pygame.image.load('./images/profilePhoto_player6_active.png').convert_alpha()
                    self.player1_photo.image = pygame.transform.scale(self.player1_photo.image_original,(self.player1_photo.width,self.player1_photo.height))

            if self.player_count == 2:
                if self.player_list[self.player_count-1] == 'player1':
                    self.player2_photo.image_original = pygame.image.load('./images/profilePhoto_player1.png').convert_alpha()
                    self.player2_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player1_disable.png').convert_alpha()
                    self.player2_photo.image_original_active = pygame.image.load('./images/profilePhoto_player1_active.png').convert_alpha()
                    self.player2_photo.image = pygame.transform.scale(self.player2_photo.image_original,(self.player2_photo.width,self.player2_photo.height))
                elif self.player_list[self.player_count-1] == 'player2':
                    self.player2_photo.image_original = pygame.image.load('./images/profilePhoto_player2.png').convert_alpha()
                    self.player2_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player2_disable.png').convert_alpha()
                    self.player2_photo.image_original_active = pygame.image.load('./images/profilePhoto_player2_active.png').convert_alpha()
                    self.player2_photo.image = pygame.transform.scale(self.player2_photo.image_original,(self.player2_photo.width,self.player2_photo.height))
                elif self.player_list[self.player_count-1] == 'player3':
                    self.player2_photo.image_original = pygame.image.load('./images/profilePhoto_player3.png').convert_alpha()
                    self.player2_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player3_disable.png').convert_alpha()
                    self.player2_photo.image_original_active = pygame.image.load('./images/profilePhoto_player3_active.png').convert_alpha()
                    self.player2_photo.image = pygame.transform.scale(self.player2_photo.image_original,(self.player2_photo.width,self.player2_photo.height))
                elif self.player_list[self.player_count-1] == 'player4':
                    self.player2_photo.image_original = pygame.image.load('./images/profilePhoto_player4.png').convert_alpha()
                    self.player2_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player4_disable.png').convert_alpha()
                    self.player2_photo.image_original_active = pygame.image.load('./images/profilePhoto_player4_active.png').convert_alpha()
                    self.player2_photo.image = pygame.transform.scale(self.player2_photo.image_original,(self.player2_photo.width,self.player2_photo.height))
                elif self.player_list[self.player_count-1] == 'player5':
                    self.player2_photo.image_original = pygame.image.load('./images/profilePhoto_player5.png').convert_alpha()
                    self.player2_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player5_disable.png').convert_alpha()
                    self.player2_photo.image_original_active = pygame.image.load('./images/profilePhoto_player5_active.png').convert_alpha()
                    self.player2_photo.image = pygame.transform.scale(self.player2_photo.image_original,(self.player2_photo.width,self.player2_photo.height))
                elif self.player_list[self.player_count-1] == 'player6':
                    self.player2_photo.image_original = pygame.image.load('./images/profilePhoto_player6.png').convert_alpha()
                    self.player2_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player6_disable.png').convert_alpha()
                    self.player2_photo.image_original_active = pygame.image.load('./images/profilePhoto_player6_active.png').convert_alpha()
                    self.player2_photo.image = pygame.transform.scale(self.player2_photo.image_original,(self.player2_photo.width,self.player2_photo.height))

            if self.player_count == 3:
                if self.player_list[self.player_count-1] == 'player1':
                    self.player3_photo.image_original = pygame.image.load('./images/profilePhoto_player1.png').convert_alpha()
                    self.player3_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player1_disable.png').convert_alpha()
                    self.player3_photo.image_original_active = pygame.image.load('./images/profilePhoto_player1_active.png').convert_alpha()
                    self.player3_photo.image = pygame.transform.scale(self.player3_photo.image_original,(self.player3_photo.width,self.player3_photo.height))
                elif self.player_list[self.player_count-1] == 'player2':
                    self.player3_photo.image_original = pygame.image.load('./images/profilePhoto_player2.png').convert_alpha()
                    self.player3_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player2_disable.png').convert_alpha()
                    self.player3_photo.image_original_active = pygame.image.load('./images/profilePhoto_player2_active.png').convert_alpha()
                    self.player3_photo.image = pygame.transform.scale(self.player3_photo.image_original,(self.player3_photo.width,self.player3_photo.height))
                elif self.player_list[self.player_count-1] == 'player3':
                    self.player3_photo.image_original = pygame.image.load('./images/profilePhoto_player3.png').convert_alpha()
                    self.player3_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player3_disable.png').convert_alpha()
                    self.player3_photo.image_original_active = pygame.image.load('./images/profilePhoto_player3_active.png').convert_alpha()
                    self.player3_photo.image = pygame.transform.scale(self.player3_photo.image_original,(self.player3_photo.width,self.player3_photo.height))
                elif self.player_list[self.player_count-1] == 'player4':
                    self.player3_photo.image_original = pygame.image.load('./images/profilePhoto_player4.png').convert_alpha()
                    self.player3_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player4_disable.png').convert_alpha()
                    self.player3_photo.image_original_active = pygame.image.load('./images/profilePhoto_player4_active.png').convert_alpha()
                    self.player3_photo.image = pygame.transform.scale(self.player3_photo.image_original,(self.player3_photo.width,self.player3_photo.height))
                elif self.player_list[self.player_count-1] == 'player5':
                    self.player3_photo.image_original = pygame.image.load('./images/profilePhoto_player5.png').convert_alpha()
                    self.player3_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player5_disable.png').convert_alpha()
                    self.player3_photo.image_original_active = pygame.image.load('./images/profilePhoto_player5_active.png').convert_alpha()
                    self.player3_photo.image = pygame.transform.scale(self.player3_photo.image_original,(self.player3_photo.width,self.player3_photo.height))
                elif self.player_list[self.player_count-1] == 'player6':
                    self.player3_photo.image_original = pygame.image.load('./images/profilePhoto_player6.png').convert_alpha()
                    self.player3_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player6_disable.png').convert_alpha()
                    self.player3_photo.image_original_active = pygame.image.load('./images/profilePhoto_player6_active.png').convert_alpha()
                    self.player3_photo.image = pygame.transform.scale(self.player3_photo.image_original,(self.player3_photo.width,self.player3_photo.height))

            if self.player_count == 4:
                if self.player_list[self.player_count-1] == 'player1':
                    self.player4_photo.image_original = pygame.image.load('./images/profilePhoto_player1.png').convert_alpha()
                    self.player4_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player1_disable.png').convert_alpha()
                    self.player4_photo.image_original_active = pygame.image.load('./images/profilePhoto_player1_active.png').convert_alpha()
                    self.player4_photo.image = pygame.transform.scale(self.player4_photo.image_original,(self.player4_photo.width,self.player4_photo.height))
                elif self.player_list[self.player_count-1] == 'player2':
                    self.player4_photo.image_original = pygame.image.load('./images/profilePhoto_player2.png').convert_alpha()
                    self.player4_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player2_disable.png').convert_alpha()
                    self.player4_photo.image_original_active = pygame.image.load('./images/profilePhoto_player2_active.png').convert_alpha()
                    self.player4_photo.image = pygame.transform.scale(self.player4_photo.image_original,(self.player4_photo.width,self.player4_photo.height))
                elif self.player_list[self.player_count-1] == 'player3':
                    self.player4_photo.image_original = pygame.image.load('./images/profilePhoto_player3.png').convert_alpha()
                    self.player4_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player3_disable.png').convert_alpha()
                    self.player4_photo.image_original_active = pygame.image.load('./images/profilePhoto_player3_active.png').convert_alpha()
                    self.player4_photo.image = pygame.transform.scale(self.player4_photo.image_original,(self.player4_photo.width,self.player4_photo.height))
                elif self.player_list[self.player_count-1] == 'player4':
                    self.player4_photo.image_original = pygame.image.load('./images/profilePhoto_player4.png').convert_alpha()
                    self.player4_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player4_disable.png').convert_alpha()
                    self.player4_photo.image_original_active = pygame.image.load('./images/profilePhoto_player4_active.png').convert_alpha()
                    self.player4_photo.image = pygame.transform.scale(self.player4_photo.image_original,(self.player4_photo.width,self.player4_photo.height))
                elif self.player_list[self.player_count-1] == 'player5':
                    self.player4_photo.image_original = pygame.image.load('./images/profilePhoto_player5.png').convert_alpha()
                    self.player4_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player5_disable.png').convert_alpha()
                    self.player4_photo.image_original_active = pygame.image.load('./images/profilePhoto_player5_active.png').convert_alpha()
                    self.player4_photo.image = pygame.transform.scale(self.player4_photo.image_original,(self.player4_photo.width,self.player4_photo.height))
                elif self.player_list[self.player_count-1] == 'player6':
                    self.player4_photo.image_original = pygame.image.load('./images/profilePhoto_player6.png').convert_alpha()
                    self.player4_photo.image_original_disable = pygame.image.load('./images/profilePhoto_player6_disable.png').convert_alpha()
                    self.player4_photo.image_original_active = pygame.image.load('./images/profilePhoto_player6_active.png').convert_alpha()
                    self.player4_photo.image = pygame.transform.scale(self.player4_photo.image_original,(self.player4_photo.width,self.player4_photo.height))
        else:
            self.add_button_disable.draw(surface)

        #the 'start' button
        if self.player_count==4:
            self.submit_button.draw(surface)
            if self.submit_button.get_result():
                #pass the player photos to next screen
                globals.player_photo_list.append(self.player1_photo) 
                globals.player_photo_list.append(self.player2_photo)
                globals.player_photo_list.append(self.player3_photo)
                globals.player_photo_list.append(self.player4_photo)
                globals.player_list = self.player_list
                globals.current_screen = GameMainPlayScreen()
        else:
            self.submit_button_disable.draw(surface)

            

        
        
            
        



        
        
        

