import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("EV REPAIR")
page = 0

# Load images
car = pygame.image.load("car3.png")
car_image = pygame.transform.scale(car, (130, 100))
car_rect = car_image.get_rect()
car_rect.x = 20
car_rect.y = 480
car_speed = 8

dc = pygame.image.load('car.png')
drive_car_rect = dc.get_rect()
drive_car = pygame.transform.scale(dc, (71, 39)) # Scale the image to 50x50
drive_car_rect.x = 20
drive_car_rect.y = 210
clock = pygame.time.Clock()

# Text setup
my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 40)
text = my_font.render('Loading...', True, (0, 0, 0))
text_rect = text.get_rect(center=(675, 575))
text_alpha = 255  # Initial alpha value

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
    
    # Checkered Background Opaque
    checker_bg = pygame.image.load("checker.png")
    checker = pygame.transform.scale(checker_bg, (800, 600))
    checker.set_alpha(25)
    screen.blit(checker, (0,0))
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
    global page, car_speed, text_alpha, crash_sound_played, transition_complete
    page = 1

    # Move the car based on car speed
    car_rect.x += car_speed

    # Check if the car reaches the end of the rectangle
    if car_rect.right >= 780:  # Adjust as needed to match the rectangle's end position
        car_speed = 0
        if text_alpha > 0:
            text_alpha -= 8  # Decrease the alpha value to fade out the text
        else:
            text_alpha = 0
            transition_complete = True
        if not crash_sound_played:
            crash.play()
            crash_sound_played = True
            bg_sound.stop()  # Stop the background sound when the crash sound is played

    # Update text surface with new alpha value
    text.set_alpha(text_alpha)
    # Background Loading Screen
    loading_bg = pygame.image.load("orange.png")
    bg_scale = pygame.transform.scale(loading_bg, (850, 650))
    # Create a surface with an alpha channel (per-pixel transparency)
    rect_surface = pygame.Surface((725, 50), pygame.SRCALPHA)
    # Fill the surface with a color including the alpha value
    rect_surface.fill((0, 0, 0, 128))  # Black color with 128 alpha (50% transparent)
    # Draw everything
    screen.blit(bg_scale, (-6,0))
    screen.blit(rect_surface, (40, 500))
    screen.blit(text, text_rect)
    screen.blit(car_image, car_rect)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)
    
    pygame.display.flip()


def roadmap():
    screen.fill((21, 21, 21))

    # Drawing circles with labels (increased resolution)
    pygame.draw.circle(screen, (197, 255, 248), (195, 195), 76)  # First circle
    pygame.draw.circle(screen, (255, 165, 165), (445, 195), 76)  # Second circle
    pygame.draw.circle(screen, (206, 255, 125), (675, 195), 76)  # Third circle
    pygame.draw.circle(screen, (179, 196, 255), (145, 445), 76)  # Fourth circle
    pygame.draw.circle(screen, (255, 186, 148), (375, 445), 76)  # Fifth circle
    pygame.draw.circle(screen, (244, 244, 116), (605, 445), 76)  # Sixth circle

    # Font for labels
    myfont = pygame.font.Font("Inter.ttf", 30)

    # Labels
    label1 = myfont.render("brake", True, (0, 0, 0))  # First circle
    label1_rect = label1.get_rect(center=(195, 195))
    screen.blit(label1, label1_rect)

    label2 = myfont.render("cameras", True, (0, 0, 0))  # Second circle
    label2_rect = label2.get_rect(center=(445, 195))
    screen.blit(label2, label2_rect)

    label3 = myfont.render("motor", True, (0, 0, 0))  # Third circle
    label3_rect = label3.get_rect(center=(675, 195))
    screen.blit(label3, label3_rect)

    label4 = myfont.render("battery", True, (0, 0, 0))  # Fourth circle
    label4_rect = label4.get_rect(center=(145, 445))
    screen.blit(label4, label4_rect)

    label5 = myfont.render("controller", True, (0, 0, 0))  # Fifth circle
    label5_rect = label5.get_rect(center=(375, 445))
    screen.blit(label5, label5_rect)

    label6 = myfont.render("charger", True, (0, 0, 0))  # Sixth circle
    label6_rect = label6.get_rect(center=(605, 445))
    screen.blit(label6, label6_rect)

    # Title
    title_font = pygame.font.Font("FrancoisOne-Regular.ttf", 45)
    title = title_font.render("Part List", True, (255, 255, 255))
    screen.blit(title, (320, 20))

    # "back" button
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)

    pygame.display.flip()

def track1():
    global drive_car, drive_car_rect
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0,0,0), [1, 152, 0,0], 75)
    track1 = pygame.image.load("track1.png")
    track1 = track1.convert()
    screen.blit(track1, (0, 0))
    screen.blit(drive_car, drive_car_rect)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)

    # dis allowed track sections
    bound1 = pygame.draw.rect(screen, (0,0,0), [0,0,800,176], 0)
    bound2 = pygame.draw.rect(screen, (0,0,0), [339,120,476,120], 0)
    bound3 = pygame.draw.rect(screen, (0,0,0), [340,0,122,420], 0)
    bound4 = pygame.draw.rect(screen, (0,0,0), [0,515,800,100], 0)
    bound5 = pygame.draw.rect(screen, (0,0,0), [0,280,203,350], 0)
    bound6 = pygame.draw.rect(screen, (0,0,0), [587,370,250,350], 0)

    pygame.display.flip()

def track2():
    global drive_car, drive_car_rect
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0,0,0), [1, 152, 0,0], 75)
    track1 = pygame.image.load("track2.png")
    track1 = track1.convert()
    screen.blit(track1, (0, 0))
    screen.blit(drive_car, drive_car_rect)
    
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)

    # dis allowed track sections
    bound1 = pygame.draw.rect(screen, (0,0,0), [0,0,800,84], 0)
    bound2 = pygame.draw.rect(screen, (0,0,0), [0,0,126,176], 0)
    bound3 = pygame.draw.rect(screen, (0,0,0), [461,0,500,209], 0)
    bound4 = pygame.draw.rect(screen, (0,0,0), [461,0,24,407], 0)
    bound5 = pygame.draw.rect(screen, (0,0,0), [0,283,332,18], 0)
    bound6 = pygame.draw.rect(screen, (0,0,0), [236,193,96,95], 0)
    bound7 = pygame.draw.rect(screen, (0,0,0), [0,283,102,318], 0)
    bound8 = pygame.draw.rect(screen, (0,0,0), [0,506,800,170], 0)
    bound9 = pygame.draw.rect(screen, (0,0,0), [607,344,800,400], 0)

    pygame.display.flip()

def track3():
    global drive_car, drive_car_rect
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0,0,0), [1, 152, 0,0], 75)
    track1 = pygame.image.load("track3.png")
    track1 = track1.convert()
    screen.blit(track1, (0, 0))
    screen.blit(drive_car, drive_car_rect)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)

    # dis allowed track sections
    bound1 = pygame.draw.rect(screen, (0,0,0), [0,0,800,107], 0)
    bound2 = pygame.draw.rect(screen, (0,0,0), [250,106,349,109], 0)
    bound3 = pygame.draw.rect(screen, (0,0,0), [250,106,211,275], 0)
    bound4 = pygame.draw.rect(screen, (0,0,0), [0,280,105,300], 0)
    bound5 = pygame.draw.rect(screen, (0,0,0), [587,344,400,300], 0)
    bound6 = pygame.draw.rect(screen, (0,0,0), [723,230,400,300], 0)
    bound7 = pygame.draw.rect(screen, (0,0,0), [0,492,800,200], 0)
    bound8 = pygame.draw.rect(screen, (0,0,0), [0,0,300,176], 0)

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
            print(x,y)
            #welcome screen
            if x > 675 and x < 750 and y > 25 and y < 75:  # Adjusted coordinates for "back" button
                page -= 1 # back button
                drive_car_rect.x = 20
                drive_car_rect.y = 210

            elif page == 2 and x > 50 and x < 300 and y > 350 and y < 450: 
                page = 3 # start button
            elif page == 2 and x > 350 and x < 770 and y > 350 and y < 450:
                print('instruct')

            # roadmap screen
            elif page == 3 and x > 100 and x < 300 and y > 120 and y < 270: # brake 
                page=4
            elif page == 3 and x > 368 and x < 522 and y > 120 and y < 270: # cameras 
                page=5
            elif page == 3 and x > 600 and x < 748 and y > 120 and y < 270: # motor 
                page=6
            elif page == 3 and x > 70 and x < 220 and y > 370 and y < 519: # battery
                page=5
            elif page == 3 and x > 300 and x < 451 and y > 370 and y < 519: # controller
                page=6
            elif page == 3 and x > 530 and x < 680 and y > 370 and y < 519: # battery
                page=4

    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()
    # also i know we didn't learn this but i just found out about it and its helpful to allow for holding down controls
    # holding down the arrow keys is particularly helpful in a racing game. (helps with user experience)
    # holding down arrow keys is a lot more fun than having to click every time

    # Move the car based on the arrow keys
    if keys[pygame.K_UP]:
        drive_car_rect.y -= 2.5  #speed of the car
    if keys[pygame.K_DOWN]:
        drive_car_rect.y += 2.5
    if keys[pygame.K_LEFT]:
        drive_car_rect.x -= 2.5
    if keys[pygame.K_RIGHT]:
        drive_car_rect.x += 2.5

    screen.blit(drive_car, drive_car_rect)  # Draw the car on the screen

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
    elif page == 5:
        track2()
    elif page == 6:
        track3()

    pygame.display.flip()
