import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
img = pygame.image.load("car.png").convert()

img_rect = img.get_rect()
img_rect.center = (320, 240)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                img_rect.y -= 10
            elif event.key == K_DOWN:
                img_rect.y += 10
            elif event.key == K_LEFT:
                img_rect.x -= 10
            elif event.key == K_RIGHT:
                img_rect.x += 10
    
    screen.fill((255, 255, 255))
    screen.blit(img, img_rect)
    pygame.display.flip()
