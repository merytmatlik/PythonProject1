import pygame
import random

pygame.init()

pygame.mixer.music.load('game-tune.mp3')
pygame.mixer.music.play(-1)#-1 tähendab, et kordab lõputult taustaheli
game_over_sound = pygame.mixer.Sound('game-over.wav')  #laeb game over heli faili
bounce_sound = pygame.mixer.Sound('bounce.mp3')  #laeb põrkeheli faili

WIDTH, HEIGHT = 640, 480  #mänguakna suurus
BALL_SIZE = 20  #palli suurus (pikkus ja laius)
PADDLE_WIDTH, PADDLE_HEIGHT = 120, 20  #aluse mõõdud
BALL_SPEED = [4, 4]  #palli algkiirus (x, y suunas)
PADDLE_SPEED = 6  #kui kiiresti alus liigub

#VÄRVID
LIGHT_BLUE = (173, 216, 230)  #taustavärv
BLACK = (0, 0, 0)  #teksti värv
RED = (255, 0, 0)  #mängu lõpu teksti värv

screen = pygame.display.set_mode((WIDTH, HEIGHT))  #mänguakna loomine
pygame.display.set_caption("Ping-Pong")  #mängu pealkiri
clock = pygame.time.Clock()  #loob kellaobjekti, mida kasutatakse mängu kaadrisageduse (FPS – frames per second) kontrollimiseks

#PILTIDE LAADIMINE JA SKALEERIMINE
ball_image = pygame.image.load("ball.png")  #palli pildi laadimine
paddle_image = pygame.image.load("pad.png")  #aluse pildi laadimine
ball_image = pygame.transform.scale(ball_image, (BALL_SIZE, BALL_SIZE))  #muudab palli suuruse õigeks
paddle_image = pygame.transform.scale(paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))  #muudab aluse suuruse õigeks

#FUNKTSIOON, MIS TAASKÄIVITAB MÄNGU
def reset_game():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, paddle_x, score, game_over
    ball_x = WIDTH // 2 - BALL_SIZE // 2  #palli horisontaalne algpositsioon
    ball_y = 0  #palli vertikaalne algpositsioon (alustab ülevalt)
    ball_speed_x, ball_speed_y = BALL_SPEED  #palli kiiruse jagamine x ja y teljele
    paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2  #aluse horisontaalne algpositsioon (keskel)
    score = 0  #algne skoor
    game_over = False  #mäng ei ole läbi
    pygame.mixer.music.play(-1)  #taustamuusika mängima uuesti

#ALGSEISUND
reset_game()
paddle_y = HEIGHT / 1.5  #aluse vertikaalne positsioon (fikseeritud)
font = pygame.font.Font(None, 36)  #font skoori ja tekstide jaoks
running = True  #peamine mängutsükkel töötab seni, kuni see on True

#MÄNGUTSÜKKEL
while running:
    screen.fill(LIGHT_BLUE)  #täidab tausta helesinise värviga igal kaadril

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  #kui kasutaja sulgeb akna, lõpetame tsükli

    #MÄNGU PEAMINE LOOGIKA
    if not game_over:

        #klaviatuuri sisend – vasakule ja paremale liikumine
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= PADDLE_SPEED  #liiguta alust vasakule
        if keys[pygame.K_RIGHT] and paddle_x + PADDLE_WIDTH < WIDTH:
            paddle_x += PADDLE_SPEED  #liiguta alust paremale

        #liiguta palli vastavalt kiirusele
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        #kui pall tabab vasakut või paremat seina – põrkub
        if ball_x <= 0 or ball_x + BALL_SIZE >= WIDTH:
            ball_speed_x *= -1
            bounce_sound.play()#mängib põrkeheli

        #kui pall tabab ülemist seina – põrkub
        if ball_y <= 0:
            ball_speed_y *= -1
            bounce_sound.play()#mängib põrkeheli

        #kui pall tabab alust – põrkub tagasi ja lisatakse skoor
        if (paddle_y <= ball_y + BALL_SIZE <= paddle_y + PADDLE_HEIGHT and
                paddle_x <= ball_x + BALL_SIZE // 2 <= paddle_x + PADDLE_WIDTH and
                ball_speed_y > 0):
            ball_speed_y *= -1
            bounce_sound.play()#mängib põrkeheli
            score += 1  #suurendame skoori ühe võrra

        #kui pall kukub ekraanist välja (alla) – mäng on läbi
        if ball_y + BALL_SIZE >= HEIGHT:
            pygame.mixer.music.stop()  #peatab taustamuusika
            game_over_sound.play()  # mängib game over heli
            game_over = True  #märgime mängu lõppenuks

        #joonistame palli ja aluse
        screen.blit(ball_image, (ball_x, ball_y))
        screen.blit(paddle_image, (paddle_x, paddle_y))

        #joonistame skoori ekraanile
        score_text = font.render(f"Skoor: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    #MÄNGU LÕPUEKRAAN
    else:
        #näitame teksti "Mäng läbi" ja skoori
        game_over_text = font.render("Mäng läbi! Vajuta ESC või r (Restart).", True, RED)
        final_score_text = font.render(f"Lõpp-skoor: {score}", True, BLACK)

        #paigutame teksti ekraanile
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
        screen.blit(final_score_text, (WIDTH // 2 - 80, HEIGHT // 2 + 20))

        #võimalus mäng sulgeda ESC klahviga või alustada uuesti R klahviga
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_r]:
            reset_game()  #taaskäivitab mängu

    #EKRAANI UUENDAMINE
    pygame.display.flip()  #kuvab kõik joonistatud elemendid ekraanil
    clock.tick(60)  #piirab mängu kiiruse 60 FPS peale

#kui tsükkel lõpeb, sulgeme Pygame'i
pygame.quit()
