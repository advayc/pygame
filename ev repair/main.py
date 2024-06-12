import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("EV REPAIR")
page = 0

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
my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 80)
text = my_font.render('Loading...', True, (255, 0, 0))
text_rect = text.get_rect(center=(400, 150))
text_alpha = 255  # Initial alpha value
text_speed = 1
text_direction = 1

# Background Sound
bg_sound = pygame.mixer.Sound("sound.mp3")
bg_sound.play(-1)  # Play the background sound in a loop

# Sound setup
crash = pygame.mixer.Sound("crash.mp3")
crash_sound_played = False
transition_complete = False

def welcome():
    global page
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 125)
    text = my_font.render('EV REPAIR', True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 150))
    screen.fill((40, 40, 40))

    # Render the outline
    for x in range(-3, 4):
        for y in range(-3, 4):
            outline = my_font.render('EV REPAIR', True, (0, 0, 0))
            screen.blit(outline, (text_rect.x + x, text_rect.y + y))

    # Draw Rectangle for Start
    pygame.draw.rect(screen, (0, 0, 0), [50, 350, 250, 100], 250)
    my_font2 = pygame.font.Font('FrancoisOne-Regular.ttf', 70)
    text2 = my_font2.render('Start', True, (255, 255, 255))
    text2_rect = text2.get_rect(center=(175, 400))
    screen.blit(text2, text2_rect)

    # Instructions rect, text
    pygame.draw.rect(screen, (0, 0, 0), [350, 350, 400, 100], 0)
    text3 = my_font2.render('Instructions', True, (255, 255, 255))
    text3_rect = text3.get_rect(center=(550, 400))
    screen.blit(text3, text3_rect)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)
    
    # Render the text
    screen.blit(text, text_rect)
    pygame.display.flip()

def loading():
    global page, car_speed, car2_speed, text_alpha, text_direction, crash_sound_played, transition_complete
    page = 1
    text_rect.y += text_speed * text_direction

    # Move the cars based on car speed 
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
            transition_complete = True
        if not crash_sound_played:
            crash.play()
            crash_sound_played = True
            bg_sound.stop()  # Stop the background sound when the crash sound is played

    # Update text surface with new alpha value
    text.set_alpha(text_alpha)

    # Draw everything
    screen.fill((40, 40, 40))
    screen.blit(text, text_rect)
    screen.blit(car_image, car_rect)
    screen.blit(car2_image, car2_rect)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)
    
    pygame.display.flip()

    if car_rect.right > 415:
        car_rect.x -= 2
        pygame.display.flip()
    if car2_rect.left < 400:
        car2_rect.x += 2
        pygame.display.flip()

def roadmap():
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), [315, 95, 160, 160], 75)
    pygame.draw.rect(screen, (255, 255, 255), [115, 95, 160, 160], 75)
    pygame.draw.rect(screen, (255, 255, 255), [515, 95, 160, 160], 75)
    pygame.draw.rect(screen, (255, 255, 255), [315, 345, 160, 160], 75)
    pygame.draw.rect(screen, (255, 255, 255), [115, 345, 160, 160], 75)
    pygame.draw.rect(screen, (255, 255, 255), [515, 345, 160, 160], 75)

    image = pygame.image.load("sensor.png")
    img = pygame.transform.scale(image, (150, 150))
    img = img.convert()
    screen.blit(img, (120, 100))

    image2 = pygame.image.load("carcam.png")
    img2 = pygame.transform.scale(image2, (150, 150))
    img2 = img2.convert()
    screen.blit(img2, (320, 100))

    image3 = pygame.image.load("motor.png")
    img3 = pygame.transform.scale(image3, (150, 150))
    img3 = img3.convert()
    screen.blit(img3, (520, 100))

    image4 = pygame.image.load("battery.png")
    img4 = pygame.transform.scale(image4, (150, 150))
    img4 = img4.convert()
    screen.blit(img4, (120, 350))

    image5 = pygame.image.load("radiator.png")
    img5 = pygame.transform.scale(image5, (150, 150))
    img5 = img5.convert()
    screen.blit(img5, (320, 350))

    image6 = pygame.image.load("charger.png")
    img6 = pygame.transform.scale(image6, (150, 150))
    img6 = img6.convert()
    screen.blit(img6, (520, 350))

    myfont = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    label = myfont.render("Sensors", True, (255, 255, 255))
    screen.blit(label, (145, 260))

    label = myfont.render("Cameras", True, (255, 255, 255))
    screen.blit(label, (345, 260))

    label = myfont.render("Motor", True, (255, 255, 255))
    screen.blit(label, (550, 260))

    label = myfont.render("Battery", True, (255, 255, 255))
    screen.blit(label, (145, 510))

    label = myfont.render("Cooling", True, (255, 255, 255))
    screen.blit(label, (345, 510))

    label = myfont.render("Charger", True, (255, 255, 255))
    screen.blit(label, (545, 510))

    label = myfont.render("Part = Level", True, (255, 255, 255))
    screen.blit(label, (350, 560))

    label = myfont.render("Parts: ", True, (255, 255, 255))
    screen.blit(label, (75, 30))

    myfont = pygame.font.Font("FrancoisOne-Regular.ttf", 50)
    label = myfont.render("Part List", True, (255, 255, 255))
    screen.blit(label, (320, 20))

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)
    
    pygame.display.flip()

def track1():
    screen.fill((0, 0, 0))
    track1 = pygame.image.load("track1.png")
    track1 = track1.convert()
    screen.blit(track1, (0, 0))

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)
    
    pygame.display.flip()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if x > 675 and x < 750 and y > 25 and y < 75:  # Adjusted coordinates for "back" button
                page -= 1 # back button
            if page == 2 and x > 50 and x < 300 and y > 350 and y < 450: 
                page = 3
            if page == 3 and x > 100 and x < 300 and y > 100 and y < 260:
                page = 4
            if page == 2 and x > 350 and x < 770 and y > 350 and y < 450:
                print('instruct')

    if page == 0:
        loading()
    elif page == 1:
        if transition_complete:
            page = 2
        else:
            loading()
    elif page == 2:
        welcome()
    elif page == 3:
        roadmap()
    elif page == 4:
        track1()
