# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:04:19 2023

@author: theod
"""

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
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
        self.image = pygame.image.load('../graphics/entities/player/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -14)
        
        self.collision_sprites = collision_sprites
        
        self.speed = 5
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        self.direction = pygame.math.Vector2(0,0)
        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.direction.x = 1
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direction.x = -1
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.direction.y = -1
        if keys[pygame.K_s] and not keys[pygame.K_w]:
            self.direction.y = 1
            
        if self.direction.magnitude() != 0: # Can't normalise zero vector
            self.direction = self.direction.normalize()
    
    def move(self, speed):
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.collision_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        
        if direction == 'vertical':
            for sprite in self.collision_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
    
    def update(self):
        self.input()
        self.move(self.speed)