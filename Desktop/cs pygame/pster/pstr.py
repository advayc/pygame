import pygame, sys
from pygame.locals import QUIT

def gotoPage3(screen, background):
    
    background.fill((5, 20, 23))
    image=pygame.image.load('dbird.jpg')
    img = pygame.transform.scale(image, (366.25,244.125))
    img = img.convert()

    #                   what        color    where on bg    width
    pygame.draw.rect(background, (179, 237, 252),[90,350,100,35], 50)
    pygame.draw.rect(background, (179, 237, 252),[270,350,100,35], 50)
    pygame.draw.rect(background, (179, 237, 252),[440,350,100,35], 50)
    screen.blit(background, (0, 0))
    screen.blit(img, (130, 25))
    
def gotoPage2(screen, background):
    
    background.fill((6, 23, 5))
    image=pygame.image.load('eagle.webp')
    img = pygame.transform.scale(image, (222.25,222.25))
    img = img.convert()

    #                   what        color    where on bg    width
    pygame.draw.rect(background, (183, 252, 179),[90,350,100,35], 50)
    pygame.draw.rect(background, (183, 252, 179),[270,350,100,35], 50)
    pygame.draw.rect(background, (183, 252, 179),[440,350,100,35], 50)
    screen.blit(background, (0, 0))
    screen.blit(img, (190, 25))
 
def gotoPage1(screen, background):
    
    background.fill((23, 5, 5))
    image=pygame.image.load('bird.jpg')
    img=pygame.transform.scale(image, (320, 213))
    img = img.convert()

    #                   what        color    where on bg    width
    pygame.draw.rect(background, (255, 163, 163),[90,350,100,35], 50)
    pygame.draw.rect(background, (255, 163, 163),[270,350,100,35], 50)
    pygame.draw.rect(background, (255, 163, 163),[440,350,100,35], 50)
    screen.blit(background, (0, 0))
    screen.blit(img, (150, 25))


pygame.init()
size=(640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Click a box')
background = pygame.Surface(size).convert()

pageNumber = 1

clock = pygame.time.Clock()
while True:
    if pageNumber == 1:
        gotoPage1(screen, background)
        
    elif pageNumber == 2:
        gotoPage2(screen, background)
        
    elif pageNumber == 3:
        gotoPage3(screen, background)
        
        
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: #90,350,100,35
            x = event.pos[0]
            y = event.pos[1]
            if x >=90 and x <= 180 and y >=350 and y <=380 and pageNumber == 1: # button one 
                print('You are already on Page 1!!')
            elif x >=270 and x <= 370 and y >=350 and y <=380 and pageNumber == 2: # button two
                print('You are already on page 2!!')
            elif x >=450 and x <=550 and y >=350 and y <=380 and pageNumber == 3: # button three
                print("You are already on page 3!!")
            elif x >=90 and x <= 180 and y >=350 and y <=380 and pageNumber == 2 or pageNumber == 3: # button one 
                pageNumber = 1
            elif x >=270 and x <= 370 and y >=350 and y <=380 and pageNumber == 1 or pageNumber == 3: # button two
                pageNumber = 2
            elif x >=450 and x <=550 and y >=350 and y <=380 and pageNumber == 1 or pageNumber == 2: # button three
                pageNumber = 3
    
    pygame.display.update() 