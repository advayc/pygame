import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("EV REPAIR")

clock = pygame.time.Clock()

instruction_sound = pygame.mixer.Sound("narration.mp3")
font = pygame.font.Font(None, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

def draw_text(text, position, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Instruction Audio
audio_playing = False
def lesson1():
    screen.fill((205,205,205))
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 65)
    text = my_font.render('What are Self-Driving Cars?', True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 40))
    screen.blit(text, text_rect)
    
    a_font = pygame.font.SysFont('Georgia', 16)
    
    b_font = pygame.font.SysFont('Georgia', 20)
    text2 = b_font.render('NEXT', True, (0, 0, 0))
    text2_rect = text.get_rect(center=(750, 600))
    screen.blit(text2, text2_rect)
    # text
    # Read the content from instructions.txt
    content = open("lesson1.txt", "r")
    instructions_lines = content.readlines()
    
    # Render the instructions text
    for i, line in enumerate(instructions_lines):
        line = line.strip()  # Remove newline characters
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()  # Close the file
    
def lesson2():
    screen.fill((205,205,205))
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 65)
    text = my_font.render('Instructions Page', True, (0, 0, 0))
    text_rect = text.get_rect(center=(300, 40))
    screen.blit(text, text_rect)
    
    diff_font = pygame.font.Font('FrancoisOne-Regular.ttf', 20)
    text2 = diff_font.render('Audio!!', True, (0, 0, 0))
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
    content = open("lesson2.txt", "r")
    instructions_lines = content.readlines()
    
    # Render the instructions text
    for i, line in enumerate(instructions_lines):
        line = line.strip()  # Remove newline characters
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()  # Close the file
'''    
def lesson1():
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
'''
while True:
    clock.tick(60)
    lesson1()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            print(x,y)
            if x > 650 and x < 810 and y > 10 and y < 90:
                    if not audio_playing:  # If audio is not already playing
                        instruction_sound.play()
                        audio_playing = True  # Set the flag to True when audio starts playing
                        
    screen.fill(BLACK)

    draw_text("Lesson1", (100, 50))
    draw_text("Lesson2", (100, 125))
    draw_text("Lesson3", (100, 200))
    draw_text("Lesson4", (100, 275))
    draw_text("Lesson5", (100, 350))
    draw_text("Lesson6", (100, 425))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x,y)
            if 50 <= x <= 750:
                if 25 <= y <= 75:
                    lesson1()
                elif 100 <= y <= 150:
                    lesson2()

    
    pygame.display.flip()
