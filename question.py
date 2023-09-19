import pygame
import sys
import json
import random
import textwrap

f = open('D:\Downloads\Geeky-Pac-Man-main\questionBank.json')
data = json.load(f)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 500  # Increased WIDTH to accommodate all options
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)


def wrap_text(text, width):
    # Use textwrap to break the text into multiple lines
    wrapper = textwrap.TextWrapper(width=width)
    wrapped_text = wrapper.wrap(text)
    return wrapped_text


# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Function to display the question and options


def show_question():

    selected_option = None
    question_data = random.choice(data)
    correct_answer = question_data["Correct Answer"]

    start_time = pygame.time.get_ticks()  # Record the start time

    while pygame.time.get_ticks() - start_time < 5000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if an option button was clicked
                for i, option_text in enumerate(question_data["Options"]):
                    button_rect = pygame.Rect(
                        (WIDTH - 400) // 2,
                        200 + i * 70,
                        400,
                        50
                    )
                    if button_rect.collidepoint(event.pos):
                        selected_option = option_text
        # screen.fill(WHITE)
        background = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        # 200 is the alpha value for transparency
        background.fill((255, 255, 255, 200))
        screen.blit(background, (0, 0))

        # Draw the question
        # question_text = FONT.render(question_data["Question"], True, BLACK)
        # question_rect = question_text.get_rect(center=(WIDTH // 2, 100))
        # screen.blit(question_text, question_rect)
        # Adjust the character count as needed
        question_lines = wrap_text(question_data["Question"], 50)

        # Draw the question lines
        y_offset = 100
        for line in question_lines:
            question_text = FONT.render(line, True, BLACK)
            question_rect = question_text.get_rect(
                center=(WIDTH // 2, y_offset))
            screen.blit(question_text, question_rect)
            y_offset += question_rect.height + 10

        # Create and draw option buttons
        for i, option in enumerate(question_data["Options"]):
            button_rect = pygame.Rect(
                (WIDTH - 400) // 2,
                200 + i * 70,
                400,
                50
            )
            pygame.draw.rect(screen, BLACK, button_rect)
            option_text = FONT.render(str(option["Option"]), True, WHITE)
            option_rect = option_text.get_rect(center=button_rect.center)
            screen.blit(option_text, option_rect)

        pygame.display.flip()

        # If an option is selected, exit the loop and close the window
        if selected_option:
            return str(selected_option["Option"]) == str(correct_answer)
    return False


# show_question()
