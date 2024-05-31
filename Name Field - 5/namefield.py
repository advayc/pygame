""" 
Text input on a Surface ... alternatively explore pygame_gui https://pygame-gui.readthedocs.io/en/latest/index.html
pygame_gui was created in 2019
"""
import pygame, sys
from pygame.locals import QUIT
pygame.init()

screen = pygame.display.set_mode((640, 480))
background = pygame.Surface(screen.get_size()).convert()
background.fill((0, 0, 0)) 

field_surf = pygame.Surface((300, 50)).convert()
field_surf.fill((255,255,255))

my_font = pygame.font.SysFont("helvetica", 20)
field_value = ""
field = my_font.render(field_value, True, (0,0,0))

clock = pygame.time.Clock()
while True:
    clock.tick(30)    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:    #when enter is pressed, your text is 
              print (field_value)            #outputted on the console
              f = field_value.split()
              i = (field_value[0],f[1][0])
            elif ev.key == pygame.K_BACKSPACE and len(field_value) > 0:
                field_value = field_value[:-1] #cut off last character
            elif (ev.unicode.isalnum() or ev.key==pygame.K_SPACE) and len(field_value) < 20:
                field_value += ev.unicode #adds character value of key
            field = my_font.render(field_value, True, (0,0,0))
            text=my_font.render(i, True, (0,0,0))
    
    screen.blit(background, (0, 0))
    screen.blit(field_surf, (50, 25))
    screen.blit(field, (60, 40))
    screen.blit(text, (100,80))
    pygame.display.flip()
