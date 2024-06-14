import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Quiz Navigation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Font
font = pygame.font.Font(None, 32)

def draw_back_button():
    f = pygame.font.Font("FrancoisOne-Regular.ttf", 15)
    lab = f.render('back', True, (255, 255, 255))
    lab_rect = lab.get_rect(center=(700, 50))

    for x in range(-1, 2):
        for y in range(-1, 2):
            screen.blit(f.render('back', True, (0, 0, 0)), (lab_rect.x + x, lab_rect.y + y))
    screen.blit(lab, lab_rect)

# Define quiz functions
def true_false_quiz():
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

# Main loop for controlling quiz navigation
while True:
    screen.fill(BLACK)

    draw_text("True or False Quiz", (100, 50))
    draw_text("Multiple Choice Quiz", (100, 125))
    draw_text("Fill in the Blanks Quiz", (100, 200))
    draw_text("Choose the Correct Option Quiz", (100, 275))
    draw_text("True or False Quiz v2", (100, 350))
    draw_text("Multiple Choice Quiz v2", (100, 425))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x,y)
            if 50 <= x <= 750:
                if 25 <= y <= 75:
                    true_false_quiz()
                elif 100 <= y <= 150:
                    multiple_choice_quiz()
                elif 175 <= y <= 225:
                    fill_blanks_quiz()
                elif 250 <= y <= 300:
                    choose_correct_option_quiz()
                elif 325 <= y <= 375:
                    true_false_quiz_v2()
                elif 400 <= y <= 450:
                    multiple_choice_quiz_v2()

    pygame.display.flip()
