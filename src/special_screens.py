import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

import os

#určení základních proměných + cesty k datum
path = DATA_ROOT + "/data/special_mistnosti"
list_of_screens = os.listdir(path)
    
screens_with_doors = []

#vytvoření seznamu obrazovek
for screen_ind,screen in enumerate(list_of_screens):
    new = []
    
    #mapka
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
