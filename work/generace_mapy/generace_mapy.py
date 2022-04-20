import random
# základní proměnné
data = []
mapa = [
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[],[]]
       ]
main_screenes = []
main_positions = []

#generace soupisu čísel (prozatimní)
for number in range(64):
    dat = bin(number).split("b")[1]
    if len(dat) != 6:
        for x in range(6 - len(dat)):
            dat = "0"+dat
    
    data.append([dat, False])

#generace hlavních obrazovek
for x in range(3):
    chosen = random.choice(data)
    chosen[1] = True
    main_screenes.append(chosen) 
    
    pos = (random.randint(0,len(mapa[0])-1),random.randint(0,len(mapa)-1))
    main_positions.append(pos)
    print()
    mapa[pos[0]][pos[1]] = chosen
    
print(mapa)
    

    