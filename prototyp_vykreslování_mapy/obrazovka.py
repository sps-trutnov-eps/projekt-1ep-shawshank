import pygame

pygame.init()

screen = pygame.display.set_mode((100,100))

images = (pygame.image.load("textury_hry/proto-dveře_v1_0.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-dveře_v1_1.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-dveře_v1_2.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-dveře_v1_3.png").convert_alpha(),
          
          pygame.image.load("textury_hry/proto-podlaha.png").convert_alpha(),
          
          pygame.image.load("textury_hry/proto-zeď_v1_0.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_1.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_2.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_3.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_4.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_5.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_6.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_7.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_8.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_9.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_10.png").convert_alpha(),
          pygame.image.load("textury_hry/proto-zeď_v1_11.png").convert_alpha(),
          
          pygame.image.load("textury_hry/void.png").convert_alpha(),)

mapa = ((17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,15,0,6,17,14,4,4,8,17,17,17,17,17),
        (5,5,5,5,5,16,4,4,7,5,16,4,7,5,16,4,4,7,5,5,5,5,5),
        (4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4),
        (4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4),
        (11,11,11,11,11,13,4,4,10,11,11,11,11,11,13,4,4,10,11,11,11,11,11),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17),
        (17,17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17,17))

mapa_2 = ((17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17),
        (17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17),
        (17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17),
        (17,17,17,17,14,4,4,8,17,15,0,6,17,14,4,4,8,17,17,17,17),
        (5,5,5,5,16,4,4,7,5,16,4,7,5,16,4,4,7,5,5,5,5),
        (4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4),
        (4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4),
        (11,11,11,11,13,4,4,10,11,11,11,11,11,13,4,4,10,11,11,11,11),
        (17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17),
        (17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17),
        (17,17,17,17,14,4,4,8,17,17,17,17,17,14,4,4,8,17,17,17,17),)


def normal():
    # 23x14
    global screen
    screen = pygame.display.set_mode((len(mapa[0])*32,len(mapa)*32))
    for line_ind,line in enumerate(mapa):
        for symbol_ind,symbol in enumerate(line):
            screen.blit(images[symbol],(symbol_ind*32,line_ind*32))
            
def more():
    # 23x14 ale větší
    global screen
    screen = pygame.display.set_mode((len(mapa[0])*64,len(mapa)*64))
    for line_ind,line in enumerate(mapa):
        for symbol_ind,symbol in enumerate(line):
            screen.blit(pygame.transform.scale2x(images[symbol]),(symbol_ind*64,line_ind*64))  

def more_minus():
    # seříznuto o 1 na každé straně => 21x12
    global screen
    screen = pygame.display.set_mode((len(mapa_2[0])*64,len(mapa_2)*64))
    for line_ind,line in enumerate(mapa_2):
        for symbol_ind,symbol in enumerate(line):
            screen.blit(pygame.transform.scale2x(images[symbol]),(symbol_ind*64,line_ind*64))

normal()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_KP1]:
        normal()
    if keys[pygame.K_KP2]:
        more()
    if keys[pygame.K_KP3]:
        more_minus()
        

    pygame.display.update()