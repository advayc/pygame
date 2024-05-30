""" 
Basic image loading as a Surface, and mouse events
"""
import pygame, sys
from pygame.locals import QUIT

pygame.init()
pygame.display.set_caption("click to change the image!")

images = [
pygame.image.load("dog.jpg"),
pygame.image.load('chess.jpg'),
pygame.image.load('bird.jpg'),
pygame.image.load('lion.jpg'),
pygame.image.load('monkey.jpg'),
pygame.image.load('snowman.jpg'),
]
index=0

#the display will not change, so we can blit & flip the display just once first
screen = pygame.display.set_mode(images[index].get_size())  #using image's size to determine the window size

pygame.display.flip()

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            index = (index + 1) % len(images)
            screen = pygame.display.set_mode(images[index].get_size())
            screen.blit(images[index], (0, 0))
            pygame.display.flip()

pygame.quit()
