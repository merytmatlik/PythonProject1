import pygame
pygame.init()
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Foor- Meryt")
pygame.draw.circle(screen, [255, 0, 0], [150,60], 40,0)
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40,0)
pygame.draw.circle(screen, [0, 255, 0], [150,230], 40,0)
pygame.draw.rect(screen, [153, 153, 153], [100, 50, 80, 250], 2)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()