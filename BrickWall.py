import pygame


class BrickWall:

    def __init__(self):
        self.width = 50
        self.height = 400

        self.xPos = -300
        self.yPos = -300
        self.xSp = -10
        self.ySp = 0
        self.imageName = "brickwall.png"
        self.image = pygame.image.load(self.imageName)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.centerLocation = self.image.get_rect(center = (self.xPos, self.yPos))
        self.hitBox = (self.xPos - self.width/2, self.yPos - self.height/2, self.width, self.height)
        self.hasPassed = False
        


    def drawHitBox(self, screen):
        print(self.hitBox, "wall")
        pygame.draw.rect(screen, (255, 0, 0), self.hitBox, 2)

    def update(self):
        self.xPos += self.xSp
        self.yPos += self.ySp
        self.centerLocation = self.image.get_rect(center = (self.xPos, self.yPos))
        self.hitBox = (self.xPos - self.width/2, self.yPos - self.height/2, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.image, self.centerLocation)

