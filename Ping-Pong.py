import pygame
import random

pygame.init()

# Mängu seadistused
WIDTH, HEIGHT = 640, 480  # Ekraani suurus
BALL_SIZE = 20  # Palli suurus
PADDLE_WIDTH, PADDLE_HEIGHT = 120, 20  # Aluse suurus
BALL_SPEED = [4, 4]  # Palli algkiirus
PADDLE_SPEED = 4  # Aluse kiirus

# Värvid
LIGHT_BLUE = (173, 216, 230)#tausta värv
BLACK = (0, 0, 0)#skoori teksti värv

# Ekraani loomine
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")
clock = pygame.time.Clock()#loob kellaobjekti, mida kasutatakse mängutsükli kiiruse kontrollimiseks

# Laadi pildid
ball_image = pygame.image.load("ball.png")
paddle_image = pygame.image.load("pad.png")
ball_image = pygame.transform.scale(ball_image, (BALL_SIZE, BALL_SIZE))
paddle_image = pygame.transform.scale(paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))

# Palli algseisund
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = 0 #alustab ülevalt keskelt
ball_speed_x, ball_speed_y = BALL_SPEED

# Aluse algseisund
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT / 1.5
paddle_direction = 1

# Skoor
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(LIGHT_BLUE)  # Taustavärv

    #mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #kontrollib, kas kasutaja sulgeb akna
            running = False #Peatab mängutsükli

    # Liiguta palli
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Palli põrkumine seintelt
    if ball_x <= 0 or ball_x + BALL_SIZE >= WIDTH:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # Palli põrkumine alusega
    if (paddle_y <= ball_y + BALL_SIZE <= paddle_y + PADDLE_HEIGHT and
            paddle_x <= ball_x + BALL_SIZE // 2 <= paddle_x + PADDLE_WIDTH and
            ball_speed_y > 0):
        ball_speed_y *= -1
        score += 1  # Suurenda skoori

    # Kui pall kukub ekraanilt välja
    if ball_y + BALL_SIZE >= HEIGHT:
        score -= 1  # Vähenda skoori
        ball_x, ball_y = WIDTH // 2 - BALL_SIZE // 2, 0  # Lähtesta palli asukoht ülevalt keskelt
        ball_speed_x, ball_speed_y = random.choice([-4, 4]), 4  # Määra uus suund

    # Liiguta alust
    paddle_x += PADDLE_SPEED * paddle_direction
    if paddle_x <= 0 or paddle_x + PADDLE_WIDTH >= WIDTH:
        paddle_direction *= -1  # Muuda aluse suunda

    # Joonista pall ja alus
    screen.blit(ball_image, (ball_x, ball_y))
    screen.blit(paddle_image, (paddle_x, paddle_y))

    # Kuvame skoori ekraanil
    score_text = font.render(f"Skoor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()#uuendab kogu ekraani ja kuvab kõik joonistatud objektid
    clock.tick(60)  # Määrame kaadrisageduse- piirab mängu kiiruse 60 kaadrini sekundis (FPS), mis tagab sujuva ja ühtlase mängukogemuse kõigil seadmetel

pygame.quit()

