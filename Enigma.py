from tkinter import *


window = Tk()

window.title("VMG-530z")
window.geometry("400x560")
window.resizable(True,True)
window.configure(background="white")

color_boton=("gray50")
cn=("white")
actb="gray75"
ancho_boton=9
alto_boton=3

number_of_letter = 0
input_text1=StringVar()
input_text2=StringVar()
input_text3=StringVar()

alphabet_for_position_rotor = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
def number_to_letter(number):
    number -=1
    if number > 26: number = 0
    out = alphabet_for_position_rotor[number]
    return out

def abc():
    global number_of_letter
    if number_of_letter > 26: number_of_letter = 0
    
    number_of_letter += 1

    letter1 = number_to_letter(number=number_of_letter+1)
    letter2 = number_to_letter(number=number_of_letter)
    letter3 = number_to_letter(number=number_of_letter-1)

    opera1=(letter1)
    opera2=(letter2)
    opera3=(letter3)

    input_text1.set(opera1)
    input_text2.set(opera2)
    input_text3.set(opera3)

abc()

Boton_up = Button(window,text="6",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:abc(),cursor="hand2").grid(row=1,column=2, padx=13, pady=10)
Boton_down = Button(window,text="6",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:abc(),cursor="hand2").grid(row=5,column=2, padx=13, pady=10)


screen1 = Entry(window,font=("arial",20,"bold"),width=2,textvariable=input_text1,borderwidth=0,background="white",justify="right")
screen2 = Entry(window,font=("arial",20,"bold"),width=2,textvariable=input_text2,borderwidth=0,background="white",justify="right")
screen3 = Entry(window,font=("arial",20,"bold"),width=2,textvariable=input_text3,borderwidth=0,background="white",justify="right")

screen1.grid(row=2,column=0,columnspan=6,padx=20,pady=20)
screen2.grid(row=3,column=1,columnspan=6,padx=20,pady=20)
screen3.grid(row=4,column=1,columnspan=6,padx=20,pady=20)

window.mainloop()
