from ScreenBaseModule import ScreenBase
from BackgroundModule import Background
from ButtonModule import Button
from GameMatchingScreenModule import GameMatchingScreen
import globals

#[1]Game Start Screen: Jiayao Song

#My Idea: 
# 1、have a start button
# 2、have a exit button
# 3、click the start button and jump to the next screen
# 4、images made by: Jiayao Song(background), Yuchen Zhou

class GameStartMenuScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        x_of_buttons = globals.screen_current_width * (1-0.54) * 0.5
        y_of_buttons = globals.screen_current_height * (1-0.18)
        gap_of_buttons = globals.screen_current_width * 0.34
        self.background = Background('./images/background_GameStart.png')
        self.start_button = Button(x_of_buttons,y_of_buttons,'./images/start_button.png',0.5,"")
        self.exit_button = Button(x_of_buttons + gap_of_buttons,y_of_buttons,'./images/exit_button.png',0.5,"")
        
        self.objects.append(self.background)
        self.objects.append(self.start_button)
        self.objects.append(self.exit_button)

    def draw(self,surface):
        super().draw(surface)
        if self.start_button.get_result():
            globals.current_screen = GameMatchingScreen()
        if self.exit_button.get_result():
            globals.running = False

        
        

