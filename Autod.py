import pygame
import random

# Pygame algatamine
pygame.init()

# Ekraani suurus ja värvid
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Autod")

# Värvid
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Piltide laadimine
background_img = pygame.image.load('bg_rally.jpg')  # Taustapilt
red_car_img = pygame.image.load('f1_red.png')  # Punane auto
blue_car_img = pygame.image.load('f1_blue.png')  # Sinine auto

# Punase auto sätted
red_car_width = red_car_img.get_width()
red_car_height = red_car_img.get_height()
red_car_x = (screen_width - red_car_width) // 2
red_car_y = screen_height - red_car_height - 10

# Sinised autod
blue_cars = []
num_blue_cars = 2
for _ in range(num_blue_cars):
    blue_car_y = random.randint(-screen_height, -50)  # Alustavad ekraanilt väljaspool
    blue_car_x = random.randint(150, 450)  # Auto ilmub ainult etteantud vahemikus
    # Kontrollime, et sinine auto x-positsioon ei satu punase auto x-vahemikku
    while (blue_car_x >= red_car_x and blue_car_x <= red_car_x + red_car_width):
        blue_car_x = random.choice([random.randint(150, 200), random.randint(400, 450)])
    blue_cars.append([blue_car_x, blue_car_y])  # Lisame auto x ja y koordinaadid loendisse

# Mängu sätete algväärtused
score = 0
font = pygame.font.SysFont(None, 36)

# Mängu tsükkel
running = True
while running:
    screen.fill(WHITE)

    # Taustapildi joonistamine
    screen.blit(background_img, (0, 0))

    # Kontrollige sündmusi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Sinised autod liikumiseks
    for car in blue_cars:
        car[1] += 5  # Auto liikumiskiirus

        # Kui auto jõuab ekraani alla, alustab see uuesti ülevalt
        if car[1] > screen_height:
            car[1] = random.randint(-screen_height, -50)
            # Uus x-positsioon, kus see ei satu punase auto x-vahemikku
            car[0] = random.choice([random.randint(150, 200), random.randint(400, 450)])
            score += 1  # Skoori lisamine

        # Joonista sinine auto
        screen.blit(blue_car_img, (car[0], car[1]))

    # Punase auto kuvamine
    screen.blit(red_car_img, (red_car_x, red_car_y))

    # Skoori kuvamine (teisendatakse stringiks)
    score_text = font.render("Skoor: " + str(score), True, BLUE)
    screen.blit(score_text, (10, 10))

    # Ekraani värskendamine
    pygame.display.update()

    # Mängu kiirus
    pygame.time.Clock().tick(60)

# Lõpetamine
pygame.quit()

