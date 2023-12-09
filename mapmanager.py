# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = 'sources/block.egg'
        self.texture = 'sources/block.png'
        self.color = (0.1,0.6,0.1,1)
        self.color2 = (0.6,0.6,0.6,1)
        self.color3 = (0.35,0.35,0.35,1)
        self.color4 = (0.9,0.9,0.9,1)
        self.startNew()
        for x in range(32):
            for y in range(32):
                for z in range(5):
                    self.addBlock((x,y,z), self.color, 1)
        for x in range(32):
            for y in range(6,28):
                self.addBlock((x,y,4.05), self.color2, 1)
        for x in range(32):
            for y in range(13,19):
                self.addBlock((x,y,4.1), self.color3, 1)
        self.addBlock((25,25,15),self.color4, (2,2,25))
        self.addBlock((22,25,15),self.color4,(2,2,25))
        self.addBlock((18,25,5),(0.5,0.5,0.5,1),(5,4,3))
        self.addBlock((18,25,7),(0.5,0.5,0.5,1),(2,2,1.5))
        self.addBlock((13,25,13),(0.1,0.6,0.8,1),(3,3,17))
        self.addBlock((11,25,13),(0.1,0.6,0.8,1),(2,2,17))
        self.addBlock((7,25,12), self.color4, (3,3,16))
        self.addBlock((5,25,11),(0.1,0.6,0.8,1),(2,2,14))
        
        # self.addPlayer()
    def startNew(self):
        self.land = render.attachNewNode('Land')
    def addBlock(self, position, color, scale): 
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(color)
        self.block.setScale(scale)
        self.block.reparentTo(self.land)
    # def addPlayer(self):
    #     self.player = loader.loadModel('sources/steve.fbx')
    #     self.player.setTexture(loader.loadTexture('sources/steve.png'))
    #     self.player.setPos(8,8,5.3)
    #     self.player.setScale(0.05,0.05,0.05)
    #     self.player.setHpr(0,90,0)
    #     self.player.reparentTo(self.land)
