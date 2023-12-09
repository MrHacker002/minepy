from direct.actor.Actor import Actor
from panda3d.core import WindowProperties
class Player:
    def __init__(self, pos, map):
        self.player = Actor('sources/steve.fbx')
        self.player.setTexture(loader.loadTexture('sources/steve.png'))
        self.player.setPos(8,8,5.3)
        self.player.setScale(0.05,0.05,0.05)
        self.player.setHpr(0,90,0)
        self.player.reparentTo(render)
        self.map = map
        self.lastMouseX, self.lastMouseY = None, None
        self.manualRecenterMouse = True
        self.rotateX, self.rotateY = 0,0
        self.mouseMagnitude = 10
        self.event()
        self.hideCursor(True)
        taskMgr.add(self.mouseTask, 'mouseTask')
    def forv(self):
        x,y,z = self.player.getPos()
        angle = self.player.getH()
        dx,dy = self.check_angle(angle%360)
        self.player.setPos(x+dx,y+dy,z)
    def right(self):
        x,y,z = self.player.getPos()
        angle = self.player.getH()
        dx,dy = self.check_angle(angle+270 % 360)
        self.player.setPos(x+dx,y+dy,z)
    def check_angle(self, angle):
        if 0 <= angle < 20 or 335 <= angle < 360:
            return 0, -1
        elif 20 <= angle < 65:
            return 1, -1
        elif 65 <= angle < 110:
            return 1, 0
        elif 110 <= angle < 155:
            return 1, 1
        elif 155 <= angle < 200:
            return 0, 1
        elif 200 <= angle < 245:
            return -1, 1
        elif 245 <= angle < 290:
            return -1, 0
        elif 290 <= angle < 335:
            return -1, -1

    def fpv(self):
        base.disableMouse()
        base.camera.reparentTo(self.player)
        base.camera.setH(180)
        base.camera.setP(90)
        base.camera.setPos((0,0,1))
    def event(self):
        base.accept('1',self.fpv)
        base.accept('2',self.spec)
        base.accept('w', self.forv)
        base.accept('w'+'-repeat', self.forv)
        base.accept('d', self.right)
        base.accept('d'+'-repeat', self.right)
    def spec(self):
        base.enableMouse()
        base.camera.reparentTo(render)
    def mouseTask(self, task):
        mw = base.mouseWatcherNode

        hasMouse = mw.hasMouse()
        if hasMouse:
            x, y = mw.getMouseX(), mw.getMouseY()

            if self.lastMouseX is not None:
                if self.manualRecenterMouse:
                    dx, dy = x, y
                else:
                    dx, dy = x - self.lastMouseX, y - self.lastMouseY
            else:
                dx, dy = 0, 0

            self.lastMouseX, self.lastMouseY = x, y

        else:
            x, y, dx, dy = 0, 0, 0, 0

        if self.manualRecenterMouse:
            self.recenterMouse()
            self.lastMouseX, self.lastMouseY = 0, 0

        self.rotateX += dx * 10 * self.mouseMagnitude
        self.rotateY += dy * 10 * self.mouseMagnitude

        self.player.setH(-self.rotateX)
        self.player.setP(-self.rotateY)

        return task.cont
    def recenterMouse(self):
        base.win.movePointer(
            0,
            int(base.win.getProperties().getXSize() / 2),
            int(base.win.getProperties().getYSize() / 2)
        )
    def hideCursor(self, mouseFlag):
        """Hide the mouse"""
        wp = WindowProperties()
        wp.setCursorHidden(mouseFlag)
        base.win.requestProperties(wp)
