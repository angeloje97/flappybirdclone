import pygame
import BrickWall

class Player:



    def __init__(self):
        self.width = 64
        self.height = 64

        self.xPos = 0
        self.yPos = 0
        self.xSp = 0.0
        self.ySp = 0.0
        self.imageFile = "birdo.png"
        self.originalImage = pygame.image.load(self.imageFile)
        self.image = pygame.image.load(self.imageFile)
        self.centerLocation = self.image.get_rect(center = (self.xPos, self.yPos))
        self.hitBox = (self.xPos - self.width/2, self.yPos - self.height/2, self.width, self.height)
        self.points = 0

        self.ani1 = "ani1.png"
        self.ani2 = "ani2.png"
        self.ani3 = "ani3.png"

        self.image1 = pygame.image.load(self.ani1)
        self.image2 = pygame.image.load(self.ani2)
        self.image3 = pygame.image.load(self.ani3)

        self.tempAni = [self.image2, self.image1, self.image2, self.image3]
        self.animations = [self.image2, self.image1, self.image2, self.image3]

    def fall(self):
        self.ySp += .3

    def update(self):
        self.yPos += self.ySp
        self.xPos += self.xSp

        self.centerLocation = self.image.get_rect(center = (self.xPos, self.yPos))
        self.hitBox = (self.xPos - self.width/2, self.yPos - self.height/2, self.width, self.height)

    def fall(self, gravity):
        self.ySp += gravity

    def jump(self, jumpValue, sound):
        self.ySp = -jumpValue
        sound.play()

    def drawHitBox(self, screen):
        print(self.hitBox, "player")
        pygame.draw.rect(screen, (255, 0, 0), self.hitBox, 2)

    def rotate(self, image):
        newImage = pygame.transform.rotozoom(image, - self.ySp * 1, 1)
        return newImage

    def drawPlayer(self, screen):
        self.centerLocation = self.image.get_rect(center = (self.xPos, self.yPos))
        self.image = self.rotate(self.originalImage)
        screen.blit(self.image, self.centerLocation)

    def drawAnimation(self, screen, frame):
        split = 16

        self.centerLocation = self.image.get_rect(center = (self.xPos, self.yPos))
        self.animations[int(frame/split)] = self.rotate(self.tempAni[int(frame/split)])
        screen.blit(self.animations[int(frame/split)], self.centerLocation)



    def hasCollide(self, hitBox2):
        result = True

        if self.hitBox[0] < hitBox2[0]:
            return False
        elif self.hitBox[0] > hitBox2[0] + hitBox2[2]:
            return False
        elif self.hitBox[1] < hitBox2[1] - 60:
            return False
        elif self.hitBox[3] + self.hitBox[1] > hitBox2[1] + hitBox2[3] + 60:
            return False

        return result

    def hasPassed(self, wall, sound):
        if self.xPos > (wall.xPos + 64) and wall.hasPassed == False:
            wall.hasPassed = True

            sound.play()
            self.points += 1
            

    def isOutOfBounds(self, width, height):
        if self.yPos < -45:
            return True
        elif self.yPos > height + 45:
            return True

    def resetPoints(self):
        self.points = 0
        

  
