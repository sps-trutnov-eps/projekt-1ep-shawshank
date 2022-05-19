import pygame,random,sys
pygame.init()

class obsticle(pygame.sprite.Sprite):
    def __init__(self,pos,w,h,floor,texture):
        super().__init__()
        self.image = texture
        self.rect = pygame.Rect(0,0,w,h) 
        self.rect.midbottom = (pos-64,floor)
        
def create(amount):
    line = "_____"
    for number in range(amount):
        line += "O"
        for s in range(random.randint(2,3)): line += "_"
    return line

def speak(text,pos,screen):
    font = pygame.font.SysFont("Courier New",17)
    writing = ""
    for symbol in text:
        writing += symbol
        screen.blit(font.render(writing,False,"black"),(pos[0]+20,pos[1]+20))
        pygame.display.update()
        pygame.time.wait(100)
        
class speaker_class():
    def __init__(self,screen):
        self.screen = screen
        self.bc0 = pygame.image.load("../data/textury_hry/I_touched_grass.jpg")
        self.textbox = pygame.Surface((620,100))
        self.textbox.fill("limegreen")
        extra_surface = pygame.Surface((600,90))
        extra_surface.fill("olivedrab2")
        self.textbox.blit(extra_surface,(10,10))
        self.textbox_rect = self.textbox.get_rect()
        self.textbox_rect.midbottom = (23*16,14*32)
        self.progress = 0
    def next(self):
        self.progress += 1
        if self.progress == 1:
            self.screen.blit(self.bc0,(0,0))
            pygame.display.update()
            pygame.time.wait(500)
            self.screen.blit(self.textbox,self.textbox_rect)
            speak("!!jhk,n.cmlcfkl,hmfhvfgmnvngf!!",self.textbox_rect.topleft,self.screen)
            return(False)
        elif self.progress == 2:
            self.screen.blit(self.bc0,(0,0))
            self.screen.blit(self.textbox,self.textbox_rect)
            speak("!!testing_testing!!",self.textbox_rect.topleft,self.screen)
            return(False)
        elif self.progress == 3:
            self.screen.blit(self.bc0,(0,0))
            self.screen.blit(self.textbox,self.textbox_rect)
            speak("toto je další text",self.textbox_rect.topleft,self.screen)
            return(False)
        elif self.progress == 4:
            self.screen.blit(self.bc0,(0,0))
            self.screen.blit(self.textbox,self.textbox_rect)
            speak("nyní hra započne",self.textbox_rect.topleft,self.screen)
            return(False)
        elif self.progress == 5:
            return(True)
            
            

def The_game():
    #základní proměnné
    
    width,heigth = 23*32,14*32
    screen = pygame.display.set_mode((width,heigth))
    clock = pygame.time.Clock()
    speed = 10
    gravity = 0
    floor = heigth-128
    game_state = "intro"
    lives = 3
    end_countdown = 20
    invurnability = 0
    jump_timeout = 0
    jump_timeout_base = 38
    speaker = speaker_class(screen)
    over = True
    space_fix = True
    
    grass = pygame.transform.rotozoom(pygame.image.load("../data/textury_hry/I_touched_grass.jpg").convert(),90,0.5).convert()
    grass_rect = grass.get_rect()
    grass_rect.bottomright = (width,heigth)
    grass_fliped = pygame.transform.flip(grass,True,False).convert()
    grass_fliped_rect = grass_fliped.get_rect()
    grass_fliped_rect.bottomright = grass_rect.bottomleft
    
    player_sheet = pygame.transform.scale2x(pygame.image.load("../data/textury_hrac/Player_sprite.png")).convert()
    
    t_0 = pygame.image.load("../data/textury_hry/kvetinka.png").convert_alpha()
    t_1 = pygame.image.load("../data/textury_hry/not_spon.png").convert_alpha()
    t_2 = pygame.image.load("../data/textury_hry/vosäk.png").convert_alpha()
    texture_mix_1 = (t_0,t_1,t_2)
    texture_mix_2 = (t_0,t_1,pygame.transform.flip(t_2,True,False).convert_alpha())
    
    
    win_image = pygame.image.load("../data/textury_hry/křída.png").convert_alpha()
    win_rect = win_image.get_rect()
    
    play_line = create(19)
    play_line += "EEEEW"
    
    player_texture = pygame.Surface((32,64))
    player_texture.set_colorkey("black")
    player_rect = player_texture.get_rect()
    player_texture_ind = 2
    player_texture_countdown = 1
    player_rect.midbottom = (width-128,floor)
    player_jump_texture = pygame.Surface((32,64))
    player_jump_texture.set_colorkey("black")
    player_jump_texture.blit(player_sheet,(-160,-64))
    info_font = pygame.font.SysFont("Courier New",30)
    info_text = info_font.render("Press ||SPACE|| to jump.",False,"green")
    lives_indicator = info_font.render(f"{lives} × <3",False,"red")
    
    obsticles = pygame.sprite.Group()
    waiting = pygame.sprite.Group()
    for symbol_ind,symbol in enumerate(play_line):
        if symbol == "O": obsticles.add(obsticle(-symbol_ind*64,32,64,floor,random.choice(texture_mix_1)))
        elif symbol == "E": waiting.add(obsticle(-symbol_ind*64,70,600,floor,random.choice(texture_mix_1)))
        elif symbol == "W":
            waiting.add(obsticle(-symbol_ind*64,70,600,floor,random.choice(texture_mix_1)))
            win_rect.center = (-symbol_ind*64,floor-32)

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
        
        #počátek
        if game_state == "intro":
            if over:
                over = False
                over = speaker.next()
                
            if pressed[pygame.K_SPACE] or pressed[pygame.K_RETURN] or pressed[pygame.K_KP_ENTER]:
                if space_fix:
                    over = speaker.next()
                    space_fix = False
                else: space_fix = True
                
            if over:
                pygame.time.wait(500)
                game_state = "play_one"
        
        #první kolo hry
        elif game_state == "play_one":
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
            
            if win_rect.right+20 < player_rect.left:
                for thing in obsticles,waiting:
                    for instance in thing: instance.rect.x += 5
                win_rect.x += 5
                grass_rect.x += 5
                grass_fliped_rect.x += 5
            else:
                pygame.time.wait(1000)
                game_state = "midstage"
                
            #textury
            if grass_rect.left > width: grass_rect.right = grass_fliped_rect.left-1
            elif grass_fliped_rect.left > width: grass_fliped_rect.right = grass_rect.left-1
            
            player_texture_countdown -=1
            if player_texture_countdown == 0:
                player_texture.blit(player_sheet,(-player_texture_ind*32,-64))
                player_texture_countdown = 4
                player_texture_ind += 1
                if player_texture_ind == 9: player_texture_ind = 0
        
            #draw
            screen.fill("black")
            screen.blit(grass,grass_rect)
            screen.blit(grass_fliped,grass_fliped_rect)
            screen.blit(win_image,win_rect)
            obsticles.draw(screen)
            screen.blit(win_image,win_rect)
            screen.blit(info_text,(32,32))
            screen.blit(lives_indicator,(32,96))
            if player_rect.bottom == floor: screen.blit(player_texture,player_rect)
            else: screen.blit(player_jump_texture,player_rect)
            
            #životy
            invurnability -= 1
            if invurnability < 0:
                for instance in obsticles:
                    if instance.rect.colliderect(player_rect):
                        lives -= 1
                        lives_indicator = info_font.render(f"{lives} × <3",False,"red")
                        invurnability = 50
                        if lives == 0:
                            pygame.time.wait(1000)
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
                if symbol == "O": obsticles.add(obsticle(width+symbol_ind*64,32,64,floor,random.choice(texture_mix_2)))
                elif symbol == "E": waiting.add(obsticle(width+symbol_ind*64,70,600,floor,random.choice(texture_mix_2)))
                elif symbol == "W":
                    waiting.add(obsticle(width+symbol_ind*64,70,600,floor,random.choice(texture_mix_2)))
                    win_rect.center = (width+symbol_ind*64,floor-32)
            player_rect.midbottom = (128,floor)
            jump_timeout_base = 40
            win_image = pygame.image.load("../data/textury_hry/cil.png").convert_alpha()
            info_text = info_font.render("Press ||SEMICOLON|| to secret.",False,"green")
            player_jump_texture.blit(player_sheet,(-160,0))
        
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
                grass_rect.x -= 5
                grass_fliped_rect.x -= 5
            else:
                pygame.time.wait(1000)
                game_state = "ˇ-ˇ"
                
            #textury
            if grass_rect.right < 0: grass_rect.left = grass_fliped_rect.right+1
            elif grass_fliped_rect.right < 0: grass_fliped_rect.left = grass_rect.right+1
            
            player_texture_countdown -=1
            if player_texture_countdown == 0:
                player_texture.blit(player_sheet,(-player_texture_ind*32,0))
                player_texture_countdown = 4
                player_texture_ind += 1
                if player_texture_ind == 9: player_texture_ind = 0
            
            #životy
            invurnability -= 1
            if invurnability < 0:
                for instance in obsticles:
                    if instance.rect.colliderect(player_rect):
                        lives -= 1
                        lives_indicator = info_font.render(f"{lives} × <3",False,"red")
                        invurnability = 50
                        if lives == 0:
                            pygame.time.wait(1000)
                            game_state = "bad_ending"
                    
        
            #draw
            screen.blit(grass,grass_rect)
            screen.blit(grass_fliped,grass_fliped_rect)
            screen.blit(win_image,win_rect)
            obsticles.draw(screen)
            screen.blit(win_image,win_rect)
            screen.blit(info_text,(32,32))
            screen.blit(lives_indicator,(32,96))
            if player_rect.bottom == floor: screen.blit(player_texture,player_rect)
            else: screen.blit(player_jump_texture,player_rect)
        
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