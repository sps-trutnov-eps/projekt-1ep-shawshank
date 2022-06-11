import os

#určení základních proměných + cesty k "projekt-1ep-shawshank"
path = os.path.join(os.getcwd(),"..","data","special_mistnosti")
list_of_screens = os.listdir(path)
    
screens_with_doors = []

#vytvoření seznamu obrazovek
for screen_ind,screen in enumerate(list_of_screens):
    new = []
    
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
    new = mapka
    
    screens_with_doors.append(new)
    #os.rename(path+"\\"+screen,f"{path}\\{binary}_{str(new[2][0])}({screen_ind}).tmx")
