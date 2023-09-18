import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
QUESTION = "What is your favorite programming language?"
OPTIONS = ["Python", "Java", "JavaScript", "C++"]

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
                    option_rect = pygame.Rect(
                        (WIDTH - 200) // 2,
                        200 + i * 70,
                        200,
                        50
                    )
                    if option_rect.collidepoint(event.pos):
                        selected_option = option_text

        screen.fill(WHITE)

        # Draw the question
        question_text = FONT.render(QUESTION, True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(question_text, question_rect)

        # Create and draw option buttons
        for i, option in enumerate(OPTIONS):
            button_rect = pygame.Rect(
                (WIDTH - 200) // 2,
                200 + i * 70,
                200,
                50
            )
            pygame.draw.rect(screen, BLACK, button_rect)
            pygame.draw.rect(screen, WHITE, button_rect.inflate(-10, -10))
            option_text = FONT.render(option, True, BLACK)
            option_rect = option_text.get_rect(center=button_rect.center)
            screen.blit(option_text, option_rect)

        pygame.display.flip()

        # If an option is selected, exit the loop and close the window
        if selected_option:
            print(selected_option)
            break

    pygame.quit()


# Show the question pop-up
# show_question()
