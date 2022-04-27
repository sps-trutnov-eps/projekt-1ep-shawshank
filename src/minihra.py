import pygame

pygame.init() 
screen = pygame.display.set_mode((1000, 1000)) 
 def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = (text="Správně!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = (text="Špatně!!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)

 
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
             
 
    screen.fill((195, 155, 119)) 
      
    screen.blit(dialogue, (40, 40)) 
      




















def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = (text="Správně!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = (text="Špatně!!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)



