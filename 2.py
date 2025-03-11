import pygame  # Impordib pygame'i
pygame.init()  # Algatab Pygame'i mooduli

screen = pygame.display.set_mode([640, 480])  # Loob akna suurusega 640x480 pikslit
pygame.display.set_caption("2")  # Määrab akna pealkirja

# Laeb pildid
background = pygame.image.load("bg_shop.png")#laeb taustapildi
seller = pygame.image.load("seller.png")#laeb müüja pildi
chat = pygame.image.load("chat.png")#laeb jutumulli

# Muudab piltide suurust
seller = pygame.transform.scale(seller, [255, 310])#
chat = pygame.transform.scale(chat, [150, 150])

# Joonistab pildid õigesti järjestikku
screen.blit(background, (0, 0))  # Kõigepealt taust
screen.blit(seller, [105, 155])  # Siis müüja
screen.blit(chat, [200, 100])  # Siis vestlusmull (erinev asukoht, et mitte katta müüjat)

pygame.display.update()  # Uuendab ekraani

# Pygame'i mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()  # Lõpetab Pygame'i
