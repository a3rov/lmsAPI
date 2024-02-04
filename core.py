import os

import pygame
import requests

import drawing

delta = '0.05'
map_file = "data/map.png"
is_typing = False
allow_symblos = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z',
                 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '0',
                 '-', '=', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '?', '(', ')', '%', '!', 'Ё', 'ё', 'й', 'ц', 'у',
                 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',
                 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х',
                 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б',
                 'Ю']

clock = pygame.time.Clock()

url = 'Казань'

move_x = 0
move_y = 0

type_map = 0
maps = ['map', 'sat', 'skl']


def get_map(adress):
    try:
        cords = get_cords(adress)
        response = get_picture(cords, delta)

        with open(map_file, "wb") as file:
            file.write(response.content)

    finally:
        return pygame.image.load(map_file)


def get_picture(centre, delta):
    map_api_server = "http://static-maps.yandex.ru/1.x/"

    map_params = {
        "ll": centre,
        "spn": ",".join([str(delta), str(delta)]),
        "l": maps[type_map]
    }

    return requests.get(map_api_server, params=map_params)


def get_cords(toponym):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split()

    return ','.join([str(float(toponym_longitude) + move_x * float(delta) * 10),
                     str(float(toponym_lattitude) + move_y * float(delta) * 10)])


def change_map():
    global type_map
    if type_map == len(maps) - 1:
        type_map = 0
    else:
        type_map += 1


if __name__ == '__main__':
    get_map(url)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    running = True
    image = pygame.image.load(map_file)
    screen.blit(image, (0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if drawing.touch_input(pygame.mouse.get_pos()):
                    if is_typing:
                        is_typing = False
                    else:
                        is_typing = True

                if drawing.touch_find(pygame.mouse.get_pos()):
                    image = get_map(url)
                    screen.fill((0, 0, 0))
                    screen.blit(image, (0, 0))
                    is_typing = False

            if event.type == pygame.KEYDOWN:
                key = event.key
                if is_typing:
                    if key == pygame.K_BACKSPACE:
                        url = url[:len(url) - 1]

                    elif key == pygame.K_SPACE:
                        url += ' '
                    elif event.unicode in allow_symblos:
                        url += event.unicode

                    continue

                if key == pygame.K_PAGEUP:
                    if float(delta) < 32:
                        delta = str(float(delta) * 1.5)

                if key == pygame.K_PAGEDOWN:
                    if float(delta) > 0.0001:
                        delta = str(float(delta) / 1.5)

                if key == pygame.K_UP:
                    move_y += 0.05

                if key == pygame.K_DOWN:
                    move_y -= 0.05

                if key == pygame.K_RIGHT:
                    move_x += 0.05

                if key == pygame.K_LEFT:
                    move_x -= 0.05

                if key == pygame.K_1:
                    change_map()

                image = get_map(url)
                screen.fill((0, 0, 0))
                screen.blit(image, (0, 0))

        drawing.draw_text_input(screen, url)
        pygame.display.flip()

    pygame.quit()
    os.remove(map_file)