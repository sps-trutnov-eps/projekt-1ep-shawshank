import random

rnd = (random.randint(1,2))

if rnd == 1:
    x = (0)
    y = (10)
    for z in range(x, y+1):
        if z>1:
            for i in range(2, z):
                if(z%i) ==0:
                    break
            else:
                print(z)
                
elif rnd == 2:
    x = (10)
    y = (20)
    for z in range(x, y+1):
        if z>1:
            for i in range(2, z):
                if(z%i) ==0:
                    break
            else:
                print(z)
            