import pygame
import random

# Algseadistused
pygame.init()
WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Obstacles")

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Mängija
player_size = 20
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Takistused
obstacle_count = 10
obstacle_size = 30
obstacles = []
for _ in range(obstacle_count):
    x = random.randint(0, WIDTH - obstacle_size)
    y = random.randint(0, HEIGHT - obstacle_size)
    obstacles.append(pygame.Rect(x, y, obstacle_size, obstacle_size))

running = True
player_alive = True

# Mängutsükkel
while running:
    pygame.time.delay(30)
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if player_alive:
        if keys[pygame.K_LEFT] and player_x - player_speed >= 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_speed <= WIDTH - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y - player_speed >= 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y + player_speed <= HEIGHT - player_size:
            player_y += player_speed

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    for obstacle in obstacles:
        pygame.draw.rect(SCREEN, BLACK, obstacle)
        if player_rect.colliderect(obstacle):
            player_alive = False

    pygame.draw.rect(SCREEN, RED if not player_alive else BLUE, player_rect)
    pygame.display.update()

pygame.quit()
#mängu lõpp
