import os

#určení základních proměných + cesty k "projekt-1ep-shawshank"
path = os.path.join(os.getcwd(),"data","tiles")
list_of_screens = os.listdir(path)
    
screens_with_doors = []
screens_without_doors = []

#vytvoření seznamu obrazovek
for screen_ind,screen in enumerate(list_of_screens):
    new = ["map","binary",[None,"sem_příjde_třída"],["prozatím_nepoužitá_kolonka_pro_bullyho"]]
    
    #mapka
    try:
        file = open(path+"\\"+screen,"r",encoding = "utf8")
    except:
        file = open(path+"/"+screen,"r",encoding = "utf8")
    mapka = file.read()
    file.close()
    mapka = mapka.split("\n</data>")[0].split("<data encoding=\"csv\">\n")[1].split("\n")
    for line_ind,line in enumerate(mapka):
        splited = line.split(",")
        new_line = []
        for symbol in splited:
            if symbol != "":
                new_line.append(symbol)
        mapka[line_ind] = new_line
    new[0] = mapka
    
    #dveře
    for line in mapka:
        if "1" in line or "2" in line or "3" in line or "4" in line:
            new[2][0] = True
    
    #průchody
    binary = ""
    if mapka[0][6] == "5": binary += "1"
    else: binary += "0"
    if mapka[0][15] == "5": binary += "1"
    else: binary += "0"
    if mapka[6][-1] == "5": binary += "1"
    else: binary += "0"
    if mapka[-1][15] == "5": binary += "1"
    else: binary += "0"
    if mapka[-1][6] == "5": binary += "1"
    else: binary += "0"
    if mapka[6][0] == "5": binary += "1"
    else: binary += "0"
    
    new[1] = binary
    
    if new[2][0]: screens_with_doors.append(new)
    else: screens_without_doors.append(new)
    #os.rename(path+"\\"+screen,f"{path}\\{binary}_{str(new[2][0])}({screen_ind}).tmx")
