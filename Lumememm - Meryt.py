import pygame
pygame.init()
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumememm- Meryt")
pygame.draw.circle(screen, [255, 255, 255], [150,70], 30,0)
pygame.draw.circle(screen, [255, 255, 255], [150,138], 40,0)
pygame.draw.circle(screen, [255, 255, 255], [150,226], 50,0)
pygame.draw.circle(screen, [0, 0, 0], [140,65], 5,0)
pygame.draw.circle(screen, [0, 0, 0], [160,65], 5,0)
pygame.draw.polygon(screen, [255, 0, 0], [(145, 75), (155, 75), (150, 90)], 0)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()