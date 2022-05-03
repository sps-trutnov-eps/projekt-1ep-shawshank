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
        
def kontrola_random(rand3,status,min,max):
    rand1 = random.randint(min,max)
    rand2 = random.randint(min,max)
    if status == 1:
        rand3 = random.randint(min,max)
    while rand1 == rand2 or rand1 == rand3 or rand2 == rand3:
        rand1 = random.randint(min,max)
        rand2 = random.randint(min,max)
        if status == 1:
            rand3 = random.randint(min,max)
    if status == 1:
        return rand1,rand2,rand3
    else:
        return rand1,rand2
        
    
    
odpovedi = cteni_dat_list("odpovedi.csv")
otazky = cteni_dat_list("otazky.csv")

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

x1_center = x1 + (w_odp/2)
x2_center = x2 + (w_odp/2)
x3_center = x3 + (w_odp/2)
y_center = y_odp + (h_odp/2)

x_pap_center = x_pap + (w_pap/2)
y_pap_center = y_pap + (h_pap/2)

vybrana_odpoved = ''
a = 0
       
pygame.init()

font_odpoved = pygame.font.SysFont(None, 25)
font_otazka = pygame.font.SysFont(None, 50)
okno = pygame.display.set_mode(rozliseni_okna)

je_otazka = "false"
pokus = 0
while True:
    udalosti = pygame.event.get()
    stisknuto = pygame.key.get_pressed()
    m_x,m_y = pygame.mouse.get_pos()
    
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if u.type == pygame.KEYDOWN:
            if u.key == pygame.K_k:
                if y_odp < m_y < y_odp + h_odp and x1 < m_x < x1 + w_odp:
                    vybrana_odpoved = data[lokace_1]
                    a = 1
                    pokus += 1
                    je_otazka = 'false'
                elif y_odp < m_y < y_odp + h_odp and x2 < m_x < x2 + w_odp:
                    vybrana_odpoved = data[lokace_2]
                    a = 1
                    pokus += 1
                    je_otazka = 'false'
                elif y_odp < m_y < y_odp + h_odp and x3 < m_x < x3 + w_odp:
                    vybrana_odpoved = data[lokace_3]
                    a = 1
                    pokus += 1
                    je_otazka = 'false'
                
    
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if pokus < 5 and je_otazka == "false":
        i_otazka = random.randint(0,(len(otazky) - 1))
        otazka = otazky[i_otazka]
        odpoved = kontrola_kod(odpovedi,otazka,"kod")
        otazka = otazka['udalost']
        #tvorba spatnych odpovedi
        i_false_odpoved1,i_false_odpoved2 = kontrola_random((int(odpoved["kod"])-1),0,0,len(otazky)-1)
        false_odpoved = odpovedi[i_false_odpoved1]
        false_odpoved2 = odpovedi[i_false_odpoved2]
        print(odpoved,false_odpoved,false_odpoved2)
        #tvorba datumu pro odpovedi
        datum = odpoved['datum']
        false_datum = false_odpoved["datum"]
        false_datum_2 = false_odpoved2["datum"]
        data = [datum, false_datum, false_datum_2]
        #zadani lokaci pro odpovedi
        lokace_1,lokace_2,lokace_3 = kontrola_random("",1,0,2)
        datum_1,datum_1_center = datum_souradnice(data[lokace_1],font_odpoved,x1_center,y_center)
        datum_2,datum_2_center = datum_souradnice(data[lokace_2],font_odpoved,x2_center,y_center)
        datum_3,datum_3_center = datum_souradnice(data[lokace_3],font_odpoved,x3_center,y_center)
        otazka,otazka_center = datum_souradnice(otazka,font_otazka,x_pap_center,y_pap_center)
        je_otazka = "true"
        
    

    if a == 1:        
        if vybrana_odpoved == odpoved['datum']:
            print('spravne')
        else:
            print('spatne')
        a = 0
    
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