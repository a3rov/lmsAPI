import pygame

pygame.init()


def draw_text_input(screen, text):
    pygame.draw.rect(screen, (73, 66, 61), (50, 20, 400, 40), border_radius=10)
    pygame.draw.rect(screen, (66, 133, 180), (475, 20, 100, 40), border_radius=10)

    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(50 + 400 / 2, 20 + 40 / 2))

    font2 = pygame.font.Font(None, 24)
    text_surface2 = font2.render('Найти', True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=(475 + 100 / 2, 20 + 40 / 2))
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)


def touch_input(pressed_coord):
    if (pressed_coord[0] >= 50 and pressed_coord[0] <= 50 + 400) \
            and (pressed_coord[1] >= 20 and pressed_coord[1] <= 20 + 40):
        return True


def touch_find(pressed_coord):
    if (pressed_coord[0] >= 475 and pressed_coord[0] <= 475 + 100) \
            and (pressed_coord[1] >= 20 and pressed_coord[1] <= 20 + 40):
        return True