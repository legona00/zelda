import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        #Initiate Tile class
        super().__init__(groups)
        #ALWAYS NEED image AND rect for sprites
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface
        if sprite_type == 'object':
            #do an offset
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
            self.hitbox = self.rect.inflate(0,-70)
        else:
            self.rect = self.image.get_rect(topleft = pos)
            self.hitbox = self.rect.inflate(0, y_offset)