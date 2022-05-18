import pygame,random,sys
pygame.init()

class obsticle(pygame.sprite.Sprite):
    def __init__(self,pos,w,h,floor):
        super().__init__()
        self.image = pygame.Surface((w,h))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (pos-64,floor)
        
def create(amount):
    line = "_____"
    for number in range(amount):
        line += "O"
        for s in range(random.randint(2,3)): line += "_"
    return line

def The_game():
    #základní veličiny
    width,heigth = 23*32,14*32
    screen = pygame.display.set_mode((width,heigth))
    clock = pygame.time.Clock()
    speed = 10
    gravity = 0
    floor = heigth-128
    game_state = "play_one"
    lives = 3
    end_countdown = 20
    invurnability = 0
    jump_timeout = 0
    jump_timeout_base = 38
    
    win_image = pygame.Surface((64,64))
    win_image.fill("gold")
    win_rect = win_image.get_rect()
    
    play_line = create(19)
    play_line += "EEEEW"
    
    player_texture = pygame.Surface((32,64))
    player_texture.fill("cyan")
    player_rect = player_texture.get_rect()
    player_rect.midbottom = (width-128,floor)
    info_font = pygame.font.SysFont("Courier New",30)
    info_text = info_font.render("Press ||SPACE|| to jump.",False,"green")
    lives_indicator = info_font.render(f"{lives} × <3",False,"red")
    
    obsticles = pygame.sprite.Group()
    waiting = pygame.sprite.Group()
    for symbol_ind,symbol in enumerate(play_line):
        if symbol == "O": obsticles.add(obsticle(-symbol_ind*64,32,64,floor))
        elif symbol == "E": waiting.add(obsticle(-symbol_ind*64,70,600,floor))
        elif symbol == "W": win_rect.center = (-symbol_ind*64,floor-32)

    while True:
        #vypnutí
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pressed[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
        
        #první kolo hry
        if game_state == "play_one":
            #pohyb
            jump = True
            for instance in waiting:
                if player_rect.colliderect(instance.rect):
                    jump = False
            
            if pressed[pygame.K_SPACE] and player_rect.bottom == floor and jump and jump_timeout < 0:
                gravity = 18
                jump_timeout = jump_timeout_base
            jump_timeout -=1
            gravity -= 1
            player_rect.y -= gravity
            if player_rect.bottom > floor: player_rect.bottom = floor
            
            if win_rect.center[0] < player_rect.center[0]:
                for thing in obsticles,waiting:
                    for instance in thing: instance.rect.x += 5
                win_rect.x += 5
            else:
                pygame.time.wait(333)
                game_state = "midstage"
        
            #draw
            screen.fill("black")
            screen.blit(win_image,win_rect)
            obsticles.draw(screen)
            screen.blit(win_image,win_rect)
            screen.blit(info_text,(32,32))
            screen.blit(lives_indicator,(32,96))
            screen.blit(player_texture,player_rect)
            
            #životy
            invurnability -= 1
            if invurnability < 0:
                for instance in obsticles:
                    if instance.rect.colliderect(player_rect):
                        lives -= 1
                        lives_indicator = info_font.render(f"{lives} × <3",False,"red")
                        invurnability = 50
                        if lives == 0:
                            pygame.time.wait(333)
                            game_state = "bad_ending"
            
        #stage between rounds
        elif game_state == "midstage":
            #přenastavení proměnných
            end_countdown = 20
            game_state = "play_two"
            play_line = create(25)
            play_line += "EEEEW"
            obsticles = pygame.sprite.Group()
            waiting = pygame.sprite.Group()
            for symbol_ind,symbol in enumerate(play_line):
                if symbol == "O": obsticles.add(obsticle(width+symbol_ind*64,32,64,floor))
                elif symbol == "E": waiting.add(obsticle(width+symbol_ind*64,70,600,floor))
                elif symbol == "W": win_rect.center = (width+symbol_ind*64,floor-32)
            player_rect.midbottom = (128,floor)
            jump_timeout_base = 40
            info_text = info_font.render("Press ||SEMICOLON|| to secret.",False,"green")
        
        #druhé kolo hry
        elif game_state == "play_two":
            
            #"secret"
            if pressed[pygame.K_SEMICOLON]:
                pygame.time.wait(666)
                game_state = "ˇ-ˇ"
                
            
            #pohyb
            jump = True
            for instance in waiting:
                if player_rect.colliderect(instance.rect):
                    jump = False
            
            if pressed[pygame.K_SPACE] and player_rect.bottom == floor and jump and jump_timeout < 0:
                gravity = 20
                jump_timeout = jump_timeout_base
            jump_timeout -= 1
            gravity -= 1
            player_rect.y -= gravity
            if player_rect.bottom > floor: player_rect.bottom = floor
            
            if win_rect.center[0] > player_rect.center[0]:
                for thing in obsticles,waiting:
                    for instance in thing: instance.rect.x -= 5
                win_rect.x -= 5
            else:
                pygame.time.wait(333)
                game_state = "ˇ-ˇ"
            
            #životy
            invurnability -= 1
            if invurnability < 0:
                for instance in obsticles:
                    if instance.rect.colliderect(player_rect):
                        lives -= 1
                        lives_indicator = info_font.render(f"{lives} × <3",False,"red")
                        invurnability = 50
                        if lives == 0:
                            pygame.time.wait(333)
                            game_state = "bad_ending"
                    
        
            #draw
            screen.fill("black")
            screen.blit(win_image,win_rect)
            obsticles.draw(screen)
            screen.blit(win_image,win_rect)
            screen.blit(info_text,(32,32))
            screen.blit(lives_indicator,(32,96))
            screen.blit(player_texture,player_rect)
        
        #prohra
        elif game_state == "bad_ending":
            return(False)
        #konec
        else:
            return(True)
            
        pygame.display.update()
        clock.tick(60)
        
print(The_game())
pygame.quit()
sys.exit()