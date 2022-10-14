import pygame
from pygame import mixer
import Player as play

pygame.init()

player = play.Player()

screen1 = pygame.display.set_mode((1280, 720))

running = True

clock = pygame.time.Clock()

player.xPos = 1280/2
player.yPos = 720/2

seconds = 0

keyPress = False

while running:
    seconds

    if seconds >= 60:
        seconds = 0

    screen1.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump(15, pygame.mixer.Sound("jump.wav"))

            elif event.key == pygame.K_d:
                player.xSp = 5
                keyPress = True

            elif event.key == pygame.K_a:
                player.xSp = -5
                keyPress = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                keyPress = False
            elif event.key == pygame.K_a:
                keyPress = False

        


    if player.xSp > 0 and not keyPress:
        player.xSp -= .1

    elif player.xSp < 0 and not keyPress:
        player.xSp += .1

    player.drawAnimation(screen1, seconds)
    player.update()

    seconds += 1


    clock.tick(60)
    pygame.display.flip()