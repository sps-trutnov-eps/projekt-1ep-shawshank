import random,pygame,sys
pygame.init()
# základní proměnné
mapa = [
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],["111111","master"],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]]
       ]
chances = ["0","1","0"]
main_screenes = []
main_positions = []
master = [5,5]
screen = pygame.display.set_mode((len(mapa[0])*20,len(mapa)*12))
drawing_positions = {"0" : (4,0),
                     "1" : (12,0),
                     "2" : (16,4),
                     "3" : (12,8),
                     "4" : (4,8),
                     "5" : (0,4)}

#kreslení obrazovky na micromapu:
def draw_screen(obrazovka,pos):
    base = pygame.Surface((12,4))
    base.fill("white")
    pixel = pygame.Surface((4,4))
    pixel.fill("white")
    dot = pygame.Surface((4,4))
    dot.fill("lime")
    screen.blit(base,(pos[0]+4,pos[1]+4))
    for symbol_ind,symbol in enumerate(obrazovka[0]):
        if symbol == "1": screen.blit(pixel,(pos[0]+drawing_positions[str(symbol_ind)][0],pos[1]+drawing_positions[str(symbol_ind)][1]))
    if obrazovka[1]:
        screen.blit(dot,(pos[0]+8,pos[1]+4))
        if obrazovka[1] == "master":
            dot.fill("red")
            screen.blit(dot,(pos[0]+8,pos[1]+4))
        elif obrazovka[1] == "main":
            dot.fill("blue")
            screen.blit(dot,(pos[0]+8,pos[1]+4))

#hledání cesty    
def test(pos):
    new_pos = ["none","none"]
    if pos[0] > master[0]:
        new_pos[0] = "up"
    elif pos[0] < master[0]:
        new_pos[0] = "down"
    if pos[1] > master[1]:
        new_pos[1] = "left"
    elif pos[1] < master[1]:
        new_pos[1] = "right"
        
    if new_pos[0] != "none" and new_pos[1] != "none":
        new_pos[random.choice((0,1))] = "none"
    if new_pos[0] == "none":
        if new_pos[1] == "left":
            pos[1] -= 1
        else:
            pos[1] += 1
    else:
        if new_pos[0] == "up":
            pos[0] -= 1
        else:
            pos[0] += 1
    return pos,new_pos

#umištěňování obrazovek
def umisteni(pos,mapa,new_pos):
    state_of_door = False
    if mapa[pos[0]][pos[1]] != []:
        state_of_door = mapa[pos[0]][pos[1]][1]
    new_screen = [False,False,False,False,False,False]
    x = pos[1]
    y = pos[0]
    
    #určení možných vstupů/výstupů
    if y == 0:
        new_screen[0] = "0"
        new_screen[1] = "0"
    elif mapa[y-1][x] != []:
        new_screen[0] = mapa[y-1][x][0][4]
        new_screen[1] = mapa[y-1][x][0][3]
        
    if y == len(mapa)-1:
        new_screen[3] = "0"
        new_screen[4] = "0"
    elif mapa[y+1][x] != []:
        new_screen[4] = mapa[y+1][x][0][0]
        new_screen[3] = mapa[y+1][x][0][1]
        
    if x == 0:
        new_screen[5] = "0"
    elif mapa[y][x-1] != []:
        new_screen[5] = mapa[y][x-1][0][2]
        
    if x == len(mapa[0])-1:
        new_screen[2] = "0"
    elif mapa[y][x+1] != []:
        new_screen[2] = mapa[y][x+1][0][5]
        
    if "up" in new_pos: new_screen[random.choice((0,1))] = "1"
    elif "down" in new_pos: new_screen[random.choice((3,4))] = "1"
    elif "left" in new_pos: new_screen[5] = "1"
    elif "right" in new_pos: new_screen[2] = "1"
    real_new_screen = ""
    
    #vybrání tile
    for symbol in new_screen:
        if symbol: real_new_screen += symbol
        else: real_new_screen += random.choice(chances)
        
    mapa[y][x] = [real_new_screen,state_of_door]
    return mapa

#generace hlavních obrazovek
for x in range(3):
    chosen = ["""
            _            
           | |             
           | |             
           | |             
           | |             
           | |             
           | |             
           | |             
      _____| |_____        
     |_____ X _____|      
           | |             
           | |
           |_|            ""","main"]
    main_screenes.append(chosen) 
    
    pos = [random.randint(1,len(mapa[0])-1),random.randint(1,len(mapa)-1)]
    while master[0]+3 > pos[0] > master[0]-3 and master[1]+3 > pos[1] > master[1]-3:
        pos = [random.randint(1,len(mapa[0])-1),random.randint(1,len(mapa)-1)]
    main_positions.append(pos)
    mapa[pos[0]][pos[1]] = chosen

#generace mapy
for main_ind,main in enumerate(main_screenes):
    old_pos = [main_positions[main_ind][0],main_positions[main_ind][1]]
    pos = main_positions[main_ind]
    pos,new_pos = test(pos)
    mapa = umisteni(old_pos,mapa,new_pos)
    
    while new_pos != ["none","none"] and pos != master:
        old_pos = [pos[0],pos[1]]
        pos,new_pos = test(pos)
        mapa = umisteni(old_pos,mapa,new_pos)

#doplňování zbytku mapy
generate = True
while generate:
    generate = False
    for line_ind,line in enumerate(mapa):
        for part_ind,part in enumerate(line):
            variable = False
            if part == []:
                if line_ind != 0:
                    if mapa[line_ind-1][part_ind] != []:
                        if mapa[line_ind-1][part_ind][0][3] == "1" or mapa[line_ind-1][part_ind][0][4] == "1": variable = True
                if line_ind != len(mapa)-1:
                    if mapa[line_ind+1][part_ind] != []:
                        if mapa[line_ind+1][part_ind][0][0] == "1" or mapa[line_ind+1][part_ind][0][1] == "1": variable = True
                if part_ind != 0:
                    if mapa[line_ind][part_ind-1] != []:
                        if mapa[line_ind][part_ind-1][0][2] == "1": variable = True
                if part_ind != len(mapa[0])-1:
                    if mapa[line_ind][part_ind+1] != []:
                        if mapa[line_ind][part_ind+1][0][5] == "1": variable = True
                
                if variable:
                    mapa = umisteni([line_ind,part_ind],mapa,["none","none"])
                    generate = True
                    
#doplnění dveří dalším obrazovkám
seznam = []
for line_ind,line in enumerate(mapa):
    for part_ind,part in enumerate(line):
        if part != []:
            if not part[1]:
                seznam.append((line_ind,part_ind))
for x in range(len(seznam)//6):
    chosen_one = random.choice(seznam)
    mapa[chosen_one[0]][chosen_one[1]][1] = "regular_door"
    seznam.remove(chosen_one)
        
    
#vykreslování obrazovky
screen.fill("black")
for line_ind,line in enumerate(mapa):
    for part_ind,part in enumerate(line):
        if part != []: draw_screen(part,(part_ind*20,line_ind*12))
    
#main loop(vypnutí obrazovky)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()