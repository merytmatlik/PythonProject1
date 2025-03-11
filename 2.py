import pygame#impordib pygame library
pygame.init()#algatab Pygame'i mooduli, et kasutada selle funktsioone
screen=pygame.display.set_mode([640,480])#loob akna suurusega 640x480 pikslit
pygame.display.set_caption("2")#määrab akna pealkirjaks "2"
background = pygame.image.load("bg_shop.png")  # Laeb pildi
screen.blit(background, (0, 0))  # Joonistab taustapildi aknasse
seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [255, 310])
screen.blit(seller,[105,155])
pygame.display.update()#muutuja, mis kontrollib mängutsüklit.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()#read 12-17 seadistavad, et programm töötab kuni kasutaja sulgeb akna