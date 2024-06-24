text = []
minigame_text = []
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

def minigame_lang(minigame, language):
    if language == "ENG":
        if minigame == "lang":
            minigame_text = ["Prime number","Incorrect- solution:","Write a prime number from "," to "]
            
        elif minigame == "michalek":
            minigame_text = ["Count the discriminant","Correct","Incorrect"]
            
        elif minigame == "polak":
            minigame_text = ["s + ENTER/SPACE to SKIP","Welcome mere human beings!","Today, we will discuss...","...","wait!","Where's þe chalk‽","What ever! The Class slave- I mean service, will get it.","It's ","OK ",", go get ÞE CHALK!!","Hey...","You got þe chalk... Good job!","Now just bring it back to our realm, so we can use it.","But you will never make it... ","AAAAAA, you're back...","GOOD","I guess we can start now.","So, todays theme is...","Þe infinite chaos beyond the stars, far away from\nour understanding...","Þe realms both beyond and inside our own...","Þe infinite possibilities of human mind and\nhalucinogenic substances from þe ","ha...","HA...","HAHAHA HA HA  HA  HA    Ha","You failed miserably.","ButYouWillFailNoMore...","Press ||SPACE|| to jump.","YOU HAVE LOST SUCCSESSFULY","YOU HAVE WON SUCCSESSFULY","Press ||SEMICOLON|| for a secret."]
            
        elif minigame == "lanka":
            minigame_text = [f"Wrong answer, the correct answer is: ",f"Correct"]
            
    if language == "CZE":
        if minigame == "lang":
            minigame_text = ["Prvočíslo","Špatně- řešení:","Napiš prvočíslo od "," do "]
            
        elif minigame == "michalek":
            minigame_text = ["Vypočti Diskriminant","Správně","Špatně"]
            
        elif minigame == "polak":
            minigame_text = ["s + ENTER/MEZERNÍK pro PŘESKOČENÍ","Vítejte prostá lidská stvoření!","Dnes probereme...","...","počkat!","Kde je křída?","Co už! Třídní otrok- tedy služba jí přinese","Je to ","Dobře ",", dojdi pro KŘÍDU!!","Hele...","Dostal jsi tu křídu... Dobrá práce!","Nyní se s ní vrať do naší dimenze, abychom jí mohli použít.","Ale to se ti nikdy nepovede... ","AAAAAA, jsi zpět...","DOBŘE","Myslím, že můžeme začít.","Takže, dnešní téma je...","Nekonečný chaos za hvězdami, daleko od\nnašeho pochopení...","Dimenze za, i v naší vlastní...","Nekonečné možnosti lidské mysli a\nhalucinogenních látek... ","ha...","HA...","HAHAHA HA HA  HA  HA    Ha","Bidně jsi zklamal.","AleUžNikdyNezklameš...","Zmáčkní ||MEZERNÍK|| pro skok.","ÚSPĚŠNĚ JSI PROHRÁL","ÚSPĚŠNĚ JSI VYHRÁL","Zmáčkní ||STŘEDNÍK|| pro tajemství."]
            
        elif minigame == "lanka":
            
            minigame_text = ["Špatná odpověd, správně je: ",f"Správně",]

    return minigame_text