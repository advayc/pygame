""" 
Basic image loading as a Surface, and mouse events
"""
import pygame, sys
from pygame.locals import QUIT

pygame.init()
pygame.display.set_caption("click to change the image!")

dog=pygame.image.load("dog.jpg")
chess=pygame.image.load('chess.jpg')
bird=pygame.image.load('bird.jpg')
monkey=pygame.image.load('monkey.jpg')
snowman=pygame.image.load('snowman.jpg')

#the display will not change, so we can blit & flip the display just once first
screen = pygame.display.set_mode(dog.get_size())  #using image's size to determine the window size
pygame.display.flip()
clock = pygame.time.Clock()
print('Press one of the following keys: \n1 -> dog picture \n2-> chess picture \n3 -> bird picture \n4 -> monkey picture \n5 -> snowman picture ')
while True:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                screen = pygame.display.set_mode(dog.get_size())  #using image's size to determine the window size
                screen.blit(dog, (0,0))
                pygame.display.flip()
            elif ev.key == pygame.K_2:
                screen=pygame.display.set_mode(chess.get_size())
                screen.blit(chess, (0,0))
                pygame.display.flip()
            elif ev.key == pygame.K_3:
                screen=pygame.display.set_mode(bird.get_size())
                screen.blit(bird, (0,0))
                pygame.display.flip()
            elif ev.key == pygame.K_4:
                screen=pygame.display.set_mode(monkey.get_size())
                screen.blit(monkey, (0,0))
                pygame.display.flip()
            elif ev.key == pygame.K_5:
                screen=pygame.display.set_mode(snowman.get_size())
                screen.blit(snowman, (0,0))
                pygame.display.flip()

pygame.quit()
