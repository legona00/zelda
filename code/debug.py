import pygame
#This file
pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    display_surace = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surace, 'Black', debug_rect)
    display_surace.blit(debug_surf, debug_rect)