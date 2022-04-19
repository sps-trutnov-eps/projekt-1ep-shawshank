import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
dialogue_font = pygame.font.SysFont("arial", 60)
dialogue = dialogue_font.render("Matematika začíná!", True, (255, 50, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    screen.fill((255, 255, 255))
     
    screen.blit(dialogue, (40, 40))
     
    pygame.display.flip()
    