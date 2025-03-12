import pygame  # Impordib pygame'i
pygame.init()  # Algatab Pygame'i mooduli

screen = pygame.display.set_mode([640, 480])  # Loob akna suurusega 640x480 pikslit
pygame.display.set_caption("2")  # Määrab akna pealkirja

# Laeb pildid
background = pygame.image.load("bg_shop.png")#laeb taustapildi
seller = pygame.image.load("seller.png")#laeb müüja pildi
chat = pygame.image.load("chat.png")#laeb jutumulli

# Muudab piltide suurust
seller = pygame.transform.scale(seller, [255, 304])#muudab müüja pildi suurust
chat = pygame.transform.scale(chat, [257, 200])#muudab jutumulli suurust

# Joonistab pildid õigesti järjestikku
screen.blit(background, (0, 0))  # Kõigepealt taust
screen.blit(seller, [105, 160])  # Siis müüja
screen.blit(chat, [245, 70])  # Siis vestlusmull (erinev asukoht, et mitte katta müüjat)

#lisame teksti
font = pygame.font.SysFont('arial', 24)
text = font.render("Tere! Olen Meryt!", True, [255,255,255])
screen.blit(text, [280,140])

pygame.display.update()  # Uuendab ekraani

# Pygame'i mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()  # Lõpetab Pygame'i
