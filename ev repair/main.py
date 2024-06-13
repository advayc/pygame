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
car_speed = 15

dc = pygame.image.load('car.png').convert_alpha()
drive_car_rect = dc.get_rect()
drive_car = pygame.transform.scale(dc, (71, 39)) # Scale the image to 50x50
drive_car_rect.x = 20
drive_car_rect.y = 210
clock = pygame.time.Clock()

# Load Sounds
bg_sound = pygame.mixer.Sound("sound.mp3")
crash = pygame.mixer.Sound("crash.mp3")
instruction_sound = pygame.mixer.Sound("narration.mp3")

# Text setup
my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 40)
text = my_font.render('Loading...', True, (0, 0, 0))
text_rect = text.get_rect(center=(675, 575))
text_alpha = 255  # Initial alpha value

# Background Sound
bg_sound.play(-1)  # Play the background sound in a loop

crash_sound_played = False
transition_complete = False

# Instruction Audio
audio_playing = False

def draw_back_button():
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)

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

    draw_back_button()

    # Render the text
    screen.blit(text, text_rect)
    pygame.display.flip()

def instructions():
    global page

    screen.fill((205,205,205))
    instruct_bg = pygame.image.load("instruct_bg.jpg")
    instruct = pygame.transform.scale(instruct_bg, (800, 600))
    instruct.set_alpha(15)
    screen.blit(instruct, (0,0))
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 65)
    text = my_font.render('Instructions Page', True, (0, 0, 0))
    text_rect = text.get_rect(center=(300, 40))
    screen.blit(text, text_rect)
    
    diff_font = pygame.font.Font('FrancoisOne-Regular.ttf', 20)
    text2 = diff_font.render('Read the Story FIRST!', True, (0, 0, 0))
    text_rect2 = text2.get_rect(center=(700, 100))
    screen.blit(text2, text_rect2)
    # images
    speaker = pygame.image.load("speaker.png")
    speaker = pygame.transform.scale(speaker, (80, 80))
    speaker_rect = speaker.get_rect(center=(710, 40))
    screen.blit(speaker, speaker_rect)
    a_font = pygame.font.SysFont('Georgia', 20)
    # text
    # Read the content from instructions.txt
    content = open("instructions.txt", "r")
    instructions_lines = content.readlines()
    
    # Render the instructions text
    for i, line in enumerate(instructions_lines):
        line = line.strip()  # Remove newline characters
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()  # Close the file
    
    # "back" button
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 40)
    lab = f.render('BACK', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 525))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('BACK', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
            
    pygame.draw.circle(screen, (90, 90, 90), (700, 525), 50)  # First circle
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

    draw_back_button()
    pygame.display.flip()
    
def track1():
    global drive_car_rect
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Load and blit the background image
    track1back = pygame.image.load("track1back.png").convert()
    screen.blit(track1back, (0, 0))

    # Load and blit the overlay image
    track1face = pygame.image.load("track1face.png").convert()
    screen.blit(track1face, (0, 175))

    # Define event points
    info_ev_center = (268, 459)
    quiz_ev_center = (604, 301)
    
    # Draw event points as circles
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)

    # Load font and render text
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev_center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev_center))

    # Blit the car image
    screen.blit(drive_car, drive_car_rect)

    # Draw the back button (function not provided, ensure it's defined elsewhere)
    draw_back_button()

    # Check for collisions with event points
    # Check if the car is within the range of the event points
    if abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and abs(drive_car_rect[1] - info_ev_center[1]) <= 50:
        print('info')
    if abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50:
        print('quiz')

    # Update the display
    pygame.display.flip()

def track2():
    global drive_car_rect

    screen.fill((0, 0, 0))
    # Load and blit the background image
    track2back = pygame.image.load("track2back.png").convert()
    screen.blit(track2back, (0, 0))
    # Load and blit the overlay image
    track2face = pygame.image.load("track2face.png").convert_alpha()
    screen.blit(track2face, (0, 85))
    
    # Define event points
    info_ev_center = (389, 264)
    quiz_ev_center = (544, 276)
    
    # Draw event points as circles
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev.center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev.center))

    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    # Check for collisions
    if (abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and
        abs(drive_car_rect[1] - info_ev_center[1]) <= 50):
        print("info")
    elif (abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and
          abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50):
        print("quiz")

    pygame.display.flip()


def track3():
    global drive_car_rect

    screen.fill((0, 0, 0))
    # Load and blit the background image
    track3back = pygame.image.load("track3back.png").convert()
    screen.blit(track3back, (0, 0))
    # Load and blit the overlay image
    track3face = pygame.image.load("track3face.png").convert_alpha()
    screen.blit(track3face, (0, 100))

    # Define event points
    info_ev_center = (173, 427)
    quiz_ev_center = (544, 276)
    
    # Draw event points as circles
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev.center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev.center))

    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    # Check for collisions
    if (abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and
        abs(drive_car_rect[1] - info_ev_center[1]) <= 50):
        print("info")
    elif (abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and
          abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50):
        print("quiz")

    pygame.display.flip()

# im sorry ms quan colliderect and collidepoint are not working because rects include their inital positions with collisions
# this means it wont work properly when checking for these collisions

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

            if page == 7 or page == 6 or page == 5:
                if 675 < x < 750 and 25 < y < 75:
                    page = 4  # Go back to roadmap
                    drive_car_rect.x = 20
                    drive_car_rect.y = 210

            elif page == 3 and 675 < x < 750 and 525 < y < 580:
                page = 2  # Go back to welcome screen

            # Welcome screen buttons
            elif page == 2:
                if 50 < x < 300 and 350 < y < 450:
                    page = 4  # Start button
                elif 350 < x < 770 and 350 < y < 450:
                    page = 3  # Instructions button

            # Roadmap screen buttons
            elif page == 4:
                if 675 < x < 750 and 25 < y < 75:
                    page = 2 # welcome page
                elif 100 < x < 300 and 120 < y < 270:
                    page = 5  # Brake
                elif 368 < x < 522 and 120 < y < 270:
                    page = 6  # Cameras
                elif 600 < x < 748 and 120 < y < 270:
                    page = 7  # Motor
                elif 70 < x < 220 and 370 < y < 519:
                    page = 6  # Battery
                elif 300 < x < 451 and 370 < y < 519:
                    page = 7  # Controller
                elif 530 < x < 680 and 370 < y < 519:
                    page = 5  # Charger

            # Instruction screen
            elif page == 3 and 650 < x < 810 and 10 < y < 90:
                if not audio_playing:
                    instruction_sound.play()
                    audio_playing = True

    # Arrow key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        drive_car_rect.y -= 2.5
    if keys[pygame.K_DOWN]:
        drive_car_rect.y += 2.5
    if keys[pygame.K_LEFT]:
        drive_car_rect.x -= 2.5
    if keys[pygame.K_RIGHT]:
        drive_car_rect.x += 2.5

    screen.blit(drive_car, drive_car_rect)

    # Page rendering based on current page value
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
        instructions()
    elif page == 4:
        roadmap()
    elif page == 5:
        track1()
    elif page == 6:
        track2()
    elif page == 7:
        track3()

    pygame.display.flip()