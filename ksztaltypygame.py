import pygame
okno = pygame.display.set_mode([800,800])
pygame.display.set_caption("Pygame is (probably) Cool!")

# robi kwadrat z kolorami RGB
pygame.draw.rect(okno, [255,0,0],  pygame.Rect(100,100,150,250))

# robi kółko
pygame.draw.circle(okno, [0,0,255], [400,300], 50)

# robi wielokąt
pygame.draw.polygon(okno, [255,255,0], [[175,175], [400,300], [300,0]])

# pokazuje kwadrat i inne rzeczy
pygame.display.update
