import pygame
import sys
def cteni_dat_list(jmeno_souboru):
    soubor = open(jmeno_souboru, 'r', encoding = 'utf-8')
    data = []
    klice = soubor.readline()
    klice = klice[:-1].split(",")
    for radek in soubor:
        hodnota = radek[:-1].split(',')
        polozka = {}
        for i, klic in enumerate(klice):
            polozka[klic] = hodnota[i]
        else:
            data.append(polozka)
    soubor.close
    return data
def kontrola_kod(seznam,seznam2,typ):
    for polozka in seznam:
        if polozka[typ] == seznam2[typ]:
            return polozka
odpovedi = cteni_dat_list("odpovedi.csv")
otazky = cteni_dat_list("otazky.csv")
i_otazka = random.randint(0,(len(otazky) - 1))
otazka = otazky[i_otazka]
odpoved = kontrola_kod(odpovedi,otazka,"kod")
odpoved_kod = odpoved["kod"]
i_false_otazka = random.randint(0,(len(otazky) - 1))
false_odpoved = odpovedi[i_false_otazka]
while false_odpoved["kod"] == odpoved["kod"]:
    i_false_otazka = random.randint(0,(len(otazky) - 1))
    false_odpoved = odpovedi[i_false_otazka]
print(false_odpoved)
print(odpoved)

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
