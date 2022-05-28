import pygame
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.update()
pygame.display.set_caption("Šibenice")
game_over = False
abeceda = [
    {"znak": "A", "stav": True},
    {"znak": "B", "stav": True},
    {"znak": "C", "stav": False},
    {"znak": "D", "stav": True},
    {"znak": "E", "stav": True},
    {"znak": "F", "stav": True},
    {"znak": "G", "stav": False},
    {"znak": "H", "stav": False},
    {"znak": "I", "stav": False},
    {"znak": "J", "stav": True},
    {"znak": "K", "stav": True},
    {"znak": "L", "stav": False},
    {"znak": "M", "stav": True},
    {"znak": "N", "stav": True},
    {"znak": "O", "stav": True},
    {"znak": "P", "stav": True},
    {"znak": "Q", "stav": False},
    {"znak": "R", "stav": True},
    {"znak": "S", "stav": True},
    {"znak": "T", "stav": True},
    {"znak": "U", "stav": True},
    {"znak": "V", "stav": True},
    {"znak": "W", "stav": True},
    {"znak": "X", "stav": True},
    {"znak": "Y", "stav": True},
    {"znak": "Z", "stav": True}
    ]
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            quit()
    color = (0,44,0)
    white = (255, 255, 255)
    X = 640
    Y = 480
    window.fill(color)
    font = pygame.font.SysFont('forte', 26)
    odsazeni = 10
    for pismeno in abeceda:
        if pismeno["stav"] == True:
            text = font.render(pismeno["znak"],True,white)
        elif pismeno["stav"] == False:
            text = font.render("_",True,white)
        textRect = text.get_rect()
        rozmery_pismene = font.size(pismeno["znak"])
        textRect.center = (rozmery_pismene[0]//2 + odsazeni, Y // 1.05)
        window.blit(text, textRect)
        odsazeni += rozmery_pismene[0] + 7.5
    pygame.display.update() 