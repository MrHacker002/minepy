# напиши тут код основного вікна гри
from mapmanager import Mapmanager
from player import Player
from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.player = Player((8, 8, 5.3), self.land)
        base.camLens.setFov(90)

game = Game()
game.run()