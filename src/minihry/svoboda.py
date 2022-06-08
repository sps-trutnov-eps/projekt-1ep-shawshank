import pygame,random,sys
pygame.init()
def main():
    stav_hry = "zivot"
    def spawn_kridy():
        return random.randint(300,780+203)



    okno = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Trida")
    start_time = pygame.time.get_ticks()
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
    font = pygame.font.SysFont("verdana", 150)
    font1  = pygame.font.SysFont("verdana", 50)
    text = font.render("YOU'RE DEAD", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_1 = font.render("YOU WIN", True, ("green"))
    text_1_rect = text_1.get_rect()
    text_1_rect.center = (1280//2, 720//2)
    text_rect.center = (1280//2, 720//2)
    skore = 0
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    krida = pygame.image.load("../data/textury_miniher/krida.png")
    libor = pygame.image.load("../data/textury_miniher/libor.png")
    lavice = pygame.image.load("../data/textury_miniher/lavice.png")
    tabule = pygame.image.load("../data/textury_miniher/tabule.png")
    vyhled = pygame.image.load("../data/textury_miniher/okno.png")
    hrac = pygame.image.load("../data/textury_miniher/hrac.png")
    
    run = True
    while run:
        score_text = font1.render("SCORE: " + str(skore), True, (0, 0, 0))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (1280//2, 17)
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if pygame.time.get_ticks() - start_time > 1000:
            skore = skore+1
            start_time = pygame.time.get_ticks()
            if skore == 10:
                kr = 7
                hr = 5
            if skore == 20:
                kr = 9
                hr = 7
            if skore == 30:
                kr = 11
                hr = 9
            if skore == 40:
                kr = 13
                hr = 11
            if skore == 50:
                okno.fill("white")
                okno.blit(text_1,text_1_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                return(True)
                
        #hra
        if stav_hry == "zivot":
            keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and hx>200:
            hx -= hr
        
        if keys[pygame.K_d] and hx<970-hw:
            hx += hr

       
        #pohyb kridy
        ky+=kr
        if ky > 720 and stav_hry == "zivot":
            ky = 10
            kx = spawn_kridy()
        
        
        #kolize
        if ((kx<hx and kx+kw>hx) or (kx>hx and kx+kw<hx+hw) or (kx<hx+hw and hx+hw<kx+kw)) and (ky+kh>hy):
            stav_hry = "smrt"

        if stav_hry == "zivot":
            okno.fill("white")
            okno.blit(score_text, score_text_rect)
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
            okno.blit(text,text_rect)
            pygame.display.update()
            pygame.time.wait(2000)
            return False
                  
        pygame.display.update()