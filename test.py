# Importing pygame
import pygame
import time
# Importing the grid class from the config file
from config import Grid
pygame.init()
# Creating an instance of the grid class
g = Grid()
win = pygame.display.set_mode((g.sWidth, g.sHeight))
slowdown = 0
level = 0

g.color2()


# Class for moving obstacles
class Obstacle(object):
    def __init__(self, velocity, x, y, width, height):
        self.velocity = velocity
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # A draw method for the moving obstacles
    def draw(self):
        pygame.draw.rect(win, g.colortwo,
                         (self.x, self.y, self.width, self.height))

    # Determining the velocities of the moving obstacles
    def mov(self):
        global slowdown
        if slowdown == 1:
            upd_vel = self.velocity//2
        else:
            upd_vel = self.velocity
        if self.x < g.sWidth - upd_vel:
            self.x += upd_vel
        else:
            self.x = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

g.color4()
g.color5()


# Class for fixed obstacles
class fixedObstacle(object):
    def __init__(self, velocity, x, y, width, height):
        self.velocity = velocity
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # A draw method for the fixed obstacles
    def draw(self):
        pygame.draw.rect(win, g.colorfour,
                         (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, g.colorfive,
                         (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
# Caption of the game
pygame.display.set_caption("River Crossing")
# List for moving obstacles
obs = []
# List for fixed obstacles
moving_obs = []
obs.append(Obstacle(3, 200, 90, 100, g.yf))
obs.append(Obstacle(3, 500, 90, 100, g.yf))
obs.append(Obstacle(3, 0, 450, 100, g.yf))
obs.append(Obstacle(3, 300, 450, 100, g.yf))
obs.append(Obstacle(3, 300, 270, 100, g.yf))
obs.append(Obstacle(3, 400, 630, 100, g.yf))
obs.append(Obstacle(3, 600, 810, 100, g.yf))
obs.append(Obstacle(3, 350, 810, 100, g.yf))
moving_obs.append(fixedObstacle(3, 80, 180, 100, g.yf))
moving_obs.append(fixedObstacle(3, 400, 180, 100, g.yf))
moving_obs.append(fixedObstacle(3, 900, 180, 100, g.yf))
moving_obs.append(fixedObstacle(3, 140, 360, 100, g.yf))
moving_obs.append(fixedObstacle(3, 400, 360, 100, g.yf))
moving_obs.append(fixedObstacle(3, 700, 360, 100, g.yf))
moving_obs.append(fixedObstacle(3, 530, 540, 100, g.yf))
moving_obs.append(fixedObstacle(3, 800, 540, 100, g.yf))
moving_obs.append(fixedObstacle(3, 300, 540, 100, g.yf))
moving_obs.append(fixedObstacle(3, 600, 720, 100, g.yf))
moving_obs.append(fixedObstacle(3, 150, 720, 100, g.yf))
moving_obs.append(fixedObstacle(3, 850, 720, 100, g.yf))


# Class for creating the player
class player(object):

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 25
        self.color = color
        self.score = 0
        self.time = 0
        self.slow_power_up = 2

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    # Draw method for the player
    def draw(self):
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))

    # Update score method
    def upd_score(self, delta):
        self.score += delta

    # Method which calls the powerup that slows down the game
    def call_powerup(self):
        global slowdown
        if self.slow_power_up > 0:
            self.slow_power_up -= 1
            slowdown = 1
g.color6()
g.color7()
# Creating the first player
box1 = player(400, 0, 100, g.yf, g.colorsix)
# Creating the second player
box2 = player(500, 900, 100, g.yf, g.colorseven)

box = []
box.append(box1)
box.append(box2)

turn = 0

run = True
hit = False
# Gives the current time in seconds to keep track
box[turn].time = time.time()
temper = 0
g.color8()
g.color9()
while run:
    pygame.time.delay(10)
    temper += 1
    if temper > 200:
        temper = 0
    # Creating the grid of the game
    for i in range(0, g.noOfRows + 1):
        if i % 2 == 0:
            pygame.draw.rect(win, g.coloreight,
                             (0, i * g.yf, g.sWidth, g.yf))
        else:
            pygame.draw.rect(win, g.colornine, (0, i * g.yf, g.sWidth, g.yf))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Assigning the movement keys to WASD
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a') and box[turn].x > box[turn].vel:
                box[turn].x -= box[turn].width
            if (event.key == ord('d') and
               box[turn].x < g.sWidth - box[turn].width):
                box[turn].x += box[turn].width
            if event.key == ord('w') and box[turn].y > box[turn].vel:
                box[turn].y -= g.yf
                if turn == 1:
                    box[1].upd_score(5)
                else:
                    box[0].upd_score(-5)
            if (event.key == ord('s') and
               box[turn].y < g.sWidth - box[turn].height - box[turn].vel):
                box[turn].y += g.yf
                if turn == 1:
                    box[1].upd_score(-5)
                else:
                    box[0].upd_score(5)
            # The 'f' key initiates the powerup
            if event.key == ord('f'):
                box[turn].call_powerup()
    # Various calls to the methods in the config file
    g.font()
    g.color1()
    g.color2()
    g.color3()
    g.p1string()
    g.p2string()
    g.levstring()
    g.fstring()
    g.motstring()
    g.p1won()
    g.p2won()
    # Setting the font of the text
    font = pygame.font.SysFont(g.fonty, 30, True)
    # Setting the text to be displayed
    nice = font.render(g.p1 + str(box[0].score), 1, g.colorone)
    # Allocating the text to a certain position on the window
    win.blit(nice, (0, 0))
    text = font.render(g.p2 + str(box[1].score), 1, g.colorone)
    win.blit(text, (0, 900))
    gg = font.render(g.level + str(level), 1, g.colorone)
    win.blit(gg, (900, 0))
    ok = font.render(g.f +
                     g.motion, 1, g.colorone)
    win.blit(ok, (250, 900))
    # This marks the last level of the game
    if level == 8:
        win.fill(g.colorthree)
        font = pygame.font.SysFont(g.fonty, 50, True)
        # Comparing the scores of the two players
        if box[0].score > box[1].score:
            same = font.render(g.won1, 1, g.colortwo)
            win.blit(same, (400, 400))
        if box[1].score > box[0].score:
            adopted = font.render(g.won2, 1, g.colortwo)
            win.blit(adopted, (400, 400))
        pygame.display.update()
        time.sleep(5)
        break

    box[turn].draw()
    # The score varies according to time
    temp_time = time.time()
    if temp_time - box[turn].time >= 1:
        box[turn].time = temp_time
        box[turn].upd_score(-1)
    for obj in obs:
        obj.draw()
        obj.mov()
    for obj in moving_obs:
        obj.draw()
    pygame.display.update()
    # Checking for collisions and assigning hit to true if there is a collision
    for obj in obs:
        if obj.get_rect().colliderect(box[turn].get_rect()):
            hit = True

    for obj in moving_obs:
        if obj.get_rect().colliderect(box[turn].get_rect()):
            hit = True

    # When the first player reaches the bottom
    if box[0].y == 900 and turn == 0:
        slowdown = 0
        box[0].upd_score(20)
        turn = 1
        box[turn].time = time.time()
        box[1].x = 500
        box[1].y = 900

    # When the second player reaches the top
    if box[1].y == 0 and turn == 1:
        slowdown = 0
        box[1].upd_score(20)
        turn = 0
        box[turn].time = time.time()
        box[0].x = 400
        box[0].y = 0
        # Increases the velocity after each level
        for obj in obs:
            obj.velocity += 1
        level += 1
    # After a collision, the next player gets a chance to play
    if hit:
        slowdown = 0
        if turn == 1:
            box[1].upd_score(-10)
            box[0].x = 400
            box[0].y = 0
            turn = 0
            for obj in obs:
                obj.velocity += 1
            level += 1
            box[turn].time = time.time()
        elif turn == 0:
            box[0].upd_score(-10)
            turn = 1
            box[turn].time = time.time()
            box[1].x = 500
            box[1].y = 900
    hit = False
pygame.quit()
