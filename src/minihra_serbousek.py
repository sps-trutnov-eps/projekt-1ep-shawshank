import pygame
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.update()
pygame.display.set_caption("minihra")
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    color = (0,44,0)
    pygame.draw.rect(window, color, pygame.Rect(120, 120, 400, 240,))
    pygame.display.update()
pygame.quit()
quit()









        
    

