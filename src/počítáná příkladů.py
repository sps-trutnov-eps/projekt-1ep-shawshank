import random
import pygame
import sys

pygame.init()

rozliseni = rozliseni_x, rozliseni_y = (800, 600)
font1 = pygame.font.SysFont ("Arial", 20)
font2 = pygame.font.SysFont("Calibri", 40)
nadpis = font1.render("Vypočítej tenty příklady:", True, (0, 0, 0))
vysledek = font1.render("Výsledek: ", True, (0, 0, 0))
screen = pygame.display.set_mode((rozliseni_x, rozliseni_y))
pygame.display.set_caption('Počítání příkladů')



o1 = random.randrange(1, 5)
if o1 == 1:
    p = ("12 + 14 = ")
    priklad = font2.render(p, True, (0, 0, 0))
elif o1 == 2:        
    p = ("43 + 23 = ")
    priklad = font2.render(p, True, (0, 0, 0))
elif o1 == 3: 
    p = ("46 - 28 = ")
    priklad = font2.render(p, True, (0, 0, 0))
elif o1 == 4: 
    p = ("27 - 8 = ")
    priklad = font2.render(p, True, (0, 0, 0))
elif o1 == 5: 
    p = ("5 * 7 = ")
    priklad = font2.render(p, True, (0, 0, 0))
o2 = random.randrange(1, 5)
if o2 == 1:
    p2 = ("38 + 52 = ")
    priklad2 = font2.render(p2, True, (0, 0, 0))
elif o2 == 2:        
    p2 = ("73 - 49 = ")
    priklad2 = font2.render(p2, True, (0, 0, 0))
elif o2 == 3: 
    p2 = ("12 * 5 = ")
    priklad2= font2.render(p2, True, (0, 0, 0))
elif o2 == 4: 
    p2 = ("42 - 24 = ")
    priklad2 = font2.render(p2, True, (0, 0, 0))
elif o2 == 5: 
    p2 = ("42 / 6 = ")
    priklad2 = font2.render(p2, True, (0, 0, 0))

print(p)
v = input("Výsledek: ")
if o1 == 1:
    if v == "26":
        print("Správně")
    else:
        print("Špatně")
        print("Správná odpověď je 26")
if o1 == 2:
    if v == "68":
        print("Správně")
    else:
        print("Špatně")
        print("Správná odpověď je 68")
if o1 == 3:
    if v == "18":
        print("Správně")
    else:
        print("Špatně")
        print("Správná odpověď je 18")
if o1 == 4:
    if v == "19":
        print("Správně")
    else:
        print("Špatně")
        print("Správná odpověď je 19")
if o1 == 5:
    if v == "35":
        print("Správně")
    else:
        print("Špatně")
        print("Správná odpověď je 35")
print(p2)
v2 = input("Výsledek: ")
if o2 == 1:
    if v2 == "90":
        print("Správně")
    else:
        print("Špatně")
elif o2 == 2:        
    if v2 == "24":
        print("Správně")
    else:
        print("Špatně")
elif o2 == 3: 
    if v2 == "60":
        print("Správně")
    else:
        print("Špatně")
elif o2 == 4: 
    if v2 == "18":
        print("Správně")
    else:
        print("Špatně")
elif o2 == 5: 
    if v2 == "7":
        print("Správně")
    else:
        print("Špatně")


while True:
    stisknuto = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if stisknuto[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        
    screen.fill((255, 255, 255))
    screen.blit(nadpis, (20, 20))
    screen.blit(priklad, (20, 50 ))
    screen.blit(priklad2, (20, 90 ))
    


    pygame.display.update()




    
    

