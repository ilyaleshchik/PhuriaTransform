import math
import pygame
import os
import time
import random

pygame.font.init()

class Game:
    def __init__(self, WIDTH, HEIGHT, FPS, BG, MIN_COUNT, MAX_COUNT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.FPS = FPS
        self.BG = BG
        self.clock = pygame.time.Clock()
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.waves = []
        self.TIME = 0.0
        self.RADIUS = 75
        self.MIN_COUNT = MIN_COUNT * 2
        self.MAX_COUNT = MAX_COUNT * 2
        self.count = MIN_COUNT * 2
        self.minusZone = pygame.Rect(295, 605, 15, 15)
        self.plusZone = pygame.Rect(322, 605, 15, 15)

    def Draw(self):
        """
            to do:
                1. Add a more circles
                2. Add a widget thar can conrtol the count of the circles
        """
        self.WIN.fill(self.BG)
        #Draw a circles and a graphic
        circleX = 200
        circleY = 300
        newX = 0
        newY = 0
        for k in range(1, self.count, 2):
            raduis = int(self.RADIUS * (4 / (math.pi * k)))
            pygame.draw.circle(self.WIN, (0, 0, 0), (circleX, circleY), raduis, 1)
            newX = int(raduis * math.cos(k * self.TIME))
            newY = int(raduis * math.sin(k * self.TIME)) 
            circleX += newX
            circleY += newY
            pygame.draw.line(self.WIN, (255, 0, 0), (circleX - newX, circleY - newY), (circleX, circleY), 1)

        self.waves.insert(0, circleY)
        if(len(self.waves) >= 420):
            self.waves.pop(-1)
        diagramX = 375
        for y in range(len(self.waves) - 1):
            pygame.draw.line(self.WIN, (255, 255, 255), (diagramX + y, self.waves[y]), (diagramX + y + 1, self.waves[y + 1]), 2)
            # pygame.draw.circle(self.WIN, (255, 255, 255), (diagramX + y, self.waves[y]), 2)
        pygame.draw.line(self.WIN, (0, 0, 0), (circleX, circleY), (diagramX, circleY), 1)

        #Draw a control widget
        font = pygame.font.SysFont("Impact", 20)
        label = font.render(f'- {self.count // 2} +', 1, (0, 0, 0))
        self.WIN.blit(label, (300, 600))
        # pygame.draw.rect(self.WIN, (255, 0, 0), self.minusZone)
        # pygame.draw.rect(self.WIN, (0, 0, 255), self.plusZone)
        pygame.display.update()



    def Run(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            self.Draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if(self.minusZone.collidepoint(event.pos)):
                            self.count = max(self.MIN_COUNT, self.count - 2)
                        elif (self.plusZone.collidepoint(event.pos)):
                            self.count = min(self.count + 2, self.MAX_COUNT)
            # keys = pygame.key.get_pressed()
            # if(keys[pygame.K_q]):
            #     self.count = max(2, self.count - 2)
            # if(keys[pygame.K_w]):
            #     self.count = min(self.count + 2, 10)
        
            self.TIME += 0.02



if __name__ == "__main__":
    game = Game(800, 800, 60, (116, 219, 173), 1, 10)
    game.Draw()
    game.Run()