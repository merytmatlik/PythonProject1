import pygame
import sys     #impordib süsteemimooduli, et saaks kasutada sys.exit()
import random  #lisatud juhuslike värvide genereerimiseks

# Algväärtused
pygame.init()  #käivitab kõik vajalikud Pygame moodulid
WIDTH, HEIGHT = 640, 512  #määrab akna laiuse ja kõrguse
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #loob mänguakna määratud suurusega
pygame.display.set_caption("Mullimäng")  #määrab akna nime

# Värvid
BACKGROUND_COLOR = (173, 216, 230)  #määrab taustavärvi (helesinine)

# Ringi info (koordinaadid + raadius + värv)
circles = []  # list kõigi ringide kohta (asukoht ja raadius)
radius = 5  #algne ringi raadius

# Põhitsükkel, mis töötab seni, kuni kasutaja akna sulgeb
running = True
while running:
    screen.fill(BACKGROUND_COLOR)  #täidab ekraani taustavärviga

    # Joonistab kõik olemasolevad ringid
    for pos, r, color in circles:
        pygame.draw.circle(screen, color, pos, r, 1)  #joonistab ringi etteantud positsiooni ja raadiusega

    # Kontrollib kõiki sündmusi (nt. hiireklikk või akna sulgemine)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #kui kasutaja sulgeb akna...
            running = False  #lõpetab mängu tsükli

        elif event.type == pygame.MOUSEBUTTONDOWN:  #kui kasutaja klõpsab hiirega
            pos = pygame.mouse.get_pos()  #saab kliki asukoha (x, y)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  #genereerib juhusliku värvi
            circles.append((pos, radius, color))  #lisab uue ringi andmed listi
            radius += 2  #suurendab järgmise ringi raadiust

    pygame.display.flip()  #värskendab ekraani, et muudatused oleks nähtavad

pygame.quit()  #sulgeb Pygame
sys.exit()  #lõpetab programmi töö
