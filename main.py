import pygame as pg
import random as rd
from moviepy.editor import VideoFileClip as vc

pg.init()
# Variables
x = 1920
y = 1080
isFullScreen = 0
screen = pg.display.set_mode((x,y), isFullScreen)
clock = pg.time.Clock()
pg.display.set_caption("My Game")

video_file = {}
video_file["MenuVideo1"] = vc("MenuVideo1.mp4").resize((x,y))
video_file["MenuVideo2"] = vc("MenuVideo2.mp4").resize((x,y))
running_video = None
running = True
isMenu = True


tile_size = 64 # Rozmiar kafelka

tiles = {} # Słownik przechowujący zdjęcia kafelków
tiles[0] = pg.image.load("Grass1.png") # Kafelek trawy
tiles[1] = pg.image.load("Dirt.png") # Kafelek ziemi
tiles[2] = pg.image.load("Stone.png") # Kafelek kamienia
tiles[3] = pg.image.load("IronOre.png") # Kafelek rudy żelaza
tutorial_map = [ # Mapa początkowa
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,3,2,2,3,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,2,2,3,2,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,2,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,3,2,2,3,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,2,2,3,2,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,2,2,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

objects = {} # Słownik przechowujący zdjęcia obiektów
objects[0] = pg.image.load("none.png") # Obiekt pusty
objects[1] = pg.image.load("Grass.png") # Obiekt trawy
tutorial_objects_map = [ # Mapa rozmieszczenia obiektów
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

class drawObject():
    def __init__(self, screen, color, posX, posY, width, height,font, size, text, textColor, image):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.font = font
        self.size = size
        self.text = text
        self.textColor = textColor
        self.image = image
    def clear(self):
        pg.draw.rect(self.screen, (0,0,0),(self.posX,self.posY,self.width,self.height))
    def drawButton(self):
        pg.draw.rect(self.screen,self.color, (self.posX,self.posY,self.width,self.height))
        button_font = pg.font.Font(self.font, self.size)
        button_text = button_font.render(self.text,True,self.textColor)
        text_rect = button_text.get_rect(center = (self.posX + self.width//2, self.posY+self.height//2))
        screen.blit(button_text, text_rect)
    def drawText(self):
        self.clear()
        font = pg.font.Font(self.font,self.size)
        text = font.render(self.text,True,self.textColor)
        text_rect = text.get_rect(center = (self.posX + self.width//2, self.posY+self.height//2))
        screen.blit(text, text_rect)
    def drawImage(self):
        image = pg.image.load(self.image)
        screen.blit(image, (self.posX,self.posY))

# Play Button

playButton_color = (5, 4, 33)
playButton_posX = (x-250)//2
playButton_posY = (y-150)//2
playButton_width = 250
playButton_height = 100
playButton_textsize = 64
playButton_textcolor = "white"
playButton = drawObject(screen, playButton_color, playButton_posX, playButton_posY, playButton_width, playButton_height, None, playButton_textsize, "Play", playButton_textcolor, None)

# Setting Button

settingsButton_color = (5, 4, 33)
settingsButton_posX = (x-250)//2
settingsButton_posY = (y+100)//2
settingsButton_width = 250
settingsButton_height = 100
settingsButton_textsize = 64
settingsButton_textcolor = "white"
settingsButton = drawObject(screen, settingsButton_color, settingsButton_posX , settingsButton_posY, settingsButton_width, settingsButton_height, None, settingsButton_textsize, "Settings", settingsButton_textcolor, None)

# Quit Button

quitButton_color = (5, 4, 33)
quitButton_posX = (x-250)//2
quitButton_posY = (y+350)//2
quitButton_width = 250
quitButton_height = 100
quitButton_textsize = 64
quitButton_textcolor = "white"
quitButton = drawObject(screen,quitButton_color,quitButton_posX,quitButton_posY,quitButton_width,quitButton_height, None, quitButton_textsize, "Quit", quitButton_textcolor, None)

# Volume Text
volLev = 100
volumeText = drawObject(screen, None, 0, 0, 300, 100, None, 60, f"Volume {volLev}", "white", None)

# Volume Button Add
volumeButtonA_color = (64, 64, 64)
volumeButtonA_posX = x - 300
volumeButtonA_posY = 0
volumeButtonA_width = 100
volumeButtonA_height = 100
volumeButtonA_textsize = 100
volumeButtonA_textcolor = "white"
volumeButtonA = drawObject(screen,volumeButtonA_color,volumeButtonA_posX,volumeButtonA_posY,volumeButtonA_width,volumeButtonA_height, None, volumeButtonA_textsize, "+", volumeButtonA_textcolor, None)

# Volume Button Subtract
volumeButtonS_color = (64, 64, 64)
volumeButtonS_posX = x - 150
volumeButtonS_posY = 0
volumeButtonS_width = 100
volumeButtonS_height = 100
volumeButtonS_textsize = 100
volumeButtonS_textcolor = "white"
volumeButtonS = drawObject(screen,volumeButtonS_color,volumeButtonS_posX,volumeButtonS_posY,volumeButtonS_width,volumeButtonS_height, None, volumeButtonS_textsize, "-", volumeButtonS_textcolor, None)

# Resolution Text
resolutionText = drawObject(screen, None, 0, 150, 600, 100, None, 60, f"Width = {x}, height = {y}", "white", None)

# Resolution Button Add
resButtonA_color = (64, 64, 64)
resButtonA_posX = x - 300
resButtonA_posY = 150
resButtonA_width = 100
resButtonA_height = 100
resButtonA_textsize = 100
resButtonA_textcolor = "white"
resButtonA = drawObject(screen,resButtonA_color,resButtonA_posX,resButtonA_posY,resButtonA_width,resButtonA_height, None, resButtonA_textsize, "+", resButtonA_textcolor, None)

# Resolution Button Mode
resButtonMode_color = (64, 64, 64)
resButtonMode_posX = x - 150
resButtonMode_posY = 150
resButtonMode_width = 100
resButtonMode_height = 100
resButtonMode_textsize = 100
resButtonMode_textcolor = "white"
resButtonMode = drawObject(screen,resButtonMode_color,resButtonMode_posX,resButtonMode_posY,resButtonMode_width,resButtonMode_height, None, resButtonMode_textsize, "W", resButtonMode_textcolor, None)

# Setting Images
back_arrow_posX = x - 150
back_arrow_posY = 620
back_arrow = drawObject(screen,None,back_arrow_posX,back_arrow_posY,100,100, None, None, None, None, "Arrow_Left.png")

# Functions
def game():
    global running
    global playButton

    videoInit()
    while running:
        eventListener()
        mainMenu()
        pg.display.flip()
        clock.tick(30)
    pg.quit()

def mainMenu():
    global isMenu
    if isMenu == True:
            videoShow()
            drawMenuButtons()

def videoInit():
    global video_file
    global running_video
    running_video = video_file[rd.choice(["MenuVideo1","MenuVideo2"])].iter_frames(fps = 30, dtype = "uint8")

def eventListener():
    global running,isMenu,volLev,x,y,screen,isFullScreen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            mouseX, mouseY = pg.mouse.get_pos()
            if playButton.posX <= mouseX <= playButton.posX + playButton.width and playButton.posY <= mouseY <= playButton.posY + playButton.height:
                playButton.color = (1, 1, 8)
            elif settingsButton.posX <= mouseX <= settingsButton.posX + settingsButton.width and settingsButton.posY <= mouseY <= settingsButton.posY + settingsButton.height:
                settingsButton.color = (1, 1, 8)
            elif quitButton.posX <= mouseX <= quitButton.posX + quitButton.width and quitButton.posY <= mouseY <= quitButton.posY + quitButton.height:
                quitButton.color = (1, 1, 8)
            else:
                playButton.color = (5, 4, 33)
                settingsButton.color = (5, 4, 33)
                quitButton.color = (5, 4, 33)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouseX, mouseY = pg.mouse.get_pos()
            if playButton.posX <= mouseX <= playButton.posX + playButton.width and playButton.posY <= mouseY <= playButton.posY + playButton.height:
                isMenu = False
                tutorialMap()
            elif settingsButton.posX <= mouseX <= settingsButton.posX + settingsButton.width and settingsButton.posY <= mouseY <= settingsButton.posY + settingsButton.height:
                isMenu = False
                opptionsMenu()
            elif back_arrow.posX <= mouseX <= back_arrow.posX + back_arrow.width and back_arrow.posY <= mouseY <= back_arrow.posY + back_arrow.height:
                isMenu = True
                mainMenu()
            elif volumeButtonA.posX <= mouseX <= volumeButtonA.posX + volumeButtonA.width and volumeButtonA.posY <= mouseY <= volumeButtonA.posY + volumeButtonA.height:
                volLev += 1
                if volLev > 100:
                    volLev = 100
                volumeText.text = f"Volume {volLev}"
                volumeText.clear()
                volumeText.drawText()
            elif volumeButtonS.posX <= mouseX <= volumeButtonS.posX + volumeButtonS.width and volumeButtonS.posY <= mouseY <= volumeButtonS.posY + volumeButtonS.height:
                volLev -= 1
                if volLev < 0:
                    volLev = 0
                volumeText.text = f"Volume {volLev}"
                volumeText.clear()
                volumeText.drawText()
            elif resButtonA.posX <= mouseX <= resButtonA.posX + resButtonA.width and resButtonA.posY <= mouseY <= resButtonA.posY + resButtonA.height:
                if x == 1080 and y == 720:
                    x = 1920
                    y = 1080
                elif x == 1920 and y == 1080:
                    x = 1080
                    y = 720
                screen = pg.display.set_mode((x,y))
                resolutionText.text = f"Width = {x}, height = {y}"
                volumeText.drawText()
                volumeButtonA.drawButton()
                volumeButtonS.drawButton()
                resButtonA.drawButton()
                resButtonMode.drawButton()
                back_arrow.drawImage()
                resolutionText.clear()
                resolutionText.drawText()
            elif resButtonMode.posX <= mouseX <= resButtonMode.posX + resButtonMode.width and resButtonMode.posY <= mouseY <= resButtonMode.posY + resButtonMode.height:
                if isFullScreen == 0:
                    isFullScreen = pg.FULLSCREEN
                else:
                    isFullScreen = 0
                screen = pg.display.set_mode((x,y), isFullScreen)
                resolutionText.text = f"Width = {x}, height = {y}"
                volumeText.drawText()
                volumeButtonA.drawButton()
                volumeButtonS.drawButton()
                resButtonA.drawButton()
                resButtonMode.drawButton()
                back_arrow.drawImage()
                resolutionText.clear()
                resolutionText.drawText()

def videoPlay():
    global video_file
    global running_video
    global frame
    try:
        frame = next(running_video)
    except StopIteration:
        running_video = video_file[rd.choice(["MenuVideo1","MenuVideo2"])].iter_frames(fps = 30, dtype = "uint8")
        frame = next(running_video)

def videoShow():
    global running_video
    global frame
    frame = next(running_video)
    video_surface = pg.surfarray.make_surface(frame.swapaxes(0,1))
    screen.blit(video_surface, (0,0))

def drawMenuButtons():
    global playButton
    playButton.drawButton()
    settingsButton.drawButton()
    quitButton.drawButton()

def tutorialMap():
    while isMenu == False:
        global screen
        drawMap(tutorial_map,tutorial_objects_map)
        pg.display.flip()

def opptionsMenu():
    global isMenu
    if isMenu == False:
        screen.fill((0,0,0))
        volumeText.drawText()
        volumeButtonA.drawButton()
        volumeButtonS.drawButton()
        resolutionText.drawText()
        resButtonA.drawButton()
        resButtonMode.drawButton()
        back_arrow.drawImage()

def drawMap(map, obj): # Funkcja rysująca mapę oraz obiekty
    # Iteracja przez każdą komórkę mapy w celu narysowania odpowiednich kafelków.
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            # Rysowanie kafelka na ekranie w odpowiedniej pozycji.
            screen.blit(tiles[tile], (x * tile_size, y * tile_size ))
     # Iteracja przez każdą komórkę obiektów w celu narysowania odpowiednich obiektów.
    for y, row in enumerate(obj):
        for x, tile in enumerate(row):
            # Rysowanie obiektu na ekranie w odpowiedniej pozycji.
            screen.blit(objects[tile], (x * tile_size, y * tile_size))

game()