import random

volba = ["kámen", "nůžky", "papír"]

počítač = random.choice(volba)
hráč = None

while hráč not in volba:
    hráč = input("kámen, nůžky, nebo papír?: ").lower()
    
    if hráč == počítač:
        print("počítač: ", počítač)
        print("hráč: ", hráč)
        print("Remíza!")
        
if hráč == "kámen":
    if počítač == "papír":
        print("počítač: ", počítač)
        print("hráč: ", hráč)
        print("Prohráváš!")
        
if hráč == "nůžky":
    if počítač == "papír":
        print("počítač: ", počítač)
        print("hráč: ", hráč)
        print("Vyhráváš!")
        
if hráč == "papír":
    if počítač == "kámen":
        print("počítač: ", počítač)
        print("hráč: ", hráč)
        print("Vyhráváš!")
        
if hráč == "papír":
    if počítač == "nůžky":
        print("počítač: ", počítač)
        print("hráč: ", hráč)
        print("Prohráváš!")
        
if hráč == "kámen":
    if počítač == "nůžky":
        print("počítač: ", počítač)
        print("hráč: ", hráč)
        print("Vyhráváš!")
        
if hráč == "nůžky":
    if počítač == "kámen":
        print("počítač: ", počítač)
        print("hráč: ", hráč)
        print("Prohráváš!")
        
        

        