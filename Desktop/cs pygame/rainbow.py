"""
A basic framework for games.
"""

import pygame, sys                          # import & initialize the pygame module
from pygame.locals import QUIT
pygame.init()                            

size = (640, 480) 
screen = pygame.display.set_mode(size) 			  # screen is now a Surface type object
pygame.display.set_caption("Blah May31 ")   	# caption appears in the title bar
background = pygame.Surface(size).convert() 	# creates a Surface object
background.fill((0, 0, 255)) 		              # (red, green, blue)
colours = pygame.color.THECOLORS

#The game loop
clock = pygame.time.Clock() 		              # controls the frame rate
while True:
  clock.tick(60) 			                        # frame rate at 30 frames per second
  for ev in pygame.event.get():			          # Handle any events in the current frame 
  #Events are objects with a type instance variable (an int, linked to pygame constants).
  #These types could be a certain key pressed, a mouse moved, or even a guitar strum!
  #These event types are mapped to constants in the pygame class.
     
    if ev.type == pygame.QUIT:            # if the x button is pressed
      pygame.quit()
      sys.exit()
    elif ev.type == pygame.KEYDOWN:       # if it was a keyboard press
      if ev.key == pygame.K_1:                # check to see which letter is pressed 
        background.fill((148, 0, 211))          # fill the background red
        pygame.display.set_caption("VIOLET!")    # update the caption
      elif ev.key == pygame.K_2:
        background.fill((75, 0, 130))
        pygame.display.set_caption("PURPLE!")
      elif ev.key == pygame.K_3:
        background.fill((0, 0, 255))
        pygame.display.set_caption("BLUE!")
      elif ev.key == pygame.K_4:
        background.fill((0, 255, 0))
        pygame.display.set_caption("GREEN!")
      elif ev.key == pygame.K_5:
        background.fill((255, 255, 0))
        pygame.display.set_caption("YELLOW!")
      elif ev.key == pygame.K_6:
        background.fill((255, 127, 0))
        pygame.display.set_caption("ORANGE!")
      elif ev.key == pygame.K_7:
        background.fill((255, 0, 0))          
        pygame.display.set_caption("RED!")

    
  #Update and refresh the display to end this frame
  screen.blit(background, (0, 0)) #'blit' means to copy the updated background to the screen. 
  pygame.display.flip()           # refresh the display
