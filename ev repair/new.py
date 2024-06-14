import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("EV REPAIR")

clock = pygame.time.Clock()

lesson2_sound = pygame.mixer.Sound("lesson2.mp3")
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
    text = my_font.render('How Do Self-Driving Cars Work?', True, (0, 0, 0))
    text_rect = text.get_rect(center=(300, 40))
    screen.blit(text, text_rect)
    
    diff_font = pygame.font.Font('FrancoisOne-Regular.ttf', 20)
    text2 = diff_font.render('Audio!!', True, (0, 0, 0))
    text_rect2 = text2.get_rect(center=(700, 590))
    screen.blit(text2, text_rect2)
    # images
    speaker = pygame.image.load("speaker.png")
    speaker = pygame.transform.scale(speaker, (80, 80))
    speaker_rect = speaker.get_rect(center=(710, 540))
    screen.blit(speaker, speaker_rect)
    a_font = pygame.font.SysFont('Georgia', 14)
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
    
def lesson3():
    screen.fill((205,205,205))
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 65)
    text = my_font.render('Ethics of Self-Driving Cars', True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 40))
    screen.blit(text, text_rect)
    
    a_font = pygame.font.SysFont('Georgia', 16)
    
    b_font = pygame.font.SysFont('Georgia', 20)
    text2 = b_font.render('NEXT', True, (0, 0, 0))
    text2_rect = text.get_rect(center=(750, 600))
    screen.blit(text2, text2_rect)
    # text
    # Read the content from instructions.txt
    content = open("lesson3.txt", "r")
    instructions_lines = content.readlines()
    
    # Render the instructions text
    for i, line in enumerate(instructions_lines):
        line = line.strip()  # Remove newline characters
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()  # Close the file
    
def lesson4():
    screen.fill((205,205,205))
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 65)
    text = my_font.render('The Future', True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 40))
    screen.blit(text, text_rect)
    
    a_font = pygame.font.SysFont('Georgia', 16)
    
    b_font = pygame.font.SysFont('Georgia', 20)
    text2 = b_font.render('NEXT', True, (0, 0, 0))
    text2_rect = text.get_rect(center=(750, 600))
    screen.blit(text2, text2_rect)
    # text
    # Read the content from instructions.txt
    content = open("lesson4.txt", "r")
    instructions_lines = content.readlines()
    
    # Render the instructions text
    for i, line in enumerate(instructions_lines):
        line = line.strip()  # Remove newline characters
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()  # Close the file

def lesson5():
    screen.fill((205,205,205))
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 65)
    text = my_font.render('Safety of Self-Driving Cars', True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 40))
    screen.blit(text, text_rect)
    
    a_font = pygame.font.SysFont('Georgia', 16)
    
    b_font = pygame.font.SysFont('Georgia', 20)
    text2 = b_font.render('NEXT', True, (0, 0, 0))
    text2_rect = text.get_rect(center=(750, 600))
    screen.blit(text2, text2_rect)
    # text
    # Read the content from instructions.txt
    content = open("lesson5.txt", "r")
    instructions_lines = content.readlines()
    
    # Render the instructions text
    for i, line in enumerate(instructions_lines):
        line = line.strip()  # Remove newline characters
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()  # Close the file
    
def lesson6():
    screen.fill((205,205,205))
    my_font = pygame.font.Font('FrancoisOne-Regular.ttf', 65)
    text = my_font.render('Safety of Self-Driving Cars', True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 40))
    screen.blit(text, text_rect)
    
    a_font = pygame.font.SysFont('Georgia', 16)
    
    b_font = pygame.font.SysFont('Georgia', 20)
    text2 = b_font.render('NEXT', True, (0, 0, 0))
    text2_rect = text.get_rect(center=(750, 600))
    screen.blit(text2, text2_rect)
    # text
    # Read the content from instructions.txt
    content = open("lesson6.txt", "r")
    instructions_lines = content.readlines()
    
    # Render the instructions text
    for i, line in enumerate(instructions_lines):
        line = line.strip()  # Remove newline characters
        line_text = a_font.render(line, True, (0, 0, 0))
        line_rect = line_text.get_rect(topleft=(20, 100 + i * 50))
        screen.blit(line_text, line_rect)
    content.close()  # Close the file
    
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                        
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
                elif 175 <= y <= 225:
                    lesson3()
                elif 250 <= y <= 300:
                    lesson4()
                elif 325 <= y <= 375:
                    lesson5()
                elif 400 <= y <= 450:
                    lesson6()
            if x > 650 and x < 810 and y > 500 and y < 580:
                if not audio_playing:  # If audio is not already playing
                    lesson2_sound.play()
                    audio_playing = True  # Set the flag to True when audio starts playing

    
    pygame.display.flip()

