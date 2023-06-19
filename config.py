import pygame

# Creating the grid class
class Grid(object):
    def __init__(self):
        self.yf = 90
        self.noOfRows = 11
        self.sHeight = self.yf * self.noOfRows
        self.sWidth = 1000

    # Creating the font method
    def font(self):
        self.fonty = "comicsans"

    # Creating a color method
    def color1(self):
        self.colorone = (0, 0, 0)

    # Creating another color method
    def color2(self):
        self.colortwo = (255, 255, 255)

    # Creating another color method
    def color3(self):
        self.colorthree = (64, 224, 208)

    # Creating another color method
    def color4(self):
        self.colorfour = (0, 200, 255)

    # Creating another color method
    def color5(self):
        self.colorfive = (1, 10, 67)

    # Creating another color method
    def color6(self):
        self.colorsix = (255, 255, 0)

    # Creating another color method
    def color7(self):
        self.colorseven = (69, 5, 5)

    # Creating another color method
    def color8(self):
        self.coloreight = (255, 194, 194)

    # Creating another color method
    def color9(self):
        self.colornine = (255, 46, 99)

    # Creating methods for my messages
    def p1string(self):
        self.p1 = "Player 1: "

    def p2string(self):
        self.p2 = "Player 2: "

    def levstring(self):
        self.level = "Level: "

    def fstring(self):
        self.f = "Press F to activate slow"

    def motstring(self):
        self.motion = " motion(only works twice per player): "

    def p1won(self):
        self.won1 = "Player 1 won! "

    def p2won(self):
        self.won2 = "Player 2 won! "
