import pygame as pg
import sys

# Inicjalizacja Pygame
pg.init()

# Zmienne wyświetlacza
x = 1920
y = 1080
screen_type = pg.FULLSCREEN
screen = pg.display.set_mode((x, y), screen_type)
clock = pg.time.Clock()
pg.display.set_caption("Deep Mountain")

# Zmienne gry
running = True

# Rozmiar kafelka
TILE_SIZE = 128

# Wymiary mapy (liczba kafelków)
MAP_WIDTH = 50
MAP_HEIGHT = 50

# Kamera
camera_x = 0
camera_y = 0
camera_speed = 10

# Kolory
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Funkcja do rysowania siatki kafelków
def draw_grid(screen):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            rect = pg.Rect(x * TILE_SIZE - camera_x, y * TILE_SIZE - camera_y, TILE_SIZE, TILE_SIZE)
            pg.draw.rect(screen, GRAY, rect, 2)  # Rysowanie obramowania kafelków

# Wydarzenia
def eventListener():
    global running, camera_x, camera_y
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        camera_x -= camera_speed
    if keys[pg.K_RIGHT]:
        camera_x += camera_speed
    if keys[pg.K_UP]:
        camera_y -= camera_speed
    if keys[pg.K_DOWN]:
        camera_y += camera_speed

# Pętla główna
while running:
    # Obsługa zdarzeń
    eventListener()

    # Wypełnienie tła
    screen.fill(BLACK)

    # Rysowanie siatki kafelków
    draw_grid(screen)

    # Odświeżenie ekranu
    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()
