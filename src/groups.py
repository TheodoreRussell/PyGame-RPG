# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:42:04 2023

@author: theod
"""
import pygame

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, display):
        super().__init__()
        self.display = display
        self.window_half_size = pygame.math.Vector2(self.display.get_size()) // 2
        
    def custom_draw(self, camera_pos):
        # Camera Pos = Player pos for basic static tracking
        offset = pygame.math.Vector2(camera_pos) - self.window_half_size
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery ):
            offset_pos = sprite.rect.topleft - offset
            self.display.blit(sprite.image, offset_pos)