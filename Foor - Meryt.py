import pygame #impordib pygame library
pygame.init() #algatab Pygame'i mooduli, et kasutada selle funktsioone
screen=pygame.display.set_mode([300,300])#loob akna suurusega 300x300 pikslit
pygame.display.set_caption("Foor- Meryt")#määrab akna pealkirjaks "Foor- Meryt"
pygame.draw.circle(screen, [255, 0, 0], [150,60], 40,0)#joonistab punase ringi koordinaatides (x=150, Y=60) raadiusega 40 pikslit, [255, 0, 0] tähistab värvi punane (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40,0)#joonistab kollase ringi koordinaatides (x=150, y=145) raadiusega 40 pikslit,[255, 255, 0] tähistab värvi kollane (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.circle(screen, [0, 255, 0], [150,230], 40,0)#joonistab rohelise ringi koordinaatides (x=150, y=230) raadiusega 40 pikslit, [0, 255, 0] tähistab värvi roheline (RGB), 0 tähendab, et ring on täidetud.
pygame.draw.rect(screen, [153, 153, 153], [100, 10, 100, 270], 2)#joonistab halli ristküliku koordinaatides (X=100, Y=10) laiusega 100 ja kõrgusega 270, [153, 153, 153] on hall värv (RGB), 2 tähendab, et ristkülik on kontuuriga, mitte täidetud.
pygame.display.update()#uuendab ekraani, et kõik joonistatud elemendid ilmuksid nähtavale.
running = True#muutuja, mis kontrollib mängutsüklit.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit() #read 10-14 seadistavad, et programm töötab kuni kasutaja sulgeb akna