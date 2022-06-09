import pygame
import sys
import os
import random
pygame.init()

def main():
    clock = pygame.time.Clock()
    v1,v2 = (500,331)
    smer = ""

    generování = True
    
    konec1 = False
    konec = False
    
    panacek = True
    
    obrazek = pygame.image.load(os.path.join("pospisil", "pixil-frame-0.png"))
    
    font = pygame.font.SysFont ("Arial" , 50)
    
    nadpis = font.render("Posbírej 30 třídnic!", True, (255,255,255))
    
    pygame.display.set_caption("Třídnice!")
    
    pozadi = pygame.image.load(os.path.join("pospisil", "121.jpg"))
    
    font1 = pygame.font.SysFont("Arial" , 300)
    
    nadpis1 = font.render("Prohrál jsi!", True, (255,255,255))
    nadpis2 = font.render("Vyhrál jsi!", True, (255,255,255))
    
    
    rozliseni_x = 1000
    rozliseni_y = 667
    
    okno = pygame.display.set_mode((rozliseni_x,rozliseni_y))
    
    skore = 0
    skore_text = font.render("skore: "+str(skore),True,("white"))
    
    cas_zacatek = pygame.time.get_ticks() 

    while True:
        if generování:
            xs = random.randint(36,964)
            ys = random.randint(36,631)
            xs1 = xs + 25
            ys1 = ys + 25
            generování = False
        
        
        if konec == False:
            for udalost in pygame.event.get():
                if udalost.type == pygame.KEYDOWN:
                    if udalost.key == pygame.K_d:
                        smer = "východ"
                    if udalost.key == pygame.K_a:
                        smer = "západ"
                    if udalost.key == pygame.K_s:
                        smer = "jih"
                    if udalost.key == pygame.K_w:
                        smer = "sever"
        if konec1 == False:
            for udalost in pygame.event.get():
                if udalost.type == pygame.KEYDOWN:
                    if udalost.key == pygame.K_d:
                        smer = "východ"
                    if udalost.key == pygame.K_a:
                        smer = "západ"
                    if udalost.key == pygame.K_s:
                        smer = "jih"
                    if udalost.key == pygame.K_w:
                        smer = "sever"
        
        if v1 < 0:
            v1 = 0
        if v2 < 0:
            v2 = 0
        if v1 > rozliseni_x - 25:
            v1 = rozliseni_x - 25
        if v2 > rozliseni_y - 25:
            v2 = rozliseni_y - 25
        
        ubehly_cas = pygame.time.get_ticks()-cas_zacatek
        ubehly_cas1 = ubehly_cas//1000
        
        
        clock_text = font.render("čas:  "+str(ubehly_cas1), True, ("white"))
        
        
        
        
        #kolize se trídní knihou
        if (xs < v1 < xs1 and ys < v2 < ys1) or (xs < v1+25 < xs1 and ys < v2 < ys1) or (xs < v1 < xs1 and ys < v2+25 < ys1) or (xs < v1+25 < xs1 and ys < v2+25 < ys1):
            generování = True
            skore += 1
            skore_text = font.render("skore: "+str(skore),True,("white"))
        
        
        if smer is "sever":
            v2 = v2-0.5
        if smer is "jih":
            v2 = v2+0.5
        if smer is "východ":
            v1 = v1+0.5
        if smer is "západ":
            v1 = v1-0.5
        
        okno.fill((0,0,0))
        
        okno.blit(pozadi,(0,0,  ))
        if panacek == True:
            pygame.draw.rect(okno, (255,255, 255), (v1,v2, 25,25))
                    
        
        okno.blit(obrazek,(xs,ys, 25,25))
        
        okno.blit(nadpis, (50,20))
        
        okno.blit(skore_text,(50,80))
        okno.blit(clock_text,(50,140))
        cas_zacatek1 = pygame.time.get_ticks()

        if skore == 30:
                konec1 = True
        if konec1 == True:
            panacek = False
            okno.blit(nadpis2, (rozliseni_x/2 - nadpis2.get_rect().width/2, rozliseni_y/2 - nadpis2.get_rect().height/2))
        if konec1 == True and ubehly_cas1 >=70:
            return(True)
        
        
        if ubehly_cas1 >= 60 :
            konec = True
        if konec == True:
            panacek = False
            okno.blit(nadpis1, (rozliseni_x/2 - nadpis1.get_rect().width/2, rozliseni_y/2 - nadpis1.get_rect().height/2))
        if konec == True and ubehly_cas1 >=10:
            return(True)
        

                
                
        

        
        pygame.display.update()
        
        if udalost.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #konec
