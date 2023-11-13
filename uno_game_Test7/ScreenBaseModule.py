#ScreenBase: Jiayao Song
#screen base form

class ScreenBase:
    def __init__(self):
        self.objects = []
 
    def draw(self, surface):
        for obj in self.objects:
            obj.draw(surface)

