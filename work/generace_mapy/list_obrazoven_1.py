import os

#určení základních proměných + cesty k "projekt-1ep-shawshank"
os.getcwd()
os.chdir("../")
os.chdir("../")
path = os.path.join(os.getcwd()+"\\data\\tiles")

list_of_screens = os.listdir(path)
screens_with_doors = []
screens_without_doors = []

#vytvoření seznamu oprazovek
for screen in list_of_screens:
    new = ["map","binary",["druh_dveří","sem_příjde_třída"],["prozatím_nepoužitá_kolonka_pro_bullyho"]]
    
    file = open(path+"\\"+screen,"r",encoding = "utf8")
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
    
    for line in mapka:
        pass