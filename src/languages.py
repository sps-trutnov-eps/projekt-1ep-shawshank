text = []
#INDEXY TEXTU
#0 Prohra
#1 Stiskni ENTER
#2 Výhra
#3 Najdi klíč od skříňky
#4 >Najdi klíč od skříňky
#5 Vezmi si boty
#6 >Vezmi si boty
#7 Uteč
#8 >Uteč
#9 Titul
#10 Začít
#11 Titulky
#12 Vypnout
#13 Titulky - Obsah
#14 ESC 1
#15 ESC 2

def lang(language):
    if language == "ENG":
        text = ["GAME OVER","PRESS ENTER","YOU WON","Find the locker key.",">Find the locker key.","Get your shoes.",">Get your shoes.","Escape!",">Escape!","¤ Escape from Shawshank high school ¤","START","CREDITS","EXIT",'''Project made by
class 1.EP group 2

---Map Generation---

Jakub Polák
Karel Kříž
Jan Štěpánek

---Player Mechanics---

Vojtěch Nepimach
Karel Kříž
Jakub Polák

---Textures---

Jakub Polák
Karel Kříž
Vojtěch Nepimach

---Sounds---

Jakub Polák
Anna Poláková

---Minigames---

Marek Langer
Jan Pospíšil
Tadeáš Udatný
Martin Michálek
Tomáš Svoboda
Jakub Polák
Stanislav Lang
Vojtěch Laňka
Jan Serbousek

---Used Software---

Thonny
Tiled
Pixel Studio
Aseprite
Ardour

(more info on github)


''', "To go to the menu, press escape again.", "You will lose all progress."]
        
    if language == "CZE":
        text = ["PROHRÁLS","ZMÁČKNI ENTER","VYHRÁLS","Najdi klíč od skříňky.",">Najdi klíč od skříňky.","Vezmi si boty.",">Vezmi si boty.","Uteč!",">Uteč","¤ Útěk ze Střední školy Shawshank ¤","ZAČÍT","TITULKY","VYPNOUT",'''Projekt vypracován
třídou 1.EP skupina 2

---Generace mapy---

Jakub Polák
Karel Kříž
Jan Štěpánek

---Mechanika hráče---

Vojtěch Nepimach
Karel Kříž
Jakub Polák

---Textury---

Jakub Polák
Karel Kříž
Vojtěch Nepimach

---Zvuky---

Jakub Polák
Anna Poláková

---Minihry---

Marek Langer
Jan Pospíšil
Tadeáš Udatný
Martin Michálek
Tomáš Svoboda
Jakub Polák
Stanislav Lang
Vojtěch Laňka
Jan Serbousek

---Použitý Software---

Thonny
Tiled
Pixel Studio
Aseprite
Ardour

(více naleznete na githubu)


''', "Pro přechod do menu znovu zmáčkněte escape.", "Ztratíte všechen postup."]
        
    return text
