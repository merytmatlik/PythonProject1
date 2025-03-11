import pygame#impordib pygame library
pygame.init()#algatab Pygame'i mooduli, et kasutada selle funktsioone
screen=pygame.display.set_mode([300,300])#loob akna suurusega 300x300 pikslit
pygame.display.set_caption("Lumememm- Meryt")#määrab akna pealkirjaks "Lumememm- Meryt"
pygame.draw.circle(screen, [255, 255, 255], [150,70], 30,0)#joonistab valge ringi koordinaatides (x=150, Y=70) raadiusega 30 pikslit, [255, 255, 255] tähistab värvi valge (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.circle(screen, [255, 255, 255], [150,138], 40,0)#joonistab valge ringi koordinaatides (x=150, Y=138) raadiusega 40 pikslit, [255, 255, 255] tähistab värvi valge (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.circle(screen, [255, 255, 255], [150,226], 50,0)#joonistab valge ringi koordinaatides (x=150, Y=226) raadiusega 50 pikslit, [255, 255, 255] tähistab värvi valge (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.circle(screen, [0, 0, 0], [140,65], 5,0)#joonistab musta ringi koordinaatides (x=140, Y=65) raadiusega 5 pikslit, [0, 0, 0] tähistab värvi must (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.circle(screen, [0, 0, 0], [160,65], 5,0)#joonistab musta ringi koordinaatides (x=140, Y=65) raadiusega 5 pikslit, [0, 0, 0] tähistab värvi must (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.polygon(screen, [255, 0, 0], [(145, 75), (155, 75), (150, 90)], 0)#joonistab punase kolmnurga, [255, 0, 0] määrab punase värvi, 0 tähendab, et kolmnurk on täidetud
pygame.display.update()#muutuja, mis kontrollib mängutsüklit.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()#read 12-17 seadistavad, et programm töötab kuni kasutaja sulgeb akna