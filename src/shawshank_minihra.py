import pygame
import sys
import random
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
def datum_souradnice(text,font,x,y):
    datum = font.render(text, True, (0,0,0))
    datum_rect = datum.get_rect()
    datum_rect.center = (x,y)
    return datum, datum_rect
odpovedi = cteni_dat_list("odpovedi.csv")
otazky = cteni_dat_list("otazky.csv")
x1_center = x1 + (w_odp/2)
x2_center = x2 + (w_odp/2)
x3_center = x3 + (w_odp/2)
y_center = y_odp + (h_odp/2)
i_otazka = random.randint(0,(len(otazky) - 1))
otazka = otazky[i_otazka]
odpoved = kontrola_kod(odpovedi,otazka,"kod")
odpoved_kod = odpoved["kod"]
i_false_odpoved = random.randint(0,(len(otazky) - 1))
false_odpoved = odpovedi[i_false_odpoved]
i_false_odpoved_2 = random.randint(0,(len(otazky) - 1))
false_odpoved_2 = odpovedi[i_false_odpoved_2]
while false_odpoved["kod"] == odpoved["kod"]:
    i_false_otazka = random.randint(0,(len(otazky) - 1))
    false_odpoved = odpovedi[i_false_otazka]
print(false_odpoved)
while false_odpoved_2['kod'] == odpoved['kod'] or false_odpoved_2 == false_odpoved:
    i_false_odpoved_2 = random.randint(0,(len(otazky) - 1))
    false_odpoved_2 = odpovedi[i_false_odpoved_2]

rozliseni_okna = rozliseni_x, rozliseni_y = (1200,800)
pozadi_barva = (186, 140, 90)
lokace_1 = random.randint(0,2)
lokace_2 = random.randint(0,2)
lokace_3 = random.randint(0,2)

lokace_1 = random.randint(0,2)
lokace_2 = random.randint(0,2)
lokace_3 = random.randint(0,2)
w_odp = 100
x_pap = (rozliseni_x - w_pap) / 2
y_pap = (rozliseni_y - h_pap) / 2
x1 = (x_pap) + (w_odp/2)
x2 = ((x_pap + w_pap) / 2) + w_odp
x3 = (x_pap + w_pap) - (w_odp + w_odp / 2)
y_odp = y_pap * 24.16

    
pygame.init()
okno = pygame.display.set_mode(rozliseni_okna)

datum_1,datum_1_center = datum_souradnice(data[lokace_1],x1_center)
datum_2,datum_2_center = datum_souradnice(data[lokace_2],x2_center)
datum_3,datum_3_center = datum_souradnice(data[lokace_3],x3_center)
otazka,otazka_center = datum_souradnice(otazka,font_otazka,x_pap_center,y_pap_center)

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
    okno.blit(datum_1, datum_1_center)
    okno.blit(datum_2, datum_2_center)
    okno.blit(datum_3, datum_3_center)
    okno.blit(otazka, otazka_center)
    pygame.display.update()
