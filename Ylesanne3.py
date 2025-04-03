import pygame
import sys

# Funktsioon, mis joonistab ekraanile ruudud
def draw_grid(screen, square_size, rows, cols, line_color):
    for row in range(rows):
        for col in range(cols):
            # Arvutame iga ruudu positsiooni
            x = col * square_size #arvutame ruudu vasaku ülanurga x-koordinaadi
            y = row * square_size #arvutame ruudu ülemise vasaku nurga y-koordinaadi
            pygame.draw.rect(screen, line_color, (x, y, square_size, square_size), 1)

# Algseaded
pygame.init()

# Ekraani suurus
screen_width = 640
screen_height = 480

# Ruudu suuruse, ridade ja veergude arvu ja joone värvi muutmine
square_size = 20  # muudab ruudu suurust
rows = screen_height // square_size  # muudab ridade arvu automaatselt, kui muuta ruudu suurust
cols = screen_width // square_size  # muudab veergude arvu automaatselt, kui muuta ruudu suurust
line_color = (255, 0, 0)  # muudab joone värvi (RGB)

# Loome akna
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ylesanne3")

# Tsükkel, mis joonistab ruudud ja kontrollib sulgemist
running = True
while running:
    # Kontrollime kasutaja sulgemissoovi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Täidame tausta rohelisega
    screen.fill((178, 255, 102))

    # Kutsume funktsiooni, mis joonistab ruudud
    draw_grid(screen, square_size, rows, cols, line_color) #joonistame ruudud vastavalt määratud parameetritele

    # Uuendame ekraani
    pygame.display.flip()

# Pygame'i sulgemine
pygame.quit()
sys.exit()
