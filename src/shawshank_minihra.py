import pygame
import sys

rozliseni_okna = rozliseni_x, rozliseni_y = (1200,800)
pozadi_barva = (186, 140, 90)

w_pap = rozliseni_x / 2
h_pap = rozliseni_y * 0.937
h_odp = 75
w_odp = 100
x_pap = (rozliseni_x - w_pap) / 2
y_pap = (rozliseni_y - h_pap) / 2
x1 = (x_pap) + (w_odp/2)
x2 = ((x_pap + w_pap) / 2) + w_odp
x3 = (x_pap + w_pap) - (w_odp + w_odp / 2)
y_odp = y_pap * 24.16

    
pygame.init()
okno = pygame.display.set_mode(rozliseni_okna)



while True:
    udalosti = pygame.event.get()
    stisknuto = pygame.key.get_pressed()
    
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
      
    okno.fill(pozadi_barva)
    
    pygame.draw.rect(okno, (255, 255, 255), (x_pap,y_pap,w_pap,h_pap))
    pygame.draw.rect(okno, (0, 0, 0), (x1,y_odp,w_odp,h_odp), (5))
    pygame.draw.rect(okno, (0, 0, 0), (x2,y_odp,w_odp,h_odp), (5))
    pygame.draw.rect(okno, (0, 0, 0), (x3,y_odp,w_odp,h_odp), (5))
    pygame.display.update()
