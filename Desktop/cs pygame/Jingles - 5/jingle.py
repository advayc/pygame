""" 
Adding sounds to our animation
"""


import pygame, sys, os

from pygame.locals import QUIT

pygame.init()


screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size()).convert()
background.fill((0, 0, 0))


bounce = pygame.mixer.Sound("Jingle.mp3") #used for a sound effect
pygame.mixer.music.set_volume(0.06)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

while True:
  clock.tick(30)
  for ev in pygame.event.get():
    if ev.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif ev.type == pygame.MOUSEBUTTONDOWN: #90,350,100,35
        jingle.play()
    elif ev.type == pygame.KEYDOWN:
      if ev.key == pygame.K_UP:
        jingle.play()
      elif ev.key == pygame.K_DOWN:
        jingle.play()


  screen.blit(background, (0, 0))
  pygame.display.flip()

pygame.quit()
