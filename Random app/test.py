import pygame
from unidecode import unidecode

pygame.init()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 36)

text = ""
input_text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                input_text = text
                text = ""
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                char = unidecode(event.unicode)  # Chuyển đổi telex thành Unicode
                text += char

    screen.fill((255, 255, 255))
    text_surface = font.render("Input: " + text, True, (0, 0, 0))
    input_text_surface = font.render("Input Text: " + input_text, True, (0, 0, 0))

    screen.blit(text_surface, (20, 20))
    screen.blit(input_text_surface, (20, 60))

    pygame.display.flip()
