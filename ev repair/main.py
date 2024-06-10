import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Beginning")

# Load images
car = pygame.image.load("car.png")
car_image = pygame.transform.scale(car, (140, 90))
car_rect = car_image.get_rect()
car_rect.x = -25
car_rect.y = 400
car_speed = 2

car2 = pygame.image.load("car2.png")
car2_image = pygame.transform.scale(car2, (140, 90))
car2_rect = car2_image.get_rect()
car2_rect.x = 700
car2_rect.y = 400
car2_speed = 2

clock = pygame.time.Clock()

# Text setup
my_font = pygame.font.SysFont('Impact', 80)
text = my_font.render('Loading...', True, (255, 0, 0))
text_rect = text.get_rect(center=(400, 150))
text_alpha = 255  # Initial alpha value
text_speed = 1
text_direction = 1

# Sound setup
crash = pygame.mixer.Sound("crash.mp3")
crash_sound_played = False

# State flag
transition_complete = False

def welcome():
    screen.fill((0, 0, 0))
    pygame.display.flip()

def loading():
    global car_speed, car2_speed, text_alpha, text_direction, crash_sound_played, transition_complete
        # im sorry ms quan i know we didn't learn this but it is so helpful here to organize our code pls dont fail us 
    
    text_rect.y += text_speed * text_direction

    # Move the cars based off car speed 
    car_rect.x += car_speed
    car2_rect.x -= car2_speed

    # Change direction if the text hits the top or bottom of the screen
    if text_rect.top <= 100 or text_rect.bottom >= 250:
        text_direction *= -1

    # Check for collision between the cars
    if car_rect.colliderect(car2_rect):
        # Stop the cars
        if text_alpha > 0:
            text_alpha -= 5  # Decrease the alpha value to fade out the text
        else:
            text_alpha = 0
            transition_complete = True
        if not crash_sound_played:
            crash.play()
            crash_sound_played = True

    # Update text surface with new alpha value
    text.set_alpha(text_alpha)

    # Draw everything
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

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if not transition_complete:
        # Move the text
        loading()
    else:
        welcome()  # Transition to the next screen
