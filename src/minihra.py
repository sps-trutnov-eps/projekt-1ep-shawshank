import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
dialogue_font = pygame.font.SysFont("arial", 60)
dialogue = dialogue_font.render("                Spočítej příklady!                      ", True, (0, 0, 0))
dialogue2 = dialogue_font.render("                Příklad 1:                      ", True, (0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    screen.fill((195, 155, 119))
     
    screen.blit(dialogue, (40, 40))
     
    pygame.display.flip()
    