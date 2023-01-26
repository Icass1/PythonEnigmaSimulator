from tkinter import *
from time import sleep

print_all_variables = False

window = Tk()

window.title("Enigma")
window.geometry("650x560")
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

error_text = StringVar()

out = StringVar() 

listbox = Listbox()

counter_invalid_letter = 0

alphabet_for_position_rotor = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
alphabet =                  ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?")

_alpha_rotor_external =     ("q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p")
_alpha_rotor_internal =     ('a','o','K','P','/','3','U','l','w','c','D','u','H','V','8','ú','Ñ','Y','n','p','4','F','k','*','2','-','O','q','B','C','d','R','I','Z',',','h','L',"¿",'r','Ú','A','.','9','S','x','é','É','Q','i','W','f','6','g','t',' ','7','s','Á','T','Ó','v','G','á','Í','M','ó','m','e','N','+','X','ñ','1','E',"?",'b','y','j','J','5','í','z')

_beta_rotor_external =      ("S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R")
_beta_rotor_internal =      ('k','n','j','*','T','O',',','z','5','L','N','F','B','o','g','P',"¿",'Ñ','3','d',' ','i','Á','J','í','Z','G','.','4','r','q','C','K','-','v','s','1','t','c','U','á','l','h','E','m','e',"?",'x','R','W','H','y','9','Y','ú','7','S','2','6','w','8','é','ñ','ó','b','I','X','u','Í','Q','Ú','D','É','M','+','V','f','a','p','/','A','Ó')

_reflector_rotor_external = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?")
_reflector_rotor_internal = ("y","+","u","a","P","M","í","*","É","v","1","T","F","Q","q","8","E","N"," ","k","L","3","n","X","W","c","h","D","x","Y","-","Ú",",","m","Z","Í","w","S","4","g","V","é","Ó","7","Ñ","6","t","s","C","J","j","b","A",".","/","I","i","o","e","ó","ñ","G","á","9","K","5","U","l","2","r","p","O","ú","z","f","R","d","B","H","Á","?","¿")

def number_to_letter(source, number):
    number -=1
    if number < 0: number = 26
    number_to_letter_out = source[number]
    return number_to_letter_out

def letter_to_number(source, letter):
    counter = 0 
    for k in source:
        if k == letter:
            letter_to_number_out = counter 
            letter_to_number_out += 1
        counter += 1
    return letter_to_number_out

def letter_up(button):

    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3

    if button == 1:
        if number_of_letter_1 > 26: number_of_letter_1 = 0
        
        number_of_letter_1 += 1

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_1 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_1)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_1 - 1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_1_1.set(value_1)
        input_text_1_2.set(value_2)
        input_text_1_3.set(value_3)
        
    if button == 2:
        if number_of_letter_2 > 26: number_of_letter_2 = 0
        
        number_of_letter_2 += 1

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_2 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_2)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_2 - 1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_2_1.set(value_1)
        input_text_2_2.set(value_2)
        input_text_2_3.set(value_3)

    if button == 3:
        if number_of_letter_3 > 26: number_of_letter_3 = 0
        
        number_of_letter_3 += 1
        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_3 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_3)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_3 - 1)

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

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_1 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_1)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_1 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        input_text_1_1.set(value_1)
        input_text_1_2.set(value_2)
        input_text_1_3.set(value_3)

    if button == 2:
        if number_of_letter_2 < 1: number_of_letter_2 = 27
        
        number_of_letter_2 -= 1

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number = number_of_letter_2+1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number = number_of_letter_2)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number = number_of_letter_2-1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_2_1.set(value_1)
        input_text_2_2.set(value_2)
        input_text_2_3.set(value_3)   

    if button == 3:
        if number_of_letter_3 < 1: number_of_letter_3 = 27
        
        number_of_letter_3 -= 1

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_3+1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_3)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_3-1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_3_1.set(value_1)
        input_text_3_2.set(value_2)
        input_text_3_3.set(value_3)

def reset():
    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3
    global label
    global counter_invalid_letter

    number_of_letter_1 = 0
    number_of_letter_2 = 0
    number_of_letter_3 = 0
    letter_up(button=1)
    letter_up(button=2)
    letter_up(button=3)
    
    while counter_invalid_letter > 0:
        counter_invalid_letter -= 1
        listbox.delete(0)
    counter_invalid_letter = 0

def encript():
    
    global label
    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3
    global out
    global counter_invalid_letter

    _input = _input_text.get()
    _position_entry_error = 0

    _out = ""
    _out += number_to_letter(source=alphabet, number=number_of_letter_1) + " " + number_to_letter(source=alphabet, number=number_of_letter_2) + " " + number_to_letter(source=alphabet, number=number_of_letter_3) + " "
    for letter in _input:
        if letter in alphabet:
            _position_alpha = number_of_letter_3
            _position_beta = number_of_letter_2
            _position_reflector = number_of_letter_1

            _letter = int(letter_to_number(source=alphabet, letter=letter))
            _letter -= _position_alpha
            _letter += 1
            if _letter > 82: _letter -= 82
            elif _letter < 1: _letter += 82

            a = number_to_letter(source=_alpha_rotor_external, number=_letter)
            
            b = int(letter_to_number(source=_alpha_rotor_internal, letter=a))

            b += _position_alpha
            b -= _position_beta
            if b > 82: b -= 82
            elif b < 1: b += 82

            c = number_to_letter(source=_beta_rotor_external, number=b)

            d = int(letter_to_number(source=_beta_rotor_internal, letter=c))

            d += _position_beta
            d -= _position_reflector
            if d > 82: d -= 82
            elif d < 1: d += 82

            e = number_to_letter(source=_reflector_rotor_external, number=d)

            f = int(letter_to_number(source=_reflector_rotor_internal, letter=e))

            f-=_position_beta
            f+=_position_reflector
            if f > 82: f -= 82
            elif f < 1: f += 82

            g = number_to_letter(source=_beta_rotor_internal, number=f)

            h = int(letter_to_number(source=_beta_rotor_external, letter=g))

            h -=_position_alpha
            h +=_position_beta
            if h > 82: h -= 82
            elif h < 1: h += 82

            i = number_to_letter(source=_alpha_rotor_internal, number=h)

            j = int(letter_to_number(source=_alpha_rotor_external, letter=i))

            j -= 1
            j += _position_alpha
            if j > 82: j -= 82
            elif j < 1: j += 82

            if print_all_variables:
                print("\n")

                print("number_of_letter_1: " + str(number_of_letter_1))
                print("number_of_letter_2: " + str(number_of_letter_2))
                print("number_of_letter_3: " + str(number_of_letter_3))

                print("Position alpha: " + str(_position_alpha))
                print("Position beta: " + str(_position_beta)) 
                print("Position reflector: " + str(_position_reflector))

                print("a: " + str(a))
                print("b: " + str(b))
                print("c: " + str(c))
                print("d: " + str(d))
                print("e: " + str(e))
                print("f: " + str(f))
                print("g: " + str(g))
                print("h: " + str(h))
                print("i: " + str(i))
                print("j: " + str(j))

                print("3: " + str(number_of_letter_3))
                print("2: " + str(number_of_letter_2))
                print("1: " + str(number_of_letter_1))

            number_of_letter_3_memory = number_of_letter_3
            number_of_letter_2_memory = number_of_letter_2
            number_of_letter_1_memory = number_of_letter_1

            letter_up(button=3)
            if number_of_letter_3_memory > 26:
                letter_up(button=2)
            
            if number_of_letter_2_memory > 26: letter_up(button=1)
            if number_of_letter_1_memory > 26:
                number_of_letter_1 = 1
                number_of_letter_2 = 1
                number_of_letter_3 = 1

            _out += number_to_letter(source=alphabet, number=j)
            out.set(value = (_out))

        else: 
            counter_invalid_letter += 1
            error_text = '"' + str(letter) + '"' + " is not in the alphabet."
            _position_entry_error += 1
            listbox.insert(_position_entry_error, error_text)

letter_up(button=1)
letter_up(button=2)
letter_up(button=3)

button_up_1 = Button(window,text="UP",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:letter_up(button=1),cursor="hand2").grid(row=1, column=0, padx=13, pady=10)
button_down_1 = Button(window,text="DOWN",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:letter_down(button=1),cursor="hand2").grid(row=5, column=0, padx=13, pady=10)

button_up_2 = Button(window, text="UP", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_up(button=2), cursor="hand2").grid(row=1, column=1, padx=13, pady=10)
button_down_2 = Button(window, text="DOWN", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_down(button=2), cursor="hand2").grid(row=5, column=1, padx=13, pady=10)

button_up_3 = Button(window, text="UP", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_up(button=3), cursor="hand2").grid(row=1, column=2, padx=13, pady=10)
button_down_3 = Button(window, text="DOWN", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_down(button=3), cursor="hand2").grid(row=5, column=2 , padx=13, pady=10)

screen_1_1 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_1_1, borderwidth=0, background="white", justify="right").grid(row=2, column=0, padx=20, pady=20)
screen_1_2 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_1_2, borderwidth=0, background="white", justify="right").grid(row=3, column=0, padx=20, pady=20)
screen_1_3 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_1_3, borderwidth=0, background="white", justify="right").grid(row=4, column=0, padx=20, pady=20)

screen_2_1 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_2_1, borderwidth=0, background="white", justify="right").grid(row=2, column=1, padx=20, pady=20)
screen_2_2 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_2_2, borderwidth=0, background="white", justify="right").grid(row=3, column=1, padx=20, pady=20)
screen_2_3 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_2_3, borderwidth=0, background="white", justify="right").grid(row=4, column=1, padx=20, pady=20)

screen_3_1 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_3_1, borderwidth=0, background="white", justify="right").grid(row=2, column=2, padx=20, pady=20)
screen_3_2 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_3_2, borderwidth=0, background="white", justify="right").grid(row=3, column=2, padx=20, pady=20)
screen_3_3 = Entry(window, font=("arial",20,"bold"), width=2, textvariable=input_text_3_3, borderwidth=0, background="white", justify="right").grid(row=4, column=2, padx=20, pady=20)

_input_text = Entry(window, font=("arial",15), width=50, textvariable="", borderwidth=3, background="white")
_input_text.place(x=30, y=400)

_output_text = Entry(window, font=("arial",15), width=50, textvariable=out, borderwidth=3, background="white").place(x=30, y=500)

button_encript = Button(window, text="Encript", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:encript(), cursor="hand2").place(x=30, y=435)

button_reset = Button(window, text="Reset", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:reset(), cursor="hand2").place(x=350, y=160)

listbox.place(x=450, y=40, width=150, height=300)

window.mainloop()
