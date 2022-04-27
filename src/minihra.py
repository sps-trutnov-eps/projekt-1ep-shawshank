import random
import tkinter as tk
okno=tk.Tk()
okno.geometry("400x350")
okno.title("kámen nůžky papír")

#hráč, počítač
hrac_score=0
pocitac_score=0
hrac_choice=""
pocitac_choice=""

#cisla, volby
def volba_to_cislo(volba):
    rps={"kámen":0,"papír":1,"nůžky":2}
    return rps[volba]

def cislo_to_volba(cislo):
    rps={0:"kámen",1:"nůžky",2:"papír"}
    return rps[cislo]

#random volba počítače



#tlačítka
tlacitko1=tk.Button(text=" kámen ", width=8,height=2,bg="gray")
tlacitko1.grid(row=1,column=0,padx=3,pady=3)

tlacitko2=tk.Button(text=" nůžky ", width=8,height=2,bg="skyblue")
tlacitko2.grid(row=2,column=0,padx=3,pady=3)

tlacitko3=tk.Button(text=" papír ", width=8,height=2,bg="white")
tlacitko3.grid(row=3,column=0,padx=3,pady=3)

okno.mainloop()

        

        