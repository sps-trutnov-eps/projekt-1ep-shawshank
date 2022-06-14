import random
import pygame
import sys

pygame.init()

rozliseni = rozliseni_x, rozliseni_y = (800, 600)
font1 = pygame.font.SysFont ("Arial", 20)
font2 = pygame.font.SysFont("Calibri", 120)
font3 = pygame.font.SysFont("Calibri", 30)
font4 = pygame.font.SysFont ("Arial", 40)
nadpis = font1.render("Vypočítej tyto příklady:", True, (0, 0, 0))
vysledek = font1.render("Výsledek: ", True, (0, 0, 0))
prikladuSpatne = 0
prikladuDobre = 0
hotovozInt = 0
hotovoz = font4.render(f"{hotovozInt}/10", True, (0, 0, 0))
screen = pygame.display.set_mode((rozliseni_x, rozliseni_y))
pygame.display.set_caption('Počítání příkladů')

timeOut = 0

vyberPozice = (10, 400)
vyberVelikost = (rozliseni_x/3-20, 150)

precti = open("priklady.txt", "r")
p = precti.read()
precti.close()
p = p.strip().split("\n")

priklad = random.choice(p)
prikladText = font2.render(priklad, True, (0, 0, 0))
spravnyVyber = random.choice(range(0, 2+1))

spravnaOdpoved = 0
spatnaOdpoved1 = 0
spatnaOdpoved2 = 0

spravnaOdpovedText = font2.render(str(spravnaOdpoved), True, (255, 255, 255))
spatnaOdpovedText1 = font2.render(str(spatnaOdpoved1), True, (255, 255, 255))
spatnaOdpovedText2 = font2.render(str(spatnaOdpoved2), True, (255, 255, 255))

def vyberPrikladu():
    global hotovozInt, rozliseni, font1, font2, font3, font4, nadpis, vysledek, prikladuSpatne, prikladuDobre, hotovoz, screen, timeOut, vyberPozice, vyberVelikost, p, priklad, prikladText, spravnyVyber, spravnaOdpoved, spatnaOdpoved1, spatnaOdpoved2, spravnaOdpovedText, spatnaOdpovedText1, spatnaOdpovedText2
    
    if hotovozInt <= 10:
        
        spatnaOdpoved1 = 0
        priklad = random.choice(p)
        prikladText = font2.render(priklad, True, (0, 0, 0))

        castiPrikladu = priklad.strip().split(" ")
        prvniHodnota = int(castiPrikladu[0])
        druhaHodnota = int(castiPrikladu[2])

        if castiPrikladu[1] == "+":
            spravnaOdpoved = prvniHodnota + druhaHodnota
        if castiPrikladu[1] == "-":
            spravnaOdpoved = prvniHodnota - druhaHodnota
        if castiPrikladu[1] == "*":
            spravnaOdpoved = prvniHodnota * druhaHodnota
        if castiPrikladu[1] == ":":
            spravnaOdpoved = prvniHodnota // druhaHodnota
        spravnyVyber = random.choice(range(0, 2+1))

        for x in range(2):
            zmenaz = random.choice(["+", "-"])
            zmenac = random.randrange(1,7)
            if spatnaOdpoved1 == 0:
                if zmenaz == "+":
                    spatnaOdpoved1 = spravnaOdpoved + zmenac
                if zmenaz == "-":
                    spatnaOdpoved1 = spravnaOdpoved - zmenac
            else:
                if zmenaz == "+":
                    spatnaOdpoved2 = spravnaOdpoved + zmenac
                if zmenaz == "-":
                    spatnaOdpoved2 = spravnaOdpoved - zmenac
                
                if spatnaOdpoved2 == spatnaOdpoved1:
                    spatnaOdpoved2 += 1

        spravnaOdpovedText = font2.render(str(spravnaOdpoved), True, (255, 255, 255))
        spatnaOdpovedText1 = font2.render(str(spatnaOdpoved1), True, (255, 255, 255))
        spatnaOdpovedText2 = font2.render(str(spatnaOdpoved2), True, (255, 255, 255))

def pocitaniPrikladu():
    global hotovozInt, rozliseni, font1, font2, font3, font4, nadpis, vysledek, prikladuSpatne, prikladuDobre, hotovoz, screen, timeOut, vyberPozice, vyberVelikost, p, priklad, prikladText, spravnyVyber, spravnaOdpoved, spatnaOdpoved1, spatnaOdpoved2, spravnaOdpovedText, spatnaOdpovedText1, spatnaOdpovedText2
    vyberPrikladu()


    while True:
        stisknuto = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if stisknuto[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pygame.mouse.get_pos()[0] > vyberPozice[0] and pygame.mouse.get_pos()[0] < vyberPozice[0] + vyberVelikost[0] and pygame.mouse.get_pos()[1] > vyberPozice[1] and pygame.mouse.get_pos()[1] < vyberPozice[1] + vyberVelikost[1]:
                if timeOut == 0 and hotovozInt < 10:
                    if spravnyVyber == 0:
                        hotovozInt += 1
                        prikladuDobre += 1
                    else:
                        hotovozInt += 1
                        prikladuSpatne += 1
                        
                    hotovoz = font4.render(f"{hotovozInt}/10", True, (0, 0, 0))
                    timeOut = 500
                    vyberPrikladu()
            if pygame.mouse.get_pos()[0] > vyberPozice[0] + vyberVelikost[0]+20 and pygame.mouse.get_pos()[0] < vyberPozice[0] + vyberVelikost[0]+20 + vyberVelikost[0] and pygame.mouse.get_pos()[1] > vyberPozice[1] and pygame.mouse.get_pos()[1] < vyberPozice[1] + vyberVelikost[1]:
                if timeOut == 0 and hotovozInt < 10:
                    if spravnyVyber == 1:
                        hotovozInt += 1
                        prikladuDobre += 1
                    else:
                        hotovozInt += 1
                        prikladuSpatne += 1
                    
                    hotovoz = font4.render(f"{hotovozInt}/10", True, (0, 0, 0))
                    timeOut = 500
                    vyberPrikladu()
            if pygame.mouse.get_pos()[0] > vyberPozice[0] + vyberVelikost[0]*2+40 and pygame.mouse.get_pos()[0] < vyberPozice[0] + vyberVelikost[0]*2+40 + vyberVelikost[0] and pygame.mouse.get_pos()[1] > vyberPozice[1] and pygame.mouse.get_pos()[1] < vyberPozice[1] + vyberVelikost[1]:
                if timeOut == 0 and hotovozInt < 10:
                    if spravnyVyber == 2:
                        hotovozInt += 1
                        prikladuDobre += 1
                    else:
                        hotovozInt += 1
                        prikladuSpatne += 1
                    
                    hotovoz = font4.render(f"{hotovozInt}/10", True, (0, 0, 0))
                    timeOut = 300
                    vyberPrikladu()
            
        screen.fill((4, 75, 240))
        pygame.draw.rect(screen, (220, 220, 220), (8, 8, 170, 30))
        screen.blit(nadpis, (10, 10))
        pygame.draw.rect(screen, (95, 230, 0), (0, 100, 800, 250))
        screen.blit(prikladText, (rozliseni_x/2 - prikladText.get_rect().width/2, 100 + 250/2 - prikladText.get_rect().height/2))
        pygame.draw.rect(screen, (255, 146, 0), (vyberPozice[0], vyberPozice[1], vyberVelikost[0], vyberVelikost[1]))
        pygame.draw.rect(screen, (255, 146, 0), (vyberPozice[0] + vyberVelikost[0]+20, vyberPozice[1], vyberVelikost[0], vyberVelikost[1]))
        pygame.draw.rect(screen, (255, 146, 0), (vyberPozice[0] + vyberVelikost[0]*2+40, vyberPozice[1], vyberVelikost[0], vyberVelikost[1]))
        screen.blit(hotovoz, (rozliseni_x/2 - hotovoz.get_rect().width/2, 8 + 35))

        if spravnyVyber == 0:
            screen.blit(spravnaOdpovedText, (vyberPozice[0] + vyberVelikost[0]/2 - spravnaOdpovedText.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText1, ((vyberPozice[0] + vyberVelikost[0]+20) + vyberVelikost[0]/2 - spatnaOdpovedText1.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText2, ((vyberPozice[0] + vyberVelikost[0]*2+40) + vyberVelikost[0]/2 - spatnaOdpovedText2.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spravnaOdpovedText.get_rect().height/2))
        if spravnyVyber == 1:
            screen.blit(spatnaOdpovedText1, (vyberPozice[0] + vyberVelikost[0]/2 - spatnaOdpovedText1.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spatnaOdpovedText1.get_rect().height/2))
            screen.blit(spravnaOdpovedText, ((vyberPozice[0] + vyberVelikost[0]+20) + vyberVelikost[0]/2 - spravnaOdpovedText.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spravnaOdpovedText.get_rect().height/2))
            screen.blit(spatnaOdpovedText2, ((vyberPozice[0] + vyberVelikost[0]*2+40) + vyberVelikost[0]/2 - spatnaOdpovedText2.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spravnaOdpovedText.get_rect().height/2))
        if spravnyVyber == 2:
            screen.blit(spatnaOdpovedText1, (vyberPozice[0] + vyberVelikost[0]/2 - spatnaOdpovedText1.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spatnaOdpovedText1.get_rect().height/2))
            screen.blit(spatnaOdpovedText2, ((vyberPozice[0] + vyberVelikost[0]+20) + vyberVelikost[0]/2 - spatnaOdpovedText2.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spatnaOdpovedText2.get_rect().height/2))
            screen.blit(spravnaOdpovedText, ((vyberPozice[0] + vyberVelikost[0]*2+40) + vyberVelikost[0]/2 - spravnaOdpovedText.get_rect().width/2, vyberPozice[1] + vyberVelikost[1]/2 - spravnaOdpovedText.get_rect().height/2))

        if timeOut > 0:
            timeOut -= 1
        
        if hotovozInt >= 10:
            if prikladuDobre >= 9:
                return True
            else:
                return False
        
        pygame.display.update()
        
pocitaniPrikladu()