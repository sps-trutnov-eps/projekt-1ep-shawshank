import sys

#určení základních proměných + cesty k "projekt-1ep-shawshank"
obrazovky = []
index = 0
parent = sys.path[0]
parent = parent.split("\\work\\")[:-1]
if len(parent) > 1:
    new = parent[0]
    for entity in parent.remove(parent[0]):
        new.append("\\work\\"+entity)

#vytvoření seznamu oprazovek
while True:
    index += 1
    try:
        file = open(f"{parent[0]}\\data\\tiles\\tile{index}.tmx","r",encoding = "utf-8")
        obrazovka = file.read()
        file.close()
        
    except:
        break
    else:
        obrazovka = obrazovka.split("\n</data>")[0].split("<data encoding=\"csv\">\n")[1].split("\n")
        for line_ind,line in enumerate(obrazovka):
            splited = line.split(",")
            new = []
            for symbol in splited:
                if symbol != "":
                    new.append(symbol)
            obrazovka[line_ind] = new
            
        obrazovka_list = [obrazovka,[False,False,False,False,False,False],
                          [False,"sem_příjde_třída"],["prozatím_nepoužitá_kolonka_pro_bullyho"]]
        
        if obrazovka[0][15] == "5":
            obrazovka_list[1][1]=True
        if obrazovka[0][6] == "5":
            obrazovka_list[1][0]=True
        if obrazovka[6][-1] == "5":
            obrazovka_list[1][2]=True
        if obrazovka[6][0] == "5":
            obrazovka_list[1][5]=True
        if obrazovka[-1][15] == "5":
            obrazovka_list[1][3]=True
        if obrazovka[-1][6] == "5":
            obrazovka_list[1][4]=True
            
        obrazovky.append(obrazovka_list)

print(obrazovky[1])