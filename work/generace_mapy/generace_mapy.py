import random
# základní proměnné
data = []
mapa = [
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],["111111",True],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[],[]]
       ]
main_screenes = []
main_positions = []
master = [5,5]

#hledání cesty    
def test(pos,new_pos):
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
    new_screen = [False,False,False,False,False,False]
    x = pos[1]
    y = pos[0]
    data_fc = []
    for dat in data:
        data_fc.append(dat)
    
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
        
    #print(new_screen,new_pos)
    real_new_screen = ""
    #vybrání tile
    for symbol in new_screen:
        if symbol: real_new_screen += symbol
        else: real_new_screen += random.choice(("0","1"))
        
    mapa[y][x] = [real_new_screen,False]
    return mapa

#generace soupisu čísel (prozatimní)
for number in range(64):
    dat = bin(number).split("b")[1]
    if len(dat) != 6:
        for x in range(6 - len(dat)):
            dat = "0"+dat
    
    data.append([dat, False])

#generace hlavních obrazovek
for x in range(1):
    chosen = random.choice(data)
    chosen[1] = True
    main_screenes.append(chosen) 
    
    pos = [random.randint(1,len(mapa[0])-1),random.randint(1,len(mapa)-1)]
    while 8 > pos[0] > 2 and 8 > pos[1] > 2:
        pos = [random.randint(1,len(mapa[0])-1),random.randint(1,len(mapa)-1)]
    main_positions.append(pos)
    mapa[pos[0]][pos[1]] = chosen

#generace mapy
for main_ind,main in enumerate(main_screenes):
    pos = main_positions[main_ind]
    pos,new_pos = test(pos,["none","none"])
    
    while new_pos != ["none","none"] and pos != master:
        old_pos = [pos[0],pos[1]]
        pos,new_pos = test(pos,["none","none"])
        mapa = umisteni(old_pos,mapa,new_pos)

print("\n::::mapa::::")
for line in mapa:
    print(line)