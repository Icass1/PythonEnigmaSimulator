from tkinter import *
from time import sleep

print_all_variables = False

window = Tk()

window.title("Enigma")
window.geometry("800x560")
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

out = StringVar() 

alphabet_for_position_rotor = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
alphabet =                  ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?")

_alpha_rotor_external =     ("q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p")
_alpha_rotor_internal =     ('a','o','K','P','/','3','U','l','w','c','D','u','H','V','8','ú','Ñ','Y','n','p','4','F','k','*','2','-','O','q','B','C','d','R','I','Z',',','h','L',"¿",'r','Ú','A','.','9','S','x','é','É','Q','i','W','f','6','g','t',' ','7','s','Á','T','Ó','v','G','á','Í','M','ó','m','e','N','+','X','ñ','1','E',"?",'b','y','j','J','5','í','z')

_beta_rotor_external =      ("S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R")
_beta_rotor_internal =      ('k','n','j','*','T','O',',','z','5','L','N','F','B','o','g','P',"¿",'Ñ','3','d',' ','i','Á','J','í','Z','G','.','4','r','q','C','K','-','v','s','1','t','c','U','á','l','h','E','m','e',"?",'x','R','W','H','y','9','Y','ú','7','S','2','6','w','8','é','ñ','ó','b','I','X','u','Í','Q','Ú','D','É','M','+','V','f','a','p','/','A','Ó')

_reflector_rotor_external = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?")
_reflector_rotor_internal = ("y","+","u","a","P","M","í","*","É","v","1","T","F","Q","q","8","E","N"," ","k","L","3","n","X","W","c","h","D","x","Y","-","Ú",",","m","Z","Í","w","S","4","g","V","é","Ó","7","Ñ","6","t","s","C","J","j","b","A",".","/","I","i","o","e","ó","ñ","G","á","9","K","5","U","l","2","r","p","O","ú","z","f","R","d","B","H","Á","?","¿")


class alpha_rotor_external:
    def __init__(self):
        self.number = None
        self.letter = None

    def number_to_letter(self, number):
        number -=1
        out = _alpha_rotor_external[number]
        return out

    def letter_to_number(self, letter):
        counter = 0 
        for k in _alpha_rotor_external:
            if k == letter:
                out = counter 
                out += 1
            counter += 1
        return out
        
class alpha_rotor_internal:
    def __init__(self):
        self.number = None
        self.letter = None

    def number_to_letter(self, number):
        number -=1
        out = _alpha_rotor_internal[number]
        return out

    def letter_to_number(self, letter):
        counter = 0 
        for k in _alpha_rotor_internal:
            if k == letter:
                out = counter 
                out += 1
            counter += 1
        return out

class beta_rotor_external:
    def __init__(self):
        self.number = None
        self.letter = None

    def number_to_letter(self, number):
        number -=1
        out = _beta_rotor_external[number]
        return out

    def letter_to_number(self, letter):
        counter = 0 
        for k in _beta_rotor_external:
            if k == letter:
                out = counter
                out += 1
            counter += 1
        return out

class beta_rotor_internal:
    def __init__(self):
        self.number = None
        self.letter = None

    def number_to_letter(self, number):
        number -=1
        out = _beta_rotor_internal[number]
        return out

    def letter_to_number(self, letter):
        counter = 0 
        for k in _beta_rotor_internal:
            if k == letter:
                out = counter
                out += 1
            counter += 1
        return out

class reflector_rotor_external:
    def __init__(self):
        self.number = None
        self.letter = None

    def number_to_letter(self, number):
        number -=1
        out = _reflector_rotor_external[number]
        return out

    def letter_to_number(self, letter):
        counter = 0 
        for k in _reflector_rotor_external:
            if k == letter:
                out = counter 
                out += 1
            counter += 1
        return out

class reflector_rotor_internal:
    def __init__(self):
        self.number = None
        self.letter = None
        
    def number_to_letter(self, number):
        number -=1
        out = _reflector_rotor_internal[number]
        return out

    def letter_to_number(self, letter):
        counter = 0 
        for k in _reflector_rotor_internal:
            if k == letter:
                out = counter
                out += 1
            counter += 1
        return out

alpha_external = alpha_rotor_external()
alpha_internal = alpha_rotor_internal()
beta_external = beta_rotor_external()
beta_internal = beta_rotor_internal()
reflector_external = reflector_rotor_external()
reflector_internal = reflector_rotor_internal()

def letter_up(button):

    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3

    if button == 1:
        if number_of_letter_1 > 26: number_of_letter_1 = 0
        
        number_of_letter_1 += 1

        letter_1 = number_to_letter_display(number=number_of_letter_1 + 1)
        letter_2 = number_to_letter_display(number=number_of_letter_1)
        letter_3 = number_to_letter_display(number=number_of_letter_1 - 1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_1_1.set(value_1)
        input_text_1_2.set(value_2)
        input_text_1_3.set(value_3)
        
    if button == 2:
        if number_of_letter_2 > 26: number_of_letter_2 = 0
        
        number_of_letter_2 += 1

        letter_1 = number_to_letter_display(number=number_of_letter_2 + 1)
        letter_2 = number_to_letter_display(number=number_of_letter_2)
        letter_3 = number_to_letter_display(number=number_of_letter_2 - 1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_2_1.set(value_1)
        input_text_2_2.set(value_2)
        input_text_2_3.set(value_3)

    if button == 3:
        if number_of_letter_3 > 26: number_of_letter_3 = 0
        
        number_of_letter_3 += 1
        letter_1 = number_to_letter_display(number=number_of_letter_3 + 1)
        letter_2 = number_to_letter_display(number=number_of_letter_3)
        letter_3 = number_to_letter_display(number=number_of_letter_3 - 1)

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

        letter_1 = number_to_letter_display(number=number_of_letter_1 + 1)
        letter_2 = number_to_letter_display(number=number_of_letter_1)
        letter_3 = number_to_letter_display(number=number_of_letter_1 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        input_text_1_1.set(value_1)
        input_text_1_2.set(value_2)
        input_text_1_3.set(value_3)

    if button == 2:
        if number_of_letter_2 < 1: number_of_letter_2 = 27
        
        number_of_letter_2 -= 1

        letter_1 = number_to_letter_display(number = number_of_letter_2+1)
        letter_2 = number_to_letter_display(number = number_of_letter_2)
        letter_3 = number_to_letter_display(number = number_of_letter_2-1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_2_1.set(value_1)
        input_text_2_2.set(value_2)
        input_text_2_3.set(value_3)   

    if button == 3:
        if number_of_letter_3 < 1: number_of_letter_3 = 27
        
        number_of_letter_3 -= 1

        letter_1 = number_to_letter_display(number=number_of_letter_3+1)
        letter_2 = number_to_letter_display(number=number_of_letter_3)
        letter_3 = number_to_letter_display(number=number_of_letter_3-1)

        value_1=(letter_1)
        value_2=(letter_2)
        value_3=(letter_3)

        input_text_3_1.set(value_1)
        input_text_3_2.set(value_2)
        input_text_3_3.set(value_3)

def number_to_letter(number):
    number -=1
    if number < 0: number = 26
    number_to_letter_out = alphabet[number]
    return number_to_letter_out

def letter_to_number(letter):
    counter = 0 
    for k in alphabet:
        if k == letter:
            letter_to_number_out = counter 
            letter_to_number_out += 1
        counter += 1
    return letter_to_number_out

def number_to_letter_display(number):
    number -=1
    if number > 26: number = 0
    out = alphabet_for_position_rotor[number]
    return out

def encript():
    
    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3
    global out

    _input = _input_text.get()

    _out = ""
    _out += number_to_letter(number_of_letter_1) + " " + number_to_letter(number_of_letter_2) + " " + number_to_letter(number_of_letter_3) + " "
    for letter in _input:
        if letter in alphabet:
            _position_alpha = number_of_letter_3
            _position_beta = number_of_letter_2
            _position_reflector = number_of_letter_1

            if print_all_variables: 
                        
                print("\n")

                print("number_of_letter_1: " + str(number_of_letter_1))
                print("number_of_letter_2: " + str(number_of_letter_2))
                print("number_of_letter_3: " + str(number_of_letter_3))

                print("Position alpha: " + str(_position_alpha))
                print("Position beta: " + str(_position_beta)) 
                print("Position reflector: " + str(_position_reflector))

            _letter = int(letter_to_number(letter=letter))
            _letter -= _position_alpha
            _letter += 1
            if _letter > 82: _letter -= 82
            elif _letter < 1: _letter += 82

            a = alpha_external.number_to_letter(number=_letter)
            if print_all_variables: print("a: " + str(a))
            
            b = int(alpha_internal.letter_to_number(letter=a))
            if print_all_variables: print("b: " + str(b))

            b += _position_alpha
            b -= _position_beta
            if b > 82: b -= 82
            elif b < 1: b += 82

            c = beta_external.number_to_letter(number=b)
            if print_all_variables: print("c: " + str(c))

            d = int(beta_internal.letter_to_number(letter=c))
            if print_all_variables: print("d: " + str(d))

            d += _position_beta
            d -= _position_reflector
            if d > 82: d -= 82
            elif d < 1: d += 82

            e = reflector_external.number_to_letter(number=d)
            if print_all_variables: print("e: " + e)

            f = int(reflector_internal.letter_to_number(letter=e))
            if print_all_variables: print("f: " + str(f))        

            f-=_position_beta
            f+=_position_reflector
            if f > 82: f -= 82
            elif f < 1: f += 82

            g = beta_internal.number_to_letter(number=f)
            if print_all_variables: print("g: " + str(g))

            h = int(beta_external.letter_to_number(letter=g))
            if print_all_variables: print("h: " + str(h))

            h -=_position_alpha
            h +=_position_beta
            if h > 82: h -= 82
            elif h < 1: h += 82

            i = alpha_internal.number_to_letter(number=h)
            if print_all_variables: print("i: " + str(i))

            j = int(alpha_external.letter_to_number(letter=i))
            if print_all_variables: print("j: " + str(j))

            j -= 1
            j += _position_alpha
            if j > 82: j -= 82
            elif j < 1: j += 82

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

            _out += number_to_letter(number=j)
            value=(_out)
            out.set(value=value)
        else: print('"' + str(letter) + '"' + " is not in the alphabet.")

def reset():
    global number_of_letter_1
    global number_of_letter_2
    global number_of_letter_3
    number_of_letter_1 = 0
    number_of_letter_2 = 0
    number_of_letter_3 = 0
    letter_up(button=1)
    letter_up(button=2)
    letter_up(button=3)

letter_up(button=1)
letter_up(button=2)
letter_up(button=3)

button_up_1 = Button(window,text="UP",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:letter_up(button=1),cursor="hand2").grid(row=1, column=0, padx=13, pady=10)
button_down_1 = Button(window,text="DOWN",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:letter_down(button=1),cursor="hand2").grid(row=5, column=0, padx=13, pady=10)

button_up_2 = Button(window, text="UP", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_up(button=2), cursor="hand2").grid(row=1, column=1, padx=13, pady=10)
button_down_2 = Button(window, text="DOWN", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_down(button=2), cursor="hand2").grid(row=5, column=1, padx=13, pady=10)

button_up_3 = Button(window, text="UP", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_up(button=3), cursor="hand2").grid(row=1, column=2, padx=13, pady=10)
button_down_3 = Button(window, text="DOWN", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:letter_down(button=3), cursor="hand2").grid(row=5, column=2 , padx=13, pady=10)


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


_input_text = Entry(window, font=("arial",15), width=50, textvariable="", borderwidth=3, background="white")
_input_text.place(x=30, y=400)

button_encript = Button(window, text="Encript", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:encript(), cursor="hand2").place(x=30, y=435)

button_reset = Button(window, text="Reset", bg=color_boton, fg=cn, activebackground=actb, width=ancho_boton, height=alto_boton, command=lambda:reset(), cursor="hand2").place(x=350, y=160)

_output_text = Entry(window, font=("arial",15), width=50, textvariable=out, borderwidth=3, background="white")
_output_text.place(x=30, y=500)

window.mainloop()
