import pygame

pygame.init()


def draw_text_input(screen, text):
    pygame.draw.rect(screen, (73, 66, 61), (50, 20, 400, 40), border_radius=10)
    pygame.draw.rect(screen, (66, 133, 180), (475, 20, 100, 40), border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), (50, 80, 100, 40), border_radius=10)

    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(50 + 400 / 2, 20 + 40 / 2))



    font2 = pygame.font.Font(None, 24)
    text_surface2 = font2.render('Искать', True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=(475 + 100 / 2, 20 + 40 / 2))

    font3 = pygame.font.Font(None, 20)
    text_surface3 = font3.render('Удалить метку', True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=(50 + 100 / 2, 80 + 40 / 2))

    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    screen.blit(text_surface3, text_rect3)


def touch_input(pressed_coord):
    if (pressed_coord[0] < 50 or pressed_coord[0] > 50 + 400) or (pressed_coord[1] < 20 or pressed_coord[1] > 20 + 40):
        return
    return True


def touch_find(pressed_coord):
    if (pressed_coord[0] < 475 or pressed_coord[0] > 475 + 100) or (
            pressed_coord[1] < 20 or pressed_coord[1] > 20 + 40):
        return
    return True


def touch_delete(pressed_coord):
    if (pressed_coord[0] < 50 or pressed_coord[0] > 50 + 100) or (
            pressed_coord[1] < 80 or pressed_coord[1] > 80 + 40):
        return
    return True