import pygame
from pygame import mixer
import Player
import BrickWall
import random
import SoundOptions

pygame.init()

#Properties ---------------------------------------------------------------------------

width = 1280
height = 720
resolution = (width, height)
title = "Flappy Bird"
frames = 60
backgroundFile = "background2.png"
gravity = .7
jump = 15
menuImage = "menudesign.png"
pauseImage = "pauselabel.png"
scoreBoardImage = "loselabel.png"
restartlabelImage = "restartlabel.png"
jumpLabelImage = "jump.png"
drawHitBoxes = False
iconFile = "ani2.png"

#Sound Files --------------------------------------------------------------------------

loseSoundFile = "losesound.wav"
getPointSoundFile = "getpointsound.wav"
jumpSoundFile = "jump.wav"
song1 = "buymode1.mp3"
readysetFile = "readyset.wav"
goFile = "go.wav"

soundEffects = []


#Sound Variables ----------------------------------------------------------------------

loseSound = pygame.mixer.Sound(loseSoundFile)
soundEffects.append(loseSound)

pointSound = mixer.Sound(getPointSoundFile)
soundEffects.append(pointSound)

jumpSound = mixer.Sound(jumpSoundFile)
soundEffects.append(jumpSound)

readySound = mixer.Sound(readysetFile)
soundEffects.append(readySound)

goSound = mixer.Sound(goFile)
soundEffects.append(goSound)

mixer.music.load(song1)


#Quick Variables ----------------------------------------------------------------------
black = (0, 0, 0)
white = (255, 255, 255)
background = pygame.image.load(backgroundFile)
pause = pygame.image.load(pauseImage)
menu = pygame.image.load(menuImage)
scoreboard = pygame.image.load(scoreBoardImage)
restartlabel = pygame.image.load(restartlabelImage)
jumpLabel = pygame.image.load(jumpLabelImage)
icon = pygame.image.load(iconFile)


#Adjustments --------------------------------------------------------------------------
background = pygame.transform.scale(background, (1920, 1080))
pause = pygame.transform.scale(pause, (211, 66))
scoreboard = pygame.transform.scale(scoreboard, (417, 260))
restartlabel = pygame.transform.scale(restartlabel, (277, 68))
jumpLabel = pygame.transform.scale(jumpLabel, (320, 82))
pygame.display.set_icon(icon)

backGroundx = 0
backGroundy = -300

mixer.music.set_volume(.25)
for sound in soundEffects:
    sound.set_volume(.25)

#Setup Screen -------------------------------------------------------------------------
screen1 = pygame.display.set_mode(resolution)
pygame.display.set_caption(title)

#Run game -----------------------------------------------------------------------------



clock = pygame.time.Clock()

optionMenu = SoundOptions.SoundOptions(soundEffects[0])

running = True

player = Player.Player()
player.xPos = width*.25
player.yPos = height*.5

startX = player.xPos
startY = player.yPos

player.update()

brickWalls = []
seconds = 0
seconds2 = 0
spawnRate = 60
bricksSpawned = 0
points = 0
lose = False
gapMax = 50
changedPicture = False

optionMenu = SoundOptions.SoundOptions(soundEffects[0])
#Text Settings ------------------------------------------------------------------------

font = pygame.font.Font('coolvetica.ttf', 64)
myStr = str(player.points)
text = font.render(myStr, True, black)

#Functions ----------------------------------------------------------------------------
def resetGame():
    global brickWalls
    global lose
    global gapMax
    global spawnRate
    global startX
    global startY
    global seconds
    global background
    global changedPicture

    changedPicture = False

    background = pygame.image.load("background2.png")
    background = pygame.transform.scale(background, (1920, 1080))

    seconds = 0

    brickWalls.clear()
    gapMax = 50
    spawnRate = 60

    player.xPos = startX
    player.yPos = startY
    player.ySp = 0

    player.resetPoints()
    lose = False

def currentLevel(currentPoints):
    global gapMax
    global spawnRate
    global background
    global changedPicture

    
    
    if currentPoints == 10 and not changedPicture:
        spawnRate = 45
        #background = pygame.image.load("background.png")
        #background = pygame.transform.scale(background, (1920,1080))
        #changedPicture = True
        return 2
    elif currentPoints > 11 and currentPoints <= 30:
        changedPicture = False
        return 2
    elif currentPoints > 30 and currentPoints <= 40:
        gapMax = 75
        return 3
    elif currentPoints > 40 and currentPoints <= 70:
        spawnRate = 35
        return 4
    elif currentPoints > 70 and currentPoints <= 100:
        gapMax = 100
        return 5


#Interfaces ---------------------------------------------------------------

def getReadyScreen():
    
    readyS = 0
    timer = 0

    while not readyS == 180:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                    return

        screen1.blit(background, (backGroundx, backGroundy))

        for wall in brickWalls:
            wall.draw(screen1)

        player.drawPlayer(screen1)

        if readyS%frames == 0:
            timer += 1

            myStr = str(timer)
            readySound.play()
                    
        screen1.blit(pause, (25, 25))
        screen1.blit(jumpLabel, (width/2 - 200, height - 100))

        
        text = font.render(myStr, True, white)
        screen1.blit(text, (width/2 - 30, height/2 - 30))

        readyS += 1
        clock.tick(frames)
        pygame.display.flip()

    goSound.play()

    return False


def loserScreen():

    global lose
    global tempGravity

    loseSound.play()

    while lose:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetGame()
                    loseSound.stop()
                    lose = False
                    player.xPos = startX
                    player.yPos = startY
                    
                    return
                                        
        screen1.blit(background, (backGroundx,backGroundy))
        for walls in brickWalls:
            walls.draw(screen1)
            walls.update()

            if walls.xPos < -50:
                brickWalls.remove(walls)

        player.update()
        player.drawPlayer(screen1)

        screen1.blit(scoreboard, (width/3, height/3 - 50))
        screen1.blit(restartlabel, (width/3 + 70, height - 250))

        myStr = str(player.points)
        text = font.render(myStr, True, black)
        screen1.blit(text, (width/2 - 25, height/3 + 100))
        
        player.fall(2)

        clock.tick(frames)
        pygame.display.flip()

def playRound():
    if getReadyScreen():
        return

    global lose 
    global frames
    global seconds
    global spawnRate
    global bricksSpawned
    global points
    global myStr
    global seconds2
    global drawHitBoxes

    global gapMax

    while not lose:
        seconds += 1
        seconds2 += 1

        if seconds2 == frames:
            seconds2 = 0

        if seconds >= spawnRate:

            gap = random.randint(0, gapMax)
            offset = random.randint(-300, 300)
            wall1 = BrickWall.BrickWall()
            wall2 = BrickWall.BrickWall()
            wall2.hasPassed = True

            wall1.xPos = width + 50
            wall1.yPos = height - gap/2 + offset

            wall2.xPos = width + 50
            wall2.yPos = gap/2 + offset


            brickWalls.append(wall1)
            brickWalls.append(wall2)
            seconds = 0

        currentLevel(player.points)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_SPACE:
                    player.jump(jump, jumpSound)

                elif event.key == pygame.K_h:
                    if drawHitBoxes:
                        drawHitBoxes = False

                    else:
                        drawHitBoxes = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    pass



        for walls in brickWalls:
            walls.draw(screen1)

            if walls.xPos < -50:
                brickWalls.remove(walls)

            if player.hasCollide(walls.hitBox):
                player.ySp = -15
                lose = True
                loserScreen()
                return

        if player.isOutOfBounds(width, height):
            lose = True
            loserScreen()
            return

        player.fall(gravity)
        player.update()
                     
        

        screen1.blit(background, (backGroundx, backGroundy))


        for walls in brickWalls:
            walls.update()
            walls.draw(screen1)
            if drawHitBoxes:
                walls.drawHitBox(screen1)

            player.hasPassed(walls, pointSound)


        myStr = str(player.points)
        text = font.render(myStr, True, black)
        screen1.blit(text, (width/2, 20))
    

        player.drawAnimation(screen1, seconds2)

        if drawHitBoxes:
            player.drawHitBox(screen1)
               
        screen1.blit(pause, (25, 25))
        #screen1.blit(jumpLabel, (width/2 - 200, height - 100))

        clock.tick(frames)
        pygame.display.flip()

def runMenu():
    global frames

    screen1.blit(background, (backGroundx, backGroundy))
   
    
    for walls in brickWalls:
        walls.draw(screen1)

        if walls.xPos < 0:
            brickWalls.remove(walls)

    
    player.drawPlayer(screen1)
    
    screen1.blit(menu, (.25*width, 25))

    clock.tick(frames)
    pygame.display.flip()

def play():
    global frames
    global lose
     
    mixer.music.play(-1)

    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not lose:
                        playRound()
                    
                elif event.key == pygame.K_q:
                    running = False

                elif event.key == pygame.K_r:
                    resetGame()

                elif event.key == pygame.K_o:

                    optionMenu.start(soundEffects)

            else:
                runMenu()

        clock.tick(15)
        pygame.display.flip()

play()

