# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:37:34 2023

@author: theod
"""
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        """
        

        Parameters
        ----------
        pos : Pygame Vector2
            DESCRIPTION.
        groups : Array of Pygame Groups
            Used to associate sprite with correct groups (e.g., render, collide)

        Returns
        -------
        None.

        """
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/scene/cobble.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -2)  #-10 would mean -5 pixels each side
        # inflate changes the size of the rectangle. This is useful for z layering. Keeps centre point the same
        # the rectangle will always follow the hitbox (move hitbox and perform collisions beforehand)