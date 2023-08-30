# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:12:49 2023

@author: theod
"""
import pygame
from settings import WIDTH, HEIGHT

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
    
    def run(self):
        running = True
        dt = 0
        
        while running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                        
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")
            
            # flip() the display to put your work on screen
            pygame.display.flip()

            #clock.tick(60) limits FPS to 60
            dt = self.clock.tick(60) / 1000

        pygame.quit()