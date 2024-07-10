import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Norse Magic 8 Ball Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
light_gray = (200, 200, 200)

# Font settings
font = pygame.font.Font(None, 36)

# Ancient Norse wisdom responses
norse_wisdom = [
    "Wisdom is welcome wherever it comes from.",
    "A guest should be courteous when he comes to the table.",
    "The unwise man lies awake all night.",
    "Cattle die, kinsmen die, one day you will die.",
    "The foolish man thinks he will live forever if he avoids battle.",
    "A man is happy if he finds praise and friendship within himself.",
    "Better to fight and fall than to live without hope.",
    "The cautious guest who comes to a meal seldom speaks.",
    "Bravery is half the battle.",
    "Where you recognize evil, speak out against it, and give no truces to your enemies."
]

# Game variables
input_active = True
input_text = ""
answer_text = ""

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Main game loop
running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() != "":
                        answer_text = random.choice(norse_wisdom)
                        input_active = False
                        input_text = ""
                    else:
                        answer_text = "Please ask a question."
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            else:
                if event.key == pygame.K_SPACE:
                    input_text = ""
                    answer_text = ""
                    input_active = False

    # Draw input box
    input_box_color = light_gray if input_active else black
    pygame.draw.rect(screen, input_box_color, (100, 100, 600, 50), 2)
    draw_text(input_text, font, black, screen, 110, 110)

    # Draw answer text
    draw_text(answer_text, font, black, screen, 100, 200)

    # Debug: Print current input and answer text
    print(f"Input: {input_text}, Answer: {answer_text}")

    pygame.display.flip()

pygame.quit()
