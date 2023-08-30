# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:12:49 2023

@author: theod
"""
import pygame
from settings import WIDTH, HEIGHT, FPS
from level import Level
import math

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        pygame.display.set_caption("RPG Game")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
    
    def run(self):
        running = True
        dt = 1.0
        
        while running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")
            # run the level and rendering
            self.level.run()
            # display FPS
            font = pygame.font.SysFont('helvetica.ttf', 102)
            img = font.render(str(math.floor(1.0 / dt)), True, 'white', 'black')
            self.screen.blit(img, (WIDTH-100,0))
            # flip() the display to put your work on screen
            pygame.display.flip()

            #clock.tick(60) limits FPS to 60
            dt = self.clock.tick(FPS) / 1000

        pygame.quit()