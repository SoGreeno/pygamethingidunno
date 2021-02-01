import pygame
import time
# pygame pygame.display.set_mode umożliwia zmianę rodzielczości okienka
okno = pygame.display.set_mode([400,300])
# pygame.display.set_caption to prawie jak <title> w HTML
pygame.display.set_caption("obrazy")
# ładuje zdjęcie
vdv = pygame.image load("vdv.png")
vx = 1
vy = 1
x = 35
y = 30
while true:
    x += vx
    y += vy
    if x < 1:
        vx = 1
        elif x > 330:
            vx= -1
        if y < 1:
            vy = 1
        elif y > 240:
            vy = 1
        vy = 1
        # wypełnia kolor tła za pomocą RGB
        okno.fill([255,255,255])
        okno.blit(vdv, [x,y])
        # pygame.display.flip() robi obrócenie. Że z lewo na prawo lub na odwrót
        pygame.display.flip()
        time sleep(0.03)
#NIE KRADZIONE Z INTERNETU. PROSTO Z KSIĄŻKI
