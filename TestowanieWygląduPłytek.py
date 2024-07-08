import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Rozmiar ekranu
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Rozmiar kafelka
TILE_SIZE = 128

# Liczba kafelków wzdłuż osi X i Y
TILES_X = SCREEN_WIDTH // TILE_SIZE
TILES_Y = SCREEN_HEIGHT // TILE_SIZE

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Funkcja do rysowania siatki kafelków wyśrodkowanej na ekranie
def draw_grid_centered(screen):
    start_x = (SCREEN_WIDTH - TILES_X * TILE_SIZE) // 2
    start_y = (SCREEN_HEIGHT - TILES_Y * TILE_SIZE) // 2
    for y in range(TILES_Y):
        for x in range(TILES_X):
            rect = pygame.Rect(start_x + x * TILE_SIZE, start_y + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 2)  # Rysowanie obramowania kafelków

# Funkcja główna
def main():
    # Utworzenie okna
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Testowanie wyglądu')

    # Pętla główna
    while True:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Wypełnienie tła
        screen.fill(BLACK)

        # Rysowanie siatki kafelków wyśrodkowanej na ekranie
        draw_grid_centered(screen)

        # Odświeżenie ekranu
        pygame.display.flip()

# Uruchomienie funkcji głównej
if __name__ == '__main__':
    main()
