from classes import *

current_screen = None
running = None

#set screen size to 10:6 ratio
screen_current_width = 1000
screen_current_height = 600

player_photo_list = []
player_list = []

# Creating Objects
img = Image() 
pm = PlayMode() 
fnt = TextFont() 
ess = Essentials()

# Setting up initial game variables
active = None  # While game is ON this variable is True
ess.play_mode = pm.in_game  # Initial screen

disp = False
win_dec = False  # True if Winner is declared
pen_check = False  # Penalty check flag
flag = False