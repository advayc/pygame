import pygame, sys
from pygame.locals import QUIT
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Race")
car = pygame.image.load("car.png")
car_image=pygame.transform.scale(car, (106.25,58.75))
car_rect = car_image.get_rect()
car_rect.x = 50
car_rect.y = 200
triangle_color = (255, 0, 0)
tx = 50 
ty = 400

clock = pygame.time.Clock()
my_font = pygame.font.SysFont("Inter", 120)
c=''
text = my_font.render(c, True, (255, 0, 0))

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    car_rect.x += 5

    screen.fill((255, 255, 255))

    screen.blit(car_image, car_rect)

    pygame.draw.polygon(screen, triangle_color, [(tx, ty - 20),
                                                  (tx - 20, ty + 20),
                                                  (tx + 20, ty + 20)])
    tx += 4 
    pygame.display.flip()

    if car_rect.right >= screen_width:
        c='Car wins!'
        text = my_font.render(c, True, (55,125,255))
        car_rect.x -= 5
        tx -= 4
        screen.blit(text, (200,200))
        pygame.display.flip()
