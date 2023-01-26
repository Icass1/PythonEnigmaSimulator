from tkinter import *
from time import sleep

window = Tk()

window.title("Enigma")
window.geometry("400x560")
window.resizable(True,True)
window.configure(background="white")

color_boton=("gray50")
cn=("white")
actb="gray75"
ancho_boton=9
alto_boton=3

number_of_letter_1 = 0
number_of_letter_2 = 0
number_of_letter_3 = 0

input_text_1_1 = StringVar()
input_text_1_2 = StringVar()
input_text_1_3 = StringVar()

input_text_2_1 = StringVar()
input_text_2_2 = StringVar()
input_text_2_3 = StringVar()

input_text_3_1 = StringVar()
input_text_3_2 = StringVar()
input_text_3_3 = StringVar()

alphabet_for_position_rotor = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
def number_to_letter(number):
    number -=1
    if number > 26: number = 0
    out = alphabet_for_position_rotor[number]
    return out

def letter_up(button):
    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3
    
    if button == 1:
        if number_of_letter_1 > 26: number_of_letter_1 = 0
        
        number_of_letter_1 += 1

        letter_1 = number_to_letter(number=number_of_letter_1 + 1)
        letter_2 = number_to_letter(number=number_of_letter_1)
        letter_3 = number_to_letter(number=number_of_letter_1 - 1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_1_1.set(value_1)
        input_text_1_2.set(value_2)
        input_text_1_3.set(value_3)

    if button == 2:
        if number_of_letter_2 > 26: number_of_letter_2 = 0
        
        number_of_letter_2 += 1

        letter_1 = number_to_letter(number=number_of_letter_2 + 1)
        letter_2 = number_to_letter(number=number_of_letter_2)
        letter_3 = number_to_letter(number=number_of_letter_2 - 1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_2_1.set(value_1)
        input_text_2_2.set(value_2)
        input_text_2_3.set(value_3)

    if button == 3:
        if number_of_letter_3 > 26: number_of_letter_3 = 0
        
        number_of_letter_3 += 1

        letter_1 = number_to_letter(number=number_of_letter_3 + 1)
        letter_2 = number_to_letter(number=number_of_letter_3)
        letter_3 = number_to_letter(number=number_of_letter_3 - 1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_3_1.set(value_1)
        input_text_3_2.set(value_2)
        input_text_3_3.set(value_3)

def letter_down(button):
    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3

    if button == 1:
        if number_of_letter_1 < 1: number_of_letter_1 = 27
        
        number_of_letter_1 -= 1

        letter_1 = number_to_letter(number=number_of_letter_1 + 1)
        letter_2 = number_to_letter(number=number_of_letter_1)
        letter_3 = number_to_letter(number=number_of_letter_1 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        input_text_1_1.set(value_1)
        input_text_1_2.set(value_2)
        input_text_1_3.set(value_3)

    if button == 2:
        if number_of_letter_2 < 1: number_of_letter_2 = 27
        
        number_of_letter_2 -= 1

        letter_1 = number_to_letter(number = number_of_letter_2+1)
        letter_2 = number_to_letter(number = number_of_letter_2)
        letter_3 = number_to_letter(number = number_of_letter_2-1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_2_1.set(value_1)
        input_text_2_2.set(value_2)
        input_text_2_3.set(value_3)   

    if button == 3:
        if number_of_letter_3 < 1: number_of_letter_3 = 27
        
        number_of_letter_3 -= 1

        letter_1 = number_to_letter(number=number_of_letter_3+1)
        letter_2 = number_to_letter(number=number_of_letter_3)
        letter_3 = number_to_letter(number=number_of_letter_3-1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_3_1.set(value_1)
        input_text_3_2.set(value_2)
        input_text_3_3.set(value_3)

letter_up(button=1)
letter_up(button=2)
letter_up(button=3)

Button_up_1 = Button(window,text="UP",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:letter_up(button=1),cursor="hand2").grid(row=1, column=0, padx=13, pady=10)
Button_down_1 = Button(window,text="DOWN",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:letter_down(button=1),cursor="hand2").grid(row=5, column=0, padx=13, pady=10)

Button_up_2 = Button(window, text="UP", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_up(button=2), cursor="hand2").grid(row=1, column=1, padx=13, pady=10)
Button_down_2 = Button(window, text="DOWN", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_down(button=2), cursor="hand2").grid(row=5, column=1, padx=13, pady=10)

Button_up_3 = Button(window, text="UP", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_up(button=3), cursor="hand2").grid(row=1, column=2, padx=13, pady=10)
Button_down_3 = Button(window, text="DOWN", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_down(button=3), cursor="hand2").grid(row=5, column=2 , padx=13, pady=10)


screen_1_1 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_1_1, borderwidth=0, background="white", justify="right")
screen_1_2 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_1_2, borderwidth=0, background="white", justify="right")
screen_1_3 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_1_3, borderwidth=0, background="white", justify="right")

screen_2_1 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_2_1, borderwidth=0, background="white", justify="right")
screen_2_2 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_2_2, borderwidth=0, background="white", justify="right")
screen_2_3 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_2_3, borderwidth=0, background="white", justify="right")

screen_3_1 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_3_1, borderwidth=0, background="white", justify="right")
screen_3_2 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_3_2, borderwidth=0, background="white", justify="right")
screen_3_3 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_3_3, borderwidth=0, background="white", justify="right")


screen_1_1.grid(row=2, column=0, padx=20, pady=20)
screen_1_2.grid(row=3, column=0, padx=20, pady=20)
screen_1_3.grid(row=4, column=0, padx=20, pady=20)

screen_2_1.grid(row=2, column=1, padx=20, pady=20)
screen_2_2.grid(row=3, column=1, padx=20, pady=20)
screen_2_3.grid(row=4, column=1, padx=20, pady=20)

screen_3_1.grid(row=2, column=2, padx=20, pady=20)
screen_3_2.grid(row=3, column=2, padx=20, pady=20)
screen_3_3.grid(row=4, column=2, padx=20, pady=20)


_input = Entry(window, font=("arial",20,"bold"), width=10, textvariable="", borderwidth=3, background="white", justify="right")
_input.place(x=30, y=400)

print(_input)
window.mainloop()
