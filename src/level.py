# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:30:08 2023

@author: theod
"""
import pygame
from tile import Tile
from player import Player
from settings import TILE_SIZE
import random
from groups import YSortCameraGroup

class Level:
    def __init__(self):
        # get display surface
        self.display = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup(self.display)
        self.collision_sprites = pygame.sprite.Group()
            
        self.load_level()
        
    def load_level(self):
        m = [
            ['x','','','',''],
            ['x','','','x','p'],
            ['x','','','x',''],
            ['x','','','','x'],
            ]
        
        for i in range(0, 100):
            Tile(pygame.Vector2(random.randint(1, 100)*TILE_SIZE, random.randint(1, 100)*TILE_SIZE), [self.visible_sprites, self.collision_sprites])
        
        for row_index, row in enumerate(m):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'x':
                    Tile(pygame.Vector2(x, y), [self.visible_sprites, self.collision_sprites])
                if col == 'p':
                    self.player = Player(pygame.Vector2(x, y), [self.visible_sprites], self.collision_sprites)
    
    def run(self):
        self.visible_sprites.custom_draw(self.player.rect.center)
        self.visible_sprites.update()