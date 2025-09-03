import pyxel

width, heigth = 160, 120

keys_to_representation = {
    pyxel.KEY_SPACE: "space",
    pyxel.KEY_A: "a",
    pyxel.KEY_D: "d",
    pyxel.KEY_E: "e",
    pyxel.KEY_Q: "q",
    pyxel.KEY_S: "s",
    pyxel.KEY_W: "w",
    pyxel.KEY_BACKSPACE: "backspace",
    pyxel.KEY_ESCAPE: "escape",
    pyxel.KEY_UP: "up",
    pyxel.KEY_DOWN: "down",
    pyxel.KEY_LEFT: "left",
    pyxel.KEY_RIGHT: "right"
}

class player:

    global width
    global heigth

    def __init__(self):
        self.pX = width / 2
        self.pY = heigth / 2
    
    #def draw_player(self):
        

    def move_player(self):
        if pyxel.btn(pyxel.KEY_W):
            self.pY -= 5
        elif pyxel.btn(pyxel.KEY_S):
            self.pY += 5
        elif pyxel.btn(pyxel.KEY_A):
            self.pX -= 5
        elif pyxel.btn(pyxel.KEY_D):
            self.pX += 5



class App:

    global width
    global heigth 
    

    def __init__(self):
        pyxel.init(width, heigth, title="Hello Pyxel")
        pyxel.load("assets/RESOURCE_FILE.pyxres")
        pyxel.run(self.update, self.draw)

        self.player = player()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):

        pyxel.cls(0)

        pyxel.blt(player().pX, player().pY, 0, 0, 0, 16, 16)

        player().move_player()

        
        

App()