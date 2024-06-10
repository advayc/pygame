import pygame, sys
from pygame.locals import QUIT
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Beginning")

# CAR 1 (forwards)

car = pygame.image.load("car.png")
car_image=pygame.transform.scale(car, (140,90))
car_rect = car_image.get_rect()
# Initial position of the car (start from the left edge)
car_rect.x = -25
car_rect.y = 400
car_speed = 2

# CAR 2 (backwards)

car2 = pygame.image.load("car2.png")
car2_image=pygame.transform.scale(car2, (140,90))
car2_rect = car2_image.get_rect()
# Initial position of the car (start from the right edge)
car2_rect.x = 700
car2_rect.y = 400
car2_speed = 2


clock = pygame.time.Clock()

# Text
my_font = pygame.font.SysFont('Impact', 80)
text = my_font.render('Loading...', True, (255, 0, 0))
text_rect = text.get_rect(center=(400, 150))
text_alpha = 255  # Initial alpha value --> alpha is the transparency level of a surface (0-255)
# Text Movement
text_speed = 1
text_direction = 1

# Sound
crash = pygame.mixer.Sound("crash.mp3") #used for a sound effect
crash_sound_played = False

def next():
    screen.fill((0,0,0))
    pygame.display.flip()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Move the text
    text_rect.y += text_speed * text_direction

    # Car Speed Movement
    car_rect.x += car_speed
    car2_rect.x -= car2_speed

    # Change direction if the text hits the top or bottom of the screen
    if text_rect.top <= 100 or text_rect.bottom >= 250:
        text_direction *= -1
    
    # Check for collision between the cars
    if car_rect.colliderect(car2_rect):
        if text_alpha > 0:
            text_alpha -= 5  # Decrease the alpha value to fade out the text
        else:
            text_alpha = 0
        if not crash_sound_played:
            crash.play()
            crash_sound_played = True
    # Update text surface with new alpha value
    text.set_alpha(text_alpha)
    
    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)
    screen.blit(car_image, car_rect)
    screen.blit(car2_image, car2_rect)
    pygame.display.flip()

    if car_rect.right > 415:
        car_rect.x -= 2
        pygame.display.flip()
    if car2_rect.left < 400:
        car2_rect.x += 2
        pygame.display.flip()

    if text_alpha == 0:
        next()