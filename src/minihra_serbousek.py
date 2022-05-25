import pygame
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.update()
pygame.display.set_caption("Šibenice")
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    color = (0,44,0)
    white = (255, 255, 255)
    X = 640
    Y = 480
    display_surface = pygame.display.set_mode((X, Y))
    window.fill(color)
    font = pygame.font.SysFont('forte', 26)
    text = font.render("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", True, white)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 1.05)
    while True:
        display_surface.fill
        display_surface.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        
        
                     
    
    
    










        
    

