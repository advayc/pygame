import pygame, sys, time
from pygame.locals import QUIT

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("EV REPAIR")
page = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
font = pygame.font.Font('Inter.ttf', 32)

# Load images
car = pygame.image.load("car3.png")
car_image = pygame.transform.scale(car, (130, 100))
car_rect = car_image.get_rect()
car_rect.x = 20
car_rect.y = 480
car_speed = 15

dc = pygame.image.load('car.png').convert_alpha()
drive_car_rect = dc.get_rect()
drive_car = pygame.transform.scale(dc, (71, 39))
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
text_alpha = 255

# Background Sound
bg_sound.play(-1)

crash_sound_played = False
transition_complete = False

# Instruction Audio
audio_playing = False

quiz_completed_count = 0  # Initialize the quiz completion counter

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

    car_rect.x += car_speed

    if car_rect.right >= 780:
        car_speed = 0
        if text_alpha > 0:
            text_alpha -= 8
        else:
            text_alpha = 0
            transition_complete = True
        if not crash_sound_played:
            crash.play()
            crash_sound_played = True
            bg_sound.stop()

    text.set_alpha(text_alpha)
    loading_bg = pygame.image.load("orange.png")
    bg_scale = pygame.transform.scale(loading_bg, (850, 650))
    rect_surface = pygame.Surface((725, 50), pygame.SRCALPHA)
    rect_surface.fill((0, 0, 0, 128))
    screen.blit(bg_scale, (-6, 0))
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

    for x in range(-3, 4):
        for y in range(-3, 4):
            outline = my_font.render('EV REPAIR', True, (0, 0, 0))
            screen.blit(outline, (text_rect.x + x, text_rect.y + y))
    
    checker_bg = pygame.image.load("checker.png")
    checker = pygame.transform.scale(checker_bg, (800, 600))
    checker.set_alpha(25)
    screen.blit(checker, (0,0))
    pygame.draw.rect(screen, (0, 0, 0), [50, 350, 250, 100], 250)
    my_font2 = pygame.font.Font('FrancoisOne-Regular.ttf', 70)
    text2 = my_font2.render('Start', True, (255, 255, 255))
    text2_rect = text2.get_rect(center=(175, 400))
    screen.blit(text2, text2_rect)

    pygame.draw.rect(screen, (0, 0, 0), [350, 350, 400, 100], 0)
    text3 = my_font2.render('Instructions', True, (255, 255, 255))
    text3_rect = text3.get_rect(center=(550, 400))
    screen.blit(text3, text3_rect)

    draw_back_button()

    screen.blit(text, text_rect)
    pygame.display.flip()

def instructions():
    global page

    screen.fill((205, 205, 205))
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
    speaker = pygame.image.load("speaker.png")
    speaker = pygame.transform.scale(speaker, (80, 80))
    speaker_rect = speaker.get_rect(center=(710, 40))
    screen.blit(speaker, speaker_rect)
    a_font = pygame.font.SysFont('Georgia', 20)
    content = open("instructions.txt", "r")
    instructions_lines = content.readlines()
    
    for i, line in enumerate(instructions_lines):
        line = line.strip()
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()
    
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 40)
    lab = f.render('BACK', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 525))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('BACK', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
            
    pygame.draw.circle(screen, (90, 90, 90), (700, 525), 50)
    screen.blit(lab, lab_rect)

    pygame.display.flip()

def roadmap():
    screen.fill((21, 21, 21))

    pygame.draw.circle(screen, (197, 255, 248), (195, 195), 76)
    pygame.draw.circle(screen, (255, 165, 165), (445, 195), 76)
    pygame.draw.circle(screen, (206, 255, 125), (675, 195), 76)
    pygame.draw.circle(screen, (179, 196, 255), (145, 445), 76)
    pygame.draw.circle(screen, (255, 186, 148), (375, 445), 76)
    pygame.draw.circle(screen, (244, 244, 116), (605, 445), 76)

    myfont = pygame.font.Font("Inter.ttf", 30)

    label1 = myfont.render("brake", True, (0, 0, 0))
    label1_rect = label1.get_rect(center=(195, 195))
    screen.blit(label1, label1_rect)

    label2 = myfont.render("cameras", True, (0, 0, 0))
    label2_rect = label2.get_rect(center=(445, 195))
    screen.blit(label2, label2_rect)

    label3 = myfont.render("motor", True, (0, 0, 0))
    label3_rect = label3.get_rect(center=(675, 195))
    screen.blit(label3, label3_rect)

    label4 = myfont.render("battery", True, (0, 0, 0))
    label4_rect = label4.get_rect(center=(145, 445))
    screen.blit(label4, label4_rect)

    label5 = myfont.render("controller", True, (0, 0, 0))
    label5_rect = label5.get_rect(center=(375, 445))
    screen.blit(label5, label5_rect)

    label6 = myfont.render("charger", True, (0, 0, 0))
    label6_rect = label6.get_rect(center=(605, 445))
    screen.blit(label6, label6_rect)

    title_font = pygame.font.Font("FrancoisOne-Regular.ttf", 45)
    title = title_font.render("Part List", True, (255, 255, 255))
    screen.blit(title, (320, 20))

    draw_back_button()
    pygame.display.flip()
    
def track1():
    global drive_car_rect, page
    
    screen.fill((0, 0, 0))
    track1back = pygame.image.load("track1back.png").convert()
    screen.blit(track1back, (0, 0))
    track1face = pygame.image.load("track1face.png").convert_alpha()
    screen.blit(track1face, (0,175))
    info_ev_center = (268, 459)
    quiz_ev_center = (604, 301)
    
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev_center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev_center))
    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    if abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and abs(drive_car_rect[1] - info_ev_center[1]) <= 50:
        print('info')
    elif abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50:
        page = 11  # Go to quiz 1

    if (drive_car_rect.y < 170 or drive_car_rect.y > 512) or \
       (drive_car_rect.x > 339 and drive_car_rect.y < 238) or \
       (drive_car_rect.x > 339 and drive_car_rect.x < 461 and drive_car_rect.y < 419) or \
       (drive_car_rect.x < 204 and drive_car_rect.y > 281 or drive_car_rect.x > 586 and drive_car_rect.y > 370):
        drive_car_rect.x, drive_car_rect.y = 20, 210

    pygame.display.flip()

def track2():
    global drive_car_rect, page

    screen.fill((0, 0, 0))
    track2back = pygame.image.load("track2back.png").convert()
    screen.blit(track2back, (0, 0))
    track2face = pygame.image.load("track2face.png").convert_alpha()
    screen.blit(track2face, (0, 85))
    
    info_ev_center = (389, 264)
    quiz_ev_center = (544, 276)
    
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev.center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev.center))

    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    if abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and abs(drive_car_rect[1] - info_ev_center[1]) <= 50:
        print("info")
    elif abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50:
        page = 12  # Go to quiz 2

    if (drive_car_rect.y < 85 or drive_car_rect.y > 508) or (drive_car_rect.x < 122 and drive_car_rect.y < 170)\
    or (drive_car_rect.x > 460 and drive_car_rect.y < 210) or (drive_car_rect.x < 330 and drive_car_rect.y > 285 and drive_car_rect.y < 302)\
    or (drive_car_rect.x > 234 and drive_car_rect.x < 328 and drive_car_rect.y > 197 and drive_car_rect.y < 296)\
    or (drive_car_rect.x > 609 and drive_car_rect.y > 346):
        drive_car_rect.x, drive_car_rect.y = 20, 210

    pygame.display.flip()

def track3():
    global drive_car_rect, page

    screen.fill((0, 0, 0))
    track3back = pygame.image.load("track3back.png").convert()
    screen.blit(track3back, (0, 0))
    track3face = pygame.image.load("track3face.png").convert_alpha()
    screen.blit(track3face, (0, 100))

    info_ev_center = (173, 427)
    quiz_ev_center = (544, 276)
    
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev.center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev.center))

    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    if abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and abs(drive_car_rect[1] - info_ev_center[1]) <= 50:
        print("info")
    elif abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50:
        page = 13  # Go to quiz 3

    if (drive_car_rect.x < 598 and drive_car_rect.y < 174) or (drive_car_rect.x < 103 and drive_car_rect.y > 283)\
    or (drive_car_rect.y > 491) or (drive_car_rect.y < 99) or (drive_car_rect.x > 250 and drive_car_rect.x < 460 and drive_car_rect.y < 377)\
    or (drive_car_rect.x > 250 and drive_car_rect.x <598 and drive_car_rect.y < 210) or (drive_car_rect.x > 588 and drive_car_rect.y > 344)\
    or (drive_car_rect.x > 720 and drive_car_rect.y > 231):
        drive_car_rect.x, drive_car_rect.y = 20, 210

    pygame.display.flip()

def track22():
    global drive_car_rect, page

    screen.fill((0, 0, 0))
    track2back = pygame.image.load("track2back.png").convert()
    screen.blit(track2back, (0, 0))
    track2face = pygame.image.load("track2face.png").convert_alpha()
    screen.blit(track2face, (0, 85))
    
    info_ev_center = (389, 264)
    quiz_ev_center = (544, 276)
    
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev.center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev.center))

    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    if abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and abs(drive_car_rect[1] - info_ev_center[1]) <= 50:
        print("info")
    elif abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50:
        page = 14  # Go to quiz 4

    if (drive_car_rect.y < 85 or drive_car_rect.y > 508) or (drive_car_rect.x < 122 and drive_car_rect.y < 170)\
    or (drive_car_rect.x > 460 and drive_car_rect.y < 210) or (drive_car_rect.x < 330 and drive_car_rect.y > 285 and drive_car_rect.y < 302)\
    or (drive_car_rect.x > 234 and drive_car_rect.x < 328 and drive_car_rect.y > 197 and drive_car_rect.y < 296)\
    or (drive_car_rect.x > 609 and drive_car_rect.y > 346):
        drive_car_rect.x, drive_car_rect.y = 20, 210

    pygame.display.flip()

def track33():
    global drive_car_rect, page

    screen.fill((0, 0, 0))
    track3back = pygame.image.load("track3back.png").convert()
    screen.blit(track3back, (0, 0))
    track3face = pygame.image.load("track3face.png").convert_alpha()
    screen.blit(track3face, (0, 100))

    info_ev_center = (173, 427)
    quiz_ev_center = (544, 276)
    
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)

    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev.center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev.center))

    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    if abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and abs(drive_car_rect[1] - info_ev_center[1]) <= 50:
        print("info")
    elif abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50:
        page = 15  # Go to quiz 5

    if (drive_car_rect.x < 598 and drive_car_rect.y < 174) or (drive_car_rect.x < 103 and drive_car_rect.y > 283)\
    or (drive_car_rect.y > 491) or (drive_car_rect.y < 99) or (drive_car_rect.x > 250 and drive_car_rect.x < 460 and drive_car_rect.y < 377)\
    or (drive_car_rect.x > 250 and drive_car_rect.x <598 and drive_car_rect.y < 210) or (drive_car_rect.x > 588 and drive_car_rect.y > 344)\
    or (drive_car_rect.x > 720 and drive_car_rect.y > 231):
        drive_car_rect.x, drive_car_rect.y = 20, 210

    pygame.display.flip()

def track11():
    global drive_car_rect, page
    
    screen.fill((0, 0, 0))
    track1back = pygame.image.load("track1back.png").convert()
    screen.blit(track1back, (0, 0))
    track1face = pygame.image.load("track1face.png").convert_alpha()
    screen.blit(track1face, (0,175))
    info_ev_center = (268, 459)
    quiz_ev_center = (604, 301)
    
    info_ev = pygame.draw.circle(screen, (0, 0, 0), info_ev_center, 25)
    quiz_ev = pygame.draw.circle(screen, (0, 0, 0), quiz_ev_center, 25)
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 30)
    ev_text = f.render('EV', True, (255, 255, 255))
    screen.blit(ev_text, ev_text.get_rect(center=info_ev_center))
    screen.blit(ev_text, ev_text.get_rect(center=quiz_ev_center))
    screen.blit(drive_car, drive_car_rect)
    draw_back_button()

    if abs(drive_car_rect[0] - info_ev_center[0]) <= 50 and abs(drive_car_rect[1] - info_ev_center[1]) <= 50:
        print('info')
    elif abs(drive_car_rect[0] - quiz_ev_center[0]) <= 50 and abs(drive_car_rect[1] - quiz_ev_center[1]) <= 50:
        page = 16  # Go to quiz 6

    if (drive_car_rect.y < 170 or drive_car_rect.y > 512) or \
       (drive_car_rect.x > 339 and drive_car_rect.y < 238) or \
       (drive_car_rect.x > 339 and drive_car_rect.x < 461 and drive_car_rect.y < 419) or \
       (drive_car_rect.x < 204 and drive_car_rect.y > 281 or drive_car_rect.x > 586 and drive_car_rect.y > 370):
        drive_car_rect.x, drive_car_rect.y = 20, 210

    pygame.display.flip()

def true_false_quiz():
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("True or False Game")

    # Load font
    font = pygame.font.SysFont(None, 32)

    # Questions and answers
    questions = [
        "Self-driving cars use cameras to be able to see everything.",
        "Self-driving cars do not use GPS for navigation.",
        "Self-driving cars use radar to detect objects."
    ]
    answers = [True, False, True]  # True = 'True', False = 'False'

    # Variables
    current_question = 0
    feedback = ""

    # Main loop
    while True:
        screen.fill((0, 0, 0))

        # Display question
        question_text = font.render(questions[current_question], True, (255, 255, 255))
        screen.blit(question_text, (50, 50))

        # Display feedback
        feedback_text = font.render(feedback, True, (255, 255, 255))
        screen.blit(feedback_text, (50, 150))

        # Display True/False buttons
        pygame.draw.rect(screen, (255, 255, 255), (50, 200, 100, 50), 2)
        true_text = font.render("True", True, (255, 255, 255))
        screen.blit(true_text, (75, 215))

        pygame.draw.rect(screen, (255, 255, 255), (200, 200, 100, 50), 2)
        false_text = font.render("False", True, (255, 255, 255))
        screen.blit(false_text, (225, 215))

        # Next question button
        pygame.draw.rect(screen, (255, 255, 255), (650, 500, 100, 50), 2)
        next_text = font.render("Next", True, (255, 255, 255))
        screen.blit(next_text, (675, 515))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 150 and 200 <= y <= 250:  # True button
                    if answers[current_question] == True:
                        feedback = "Correct!"
                    else:
                        feedback = "Wrong!"
                elif 200 <= x <= 300 and 200 <= y <= 250:  # False button
                    if answers[current_question] == False:
                        feedback = "Correct!"
                    else:
                        feedback = "Wrong!"
                elif 650 <= x <= 750 and 500 <= y <= 550:  # Next button
                    current_question += 1
                    if current_question >= len(questions):
                        current_question = 0
                    feedback = ""
        draw_back_button()
        pygame.display.flip()

def draw_text(text, position, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def multiple_choice_quiz():
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Multiple Choice Game")

    # Questions and answers
    questions = [
        ("What is one of the biggest ethical concerns about self-driving cars?",
         ["A. Decision making in moments of accidents",
          "B. The speed of the car",
          "C. The color of the car"],
         0),  # Index of the correct answer in the answers list
        ("Who might be liable in an accident involving a self-driving car?",
         ["A. The car owner",
          "B. The car manufacturer",
          "C. The pedestrian"],
         1)   # Index of the correct answer in the answers list
    ]

    # Variables
    current_question = 0
    result_text = ""

    def display_question(question_data):
        screen.fill(BLACK)
        question_text, answers, correct_index = question_data

        draw_text(question_text, (50, 50))

        for idx, answer in enumerate(answers):
            draw_text(answer, (50, 150 + idx * 50))

        # Display the result text if available
        if result_text:
            draw_text(result_text, (50, 400), BLUE)

    def check_answer(question_data, answer_idx):
        _, _, correct_index = question_data
        return answer_idx == correct_index

    def display_end_screen():
        screen.fill(BLACK)
        draw_text("Quiz Completed!", (300, 250))
        pygame.draw.rect(screen, GREEN, (350, 350, 100, 50))
        draw_text("Next", (375, 365))

    # Main loop
    running = True
    quiz_completed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if not quiz_completed:
                    if 50 <= x <= 750:
                        for idx in range(len(questions[current_question][1])):
                            if 150 + idx * 50 <= y <= 150 + (idx + 1) * 50:
                                if check_answer(questions[current_question], idx):
                                    result_text = "Correct!"
                                else:
                                    result_text = "Wrong answer."

                                current_question += 1
                                if current_question >= len(questions):
                                    quiz_completed = True
                                break
                else:
                    if 350 <= x <= 450 and 350 <= y <= 400:
                        screen.fill(BLACK)
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Wait for 2 seconds
                        running = False

        if not quiz_completed:
            if current_question < len(questions):
                display_question(questions[current_question])
        else:
            display_end_screen()
        draw_back_button()
        pygame.display.flip()

def fill_blanks_quiz():
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Fill in the Blanks")

    # Load font
    font = pygame.font.SysFont(None, 22)

    # Define the sentences and their answers
    questions = [
        "Advanced sensors and artificial intelligence enable _____________ cars to navigate roads independently.",
        "Many self-driving cars are _____________ to align with sustainability goals.",
        "Continuous evolution of ______________ is necessary for the advancement of self-driving technology."
    ]
    answers = ["self-driving", "electric", "regulation"]

    # Load check and cross images (replace with actual images)
    check_img = pygame.Surface((30, 30))  # Placeholder for check image
    check_img.fill(GREEN)
    wrong_img = pygame.Surface((30, 30))  # Placeholder for wrong image
    wrong_img.fill(RED)

    # Game variables
    current_question = 0
    input_text = ""
    feedback_image = None
    submit_clicked = False

    # Main loop
    while True:
        screen.fill((0, 0, 0))

        # Display question
        text = font.render(questions[current_question], True, (255, 255, 255))
        screen.blit(text, (25, 50))

        # Display input box
        pygame.draw.rect(screen, (255, 255, 255), (50, 100, 600, 50), 2)
        input_surface = font.render(input_text, True, (255, 255, 255))
        screen.blit(input_surface, (55, 110))

        # Display feedback image
        if submit_clicked:
            if input_text.lower() == answers[current_question]:
                feedback_image = check_img
            else:
                feedback_image = wrong_img
            screen.blit(feedback_image, (680, 105))

        # Submit button
        pygame.draw.rect(screen, (255, 255, 255), (650, 500, 100, 50), 2)
        submit_text = font.render("Submit", True, (255, 255, 255))
        screen.blit(submit_text, (670, 510))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    submit_clicked = True
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if submit button is clicked
                if 650 <= event.pos[0] <= 750 and 500 <= event.pos[1] <= 550:
                    current_question += 1
                    if current_question >= len(questions):
                        print("Switching to a new page...")
                        time.sleep(2)  # Wait for 5 seconds before switching
                        return  # Exit the function to switch to the next quiz or end the program
                    input_text = ""  # Reset input text
                    feedback_image = None
                    submit_clicked = False
        draw_back_button()
        pygame.display.flip()

def choose_correct_option_quiz():
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Choose the Correct Option Quiz")

    # Questions and answers
    questions = [
        ("What is one of the main challenges of implementing AI in self-driving cars?",
         ["A. High computational power",
          "B. Limited sensors",
          "C. Inability to learn from data"],
         0),  # Index of the correct answer in the answers list
        ("Which sensor is essential for detecting pedestrians in self-driving cars?",
         ["A. Lidar",
          "B. Radar",
          "C. Ultrasonic sensors"],
         2),  # Index of the correct answer in the answers list
        ("What type of technology enables self-driving cars to navigate without human intervention?",
         ["A. Blockchain",
          "B. Artificial Intelligence",
          "C. Virtual Reality"],
         1)   # Index of the correct answer in the answers list
    ]

    # Variables
    current_question = 0
    result_text = ""

    def display_question(question_data):
        screen.fill(BLACK)
        question_text, options, correct_index = question_data

        draw_text(question_text, (50, 50))

        for idx, option in enumerate(options):
            draw_text(option, (50, 150 + idx * 50))

        # Display the result text if available
        if result_text:
            draw_text(result_text, (50, 400), BLUE)

    def check_answer(question_data, answer_idx):
        _, _, correct_index = question_data
        return answer_idx == correct_index

    def display_end_screen():
        screen.fill(BLACK)
        draw_text("Quiz Completed!", (300, 250))
        pygame.draw.rect(screen, GREEN, (350, 350, 100, 50))
        draw_text("Next", (375, 365))

    # Main loop
    running = True
    quiz_completed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if not quiz_completed:
                    if 50 <= x <= 750:
                        for idx in range(len(questions[current_question][1])):
                            if 150 + idx * 50 <= y <= 150 + (idx + 1) * 50:
                                if check_answer(questions[current_question], idx):
                                    result_text = "Correct!"
                                else:
                                    result_text = "Wrong answer."

                                current_question += 1
                                if current_question >= len(questions):
                                    quiz_completed = True
                                break
                else:
                    if 350 <= x <= 450 and 350 <= y <= 400:
                        screen.fill(BLACK)
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Wait for 2 seconds
                        running = False

        if not quiz_completed:
            if current_question < len(questions):
                display_question(questions[current_question])
        else:
            display_end_screen()

        draw_back_button()
        pygame.display.flip()

def multiple_choice_quiz_v2():
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Multiple Choice Game - Safety and Cost")

    # Questions and answers
    questions = [
        ("What is one of the key promises of self-driving cars?",
         ["A. Enhancing road safety",
          "B. Reducing fuel consumption",
          "C. Making cars cheaper"],
         0),  # Correct answer is A
        ("What is one major challenge for the safety of AVs?",
         ["A. Maintaining lane position",
          "B. Diverse weather and road conditions",
          "C. Communicating with passengers"],
         1),  # Correct answer is B
        ("Why is the cost of AVs a barrier to widespread adoption?",
         ["A. High price of sensors and computing components",
          "B. Lack of consumer interest",
          "C. High fuel costs"],
         0),  # Correct answer is A
        ("What potential convenience could AVs provide?",
         ["A. Increased fuel efficiency",
          "B. Increased productivity during commutes",
          "C. Reduced travel distances"],
         1),  # Correct answer is B
    ]

    # Variables
    current_question = 0
    result_text = ""

    def display_question(question_data):
        screen.fill(BLACK)
        question_text, answers, correct_index = question_data

        draw_text(question_text, (50, 50))

        for idx, answer in enumerate(answers):
            draw_text(answer, (50, 150 + idx * 50))

        # Display the result text if available
        if result_text:
            draw_text(result_text, (50, 400), BLUE)

    def check_answer(question_data, answer_idx):
        _, _, correct_index = question_data
        return answer_idx == correct_index

    def display_end_screen():
        screen.fill(BLACK)
        draw_text("Quiz Completed!", (300, 250))
        pygame.draw.rect(screen, GREEN, (350, 350, 100, 50))
        draw_text("Next", (375, 365))

    # Main loop
    running = True
    quiz_completed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if not quiz_completed:
                    if 50 <= x <= 750:
                        for idx in range(len(questions[current_question][1])):
                            if 150 + idx * 50 <= y <= 150 + (idx + 1) * 50:
                                if check_answer(questions[current_question], idx):
                                    result_text = "Correct!"
                                else:
                                    result_text = "Wrong answer."

                                current_question += 1
                                if current_question >= len(questions):
                                    quiz_completed = True
                                break
                else:
                    if 350 <= x <= 450 and 350 <= y <= 400:
                        screen.fill(BLACK)
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Wait for 2 seconds
                        running = False

        if not quiz_completed:
            if current_question < len(questions):
                display_question(questions[current_question])
        else:
            display_end_screen()
        draw_back_button()

        pygame.display.flip()

def true_false_quiz_v2():
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("True or False Game - Safety and Cost")

    # Load font
    font = pygame.font.SysFont(None, 32)

    # Questions and answers
    questions = [
        "Self-driving cars aim to eliminate human error in driving.",
        "Self-driving cars perform equally well in all weather conditions.",
        "The cost of AVs is not a barrier to their widespread adoption.",
        "Consumers are showing willingness to pay for advanced autonomous functions.",
        "AVs could allow passengers to use travel time for leisure or work."
    ]
    answers = [True, False, False, True, True]  # True = 'True', False = 'False'

    # Variables
    current_question = 0
    feedback = ""

    # Main loop
    while True:
        screen.fill((0, 0, 0))

        # Display question
        question_text = font.render(questions[current_question], True, (255, 255, 255))
        screen.blit(question_text, (50, 50))

        # Display feedback
        feedback_text = font.render(feedback, True, (255, 255, 255))
        screen.blit(feedback_text, (50, 150))

        # Display True/False buttons
        pygame.draw.rect(screen, (255, 255, 255), (50, 200, 100, 50), 2)
        true_text = font.render("True", True, (255, 255, 255))
        screen.blit(true_text, (75, 215))

        pygame.draw.rect(screen, (255, 255, 255), (200, 200, 100, 50), 2)
        false_text = font.render("False", True, (255, 255, 255))
        screen.blit(false_text, (225, 215))

        # Next question button
        pygame.draw.rect(screen, (255, 255, 255), (650, 500, 100, 50), 2)
        next_text = font.render("Next", True, (255, 255, 255))
        screen.blit(next_text, (675, 515))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 150 and 200 <= y <= 250:  # True button
                    if answers[current_question] == True:
                        feedback = "Correct!"
                    else:
                        feedback = "Wrong!"
                elif 200 <= x <= 300 and 200 <= y <= 250:  # False button
                    if answers[current_question] == False:
                        feedback = "Correct!"
                    else:
                        feedback = "Wrong!"
                elif 650 <= x <= 750 and 500 <= y <= 550:  # Next button
                    current_question += 1
                    if current_question >= len(questions):
                        current_question = 0
                    feedback = ""
        draw_back_button()
        pygame.display.flip()

def quiz_completed():
    global page, quiz_completed_count
    quiz_completed_count += 1
    page = 4  # Return to roadmap

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

            elif page == 2:
                if 50 < x < 300 and 350 < y < 450:
                    page = 4  # Start button
                elif 350 < x < 770 and 350 < y < 450:
                    page = 3  # Instructions button

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
                    page = 8  # Battery
                elif 300 < x < 451 and 370 < y < 519:
                    page = 9  # Controller
                elif 530 < x < 680 and 370 < y < 519:
                    page = 10  # Charger

            elif page == 3 and 650 < x < 810 and 10 < y < 90:
                if not audio_playing:
                    instruction_sound.play()
                    audio_playing = True

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
    elif page == 8:
        track22()
    elif page == 9:
        track33()
    elif page == 10:
        track11()
    elif page == 11:
        true_false_quiz()
    elif page == 12:
        multiple_choice_quiz()
    elif page == 13:
        fill_blanks_quiz()
    elif page == 14:
        choose_correct_option_quiz()
    elif page == 15:
        true_false_quiz_v2()
    elif page == 16:
        multiple_choice_quiz_v2()

    pygame.display.flip()
