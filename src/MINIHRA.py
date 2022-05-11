import pygame,random
import sys

stav_hry = "zivot"
def spawn_kridy():
    return random.randint(300,780+203)



okno = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Trida")

kx = spawn_kridy()
ky = 10
kw = 20
kh = 132

hx = 400
hy = 550
hw = 223
hh = 151

hr = 5
kr = 5
krida = pygame.image.load("krida.png")
libor = pygame.image.load("libor.png")
lavice = pygame.image.load("lavice.png")
tabule = pygame.image.load("tabule.png")
vyhled = pygame.image.load("okno.png")
hrac = pygame.image.load("hrac.png")


run = True
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            
    #hra
    if stav_hry == "zivot":
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hx>200:
        hx -= hr
    
    if keys[pygame.K_RIGHT] and hx<970-hw:
        hx += hr

   
    #pohyb kridy
    ky+=5
    if ky > 720 and stav_hry == "zivot":
        ky = 10
        kx = spawn_kridy()
    
    
    #kolize
    if ((kx<hx and kx+kw>hx) or (kx>hx and kx+kw<hx+hw) or (kx<hx+hw and hx+hw<kx+kw)) and (ky+kh>hy):
        stav_hry = "smrt"

    if stav_hry == "zivot":
        okno.fill("white")
        
        okno.blit(tabule, (150, 40))
        okno.blit(libor, (900, 0))
        okno.blit(lavice, (200, 300))
        okno.blit(lavice, (500, 300))
        okno.blit(lavice, (800, 300))
        okno.blit(lavice, (200, 400))
        okno.blit(lavice, (800, 400))
        okno.blit(lavice, (500, 400))
        okno.blit(vyhled, (20, 500))
        okno.blit(vyhled, (20, 280))
        okno.blit(hrac, (hx, hy))
        okno.blit(krida, (kx,ky))
        
    if stav_hry == "smrt":
        okno.fill("black")
        
    
              
    pygame.display.update()
pygame.quit()
sys.exit()