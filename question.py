import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 500  # Increased WIDTH to accommodate all options
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

QUESTION = "What is your favorite programming language?"
OPTIONS = ["A. Python", "B. Java", "C. JavaScript", "D. C++"]

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Question Pop-up")

# Function to display the question and options
def show_question():
    selected_option = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if an option button was clicked
                for i, option_text in enumerate(OPTIONS):
                    button_rect = pygame.Rect(
                        (WIDTH - 400) // 2,
                        200 + i * 70,
                        400,
                        50
                    )
                    if button_rect.collidepoint(event.pos):
                        selected_option = option_text.split(". ")[1]

        screen.fill(WHITE)
        
        # Draw the question
        question_text = FONT.render(QUESTION, True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(question_text, question_rect)

        # Create and draw option buttons
        for i, option in enumerate(OPTIONS):
            button_rect = pygame.Rect(
                (WIDTH - 400) // 2,
                200 + i * 70,
                400,
                50
            )
            pygame.draw.rect(screen, BLACK, button_rect)
            option_text = FONT.render(option, True, WHITE)
            option_rect = option_text.get_rect(center=button_rect.center)
            screen.blit(option_text, option_rect)

        pygame.display.flip()

        # If an option is selected, exit the loop and close the window
        if selected_option:
            return selected_option

    pygame.quit()

# show_question()
