from tkinter import *
from time import sleep

print_all_variables = False

window = Tk()

window.title("Enigma")
window.geometry("650x560")
window.resizable(True,True)
window.configure(background="white")

color_button = ("gray50")
cn = ("white")
actb = "gray75"
width_button = 9
high_button = 3

# Set rotors position.
number_of_letter_rotor_1 = 1
number_of_letter_rotor_2 = 1
number_of_letter_rotor_3 = 1

# Set tipe of variables for rotors.
rotor_letter_1_1 = StringVar()
rotor_letter_1_2 = StringVar()
rotor_letter_1_3 = StringVar()

rotor_letter_2_1 = StringVar()
rotor_letter_2_2 = StringVar()
rotor_letter_2_3 = StringVar()

rotor_letter_3_1 = StringVar()
rotor_letter_3_2 = StringVar()
rotor_letter_3_3 = StringVar()

# Set start letter for rotors for Screen.
rotor_letter_1_1.set("B")
rotor_letter_1_2.set("A")
rotor_letter_1_3.set("Z")
rotor_letter_2_1.set("B")
rotor_letter_2_2.set("A")
rotor_letter_2_3.set("Z")
rotor_letter_3_1.set("B")
rotor_letter_3_2.set("A")
rotor_letter_3_3.set("Z")

# Set variables.
error_text = StringVar()

out = StringVar() 

listbox = Listbox()

counter_invalid_letter = 0

# Set alphabet for rotors.
alphabet_for_position_rotor = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")

# Set alphabet(82 letters). 
alphabet =                  ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?")

_alpha_rotor_external =     ("q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p")
_alpha_rotor_internal =     ('a','o','K','P','/','3','U','l','w','c','D','u','H','V','8','ú','Ñ','Y','n','p','4','F','k','*','2','-','O','q','B','C','d','R','I','Z',',','h','L',"¿",'r','Ú','A','.','9','S','x','é','É','Q','i','W','f','6','g','t',' ','7','s','Á','T','Ó','v','G','á','Í','M','ó','m','e','N','+','X','ñ','1','E',"?",'b','y','j','J','5','í','z')

_beta_rotor_external =      ("S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R")
_beta_rotor_internal =      ('k','n','j','*','T','O',',','z','5','L','N','F','B','o','g','P',"¿",'Ñ','3','d',' ','i','Á','J','í','Z','G','.','4','r','q','C','K','-','v','s','1','t','c','U','á','l','h','E','m','e',"?",'x','R','W','H','y','9','Y','ú','7','S','2','6','w','8','é','ñ','ó','b','I','X','u','Í','Q','Ú','D','É','M','+','V','f','a','p','/','A','Ó')

_reflector_rotor_external = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?")
_reflector_rotor_internal = ("y","+","u","a","P","M","í","*","É","v","1","T","F","Q","q","8","E","N"," ","k","L","3","n","X","W","c","h","D","x","Y","-","Ú",",","m","Z","Í","w","S","4","g","V","é","Ó","7","Ñ","6","t","s","C","J","j","b","A",".","/","I","i","o","e","ó","ñ","G","á","9","K","5","U","l","2","r","p","O","ú","z","f","R","d","B","H","Á","?","¿")

# Returns the letter that is in the posiiton of number in source.
def number_to_letter(source, number):
    number -= 1
    if source == alphabet_for_position_rotor:
        
        if number < 0: number += 27
        if number > 26: number -= 27
        number_to_letter_out = source[number]
 
    else:
        number_to_letter_out = source[number]
    
    return number_to_letter_out

# Returns the number of the position of letter in source.
def letter_to_number(source, letter):
    counter = 0 
    for k in source:
        if k == letter:
            letter_to_number_out = counter 
            letter_to_number_out += 1
        counter += 1
    return letter_to_number_out

# Set mousewheel.
def set_mousewheel(widget, command):
    widget.bind("<Enter>", lambda e: widget.bind_all('<MouseWheel>', lambda e: command(e)))
    widget.bind("<Leave>", lambda e: widget.unbind_all('<MouseWheel>'))

# Move one position up all the letters of one rotor.
def letter_up(rotor):
    global number_of_letter_rotor_1
    global number_of_letter_rotor_2
    global number_of_letter_rotor_3

    if rotor == 1:
        number_of_letter_rotor_1 += 1
        if number_of_letter_rotor_1 > 27: number_of_letter_rotor_1 -= 27
        if number_of_letter_rotor_1 < 1: number_of_letter_rotor_1 += 27

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_1 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_1)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_1 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        rotor_letter_1_1.set(value_1)
        rotor_letter_1_2.set(value_2)
        rotor_letter_1_3.set(value_3)

    if rotor == 2:
        number_of_letter_rotor_2 += 1
        if number_of_letter_rotor_2 > 27: number_of_letter_rotor_2 -= 27
        if number_of_letter_rotor_2 < 1: number_of_letter_rotor_2 += 27

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_2 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_2)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_2 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        rotor_letter_2_1.set(value_1)
        rotor_letter_2_2.set(value_2)
        rotor_letter_2_3.set(value_3)

    if rotor == 3:
        number_of_letter_rotor_3 += 1
        if number_of_letter_rotor_3 > 27: number_of_letter_rotor_3 -= 27
        if number_of_letter_rotor_3 < 1: number_of_letter_rotor_3 += 27

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_3 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_3)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_3 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        rotor_letter_3_1.set(value_1)
        rotor_letter_3_2.set(value_2)
        rotor_letter_3_3.set(value_3)

# Move one position down all the letters of one rotor.
def letter_down(rotor):

    global number_of_letter_rotor_1
    global number_of_letter_rotor_2
    global number_of_letter_rotor_3
    if rotor == 1:        
        number_of_letter_rotor_1 -= 1
        if number_of_letter_rotor_1 > 27: number_of_letter_rotor_1 -= 27
        if number_of_letter_rotor_1 < 1: number_of_letter_rotor_1 += 27

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_1 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_1)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_1 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        rotor_letter_1_1.set(value_1)
        rotor_letter_1_2.set(value_2)
        rotor_letter_1_3.set(value_3)

    if rotor == 2:        
        number_of_letter_rotor_2 -= 1
        if number_of_letter_rotor_2 > 27: number_of_letter_rotor_2 -= 27
        if number_of_letter_rotor_2 < 1: number_of_letter_rotor_2 += 27

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number = number_of_letter_rotor_2 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number = number_of_letter_rotor_2)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number = number_of_letter_rotor_2 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        rotor_letter_2_1.set(value_1)
        rotor_letter_2_2.set(value_2)
        rotor_letter_2_3.set(value_3)   

    if rotor == 3:
        number_of_letter_rotor_3 -= 1
        if number_of_letter_rotor_3 > 27: number_of_letter_rotor_3 -= 27
        if number_of_letter_rotor_3 < 1: number_of_letter_rotor_3 += 27

        letter_1 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_3 + 1)
        letter_2 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_3)
        letter_3 = number_to_letter(source=alphabet_for_position_rotor, number=number_of_letter_rotor_3 - 1)

        value_1 = (letter_1)
        value_2 = (letter_2)
        value_3 = (letter_3)

        rotor_letter_3_1.set(value_1)
        rotor_letter_3_2.set(value_2)
        rotor_letter_3_3.set(value_3)

# Reset all the rotor to "A" and clear the error list.
def reset():
    global number_of_letter_rotor_1
    global number_of_letter_rotor_2
    global number_of_letter_rotor_3
    global counter_invalid_letter

    number_of_letter_rotor_1 = 0
    number_of_letter_rotor_2 = 0
    number_of_letter_rotor_3 = 0
    letter_up(rotor=1)
    letter_up(rotor=2)
    letter_up(rotor=3)
    
    while counter_invalid_letter > 0:
        counter_invalid_letter -= 1
        listbox.delete(0)
    counter_invalid_letter = 0

def encript():
    global number_of_letter_rotor_1
    global number_of_letter_rotor_2
    global number_of_letter_rotor_3
    global out
    global counter_invalid_letter

    # Take the input of the entry.
    _input = _input_text.get()

    # If the input has the initial letters of the rotors, remove them from the input and set them as the position of the rotors.
    _input_list = []
    for letter in _input:
        _input_list.append(letter)
    
    _input_list_counter = 0
    try:
        if _input_list[0] in alphabet: _input_list_counter += 1
        if _input_list[1] == " ": _input_list_counter += 1
        if _input_list[2] in alphabet: _input_list_counter += 1
        if _input_list[3] == " ": _input_list_counter += 1
        if _input_list[4] in alphabet: _input_list_counter += 1
        if _input_list[5] == " ": _input_list_counter += 1
    except: pass

    if _input_list_counter == 6:
        _input = ""
        number_of_letter_rotor_1 = letter_to_number(letter=_input_list[0], source=alphabet)
        number_of_letter_rotor_2 = letter_to_number(letter=_input_list[2], source=alphabet)
        number_of_letter_rotor_3 = letter_to_number(letter=_input_list[4], source=alphabet)
        
        counter = 0
        for letter in _input_list:
            if counter > 5: _input += letter
            counter += 1
    _len_input_list = []
    for k in _input:
        _len_input_list.append(k)

    _len_input = len(_len_input_list)
    print(_len_input)
    _position_entry_error = 0

    # Write the initial position of the rotors in _out.
    _out = ""
    _out += number_to_letter(source=alphabet, number=number_of_letter_rotor_1) + " " + number_to_letter(source=alphabet, number=number_of_letter_rotor_2) + " " + number_to_letter(source=alphabet, number=number_of_letter_rotor_3) + " "

    # Encript each letter of the input one by one.
    counter = 1
    for letter in _input:
        if letter in alphabet:
            _position_alpha = number_of_letter_rotor_3
            _position_beta = number_of_letter_rotor_2
            _position_reflector = number_of_letter_rotor_1

            a = int(letter_to_number(source=alphabet, letter=letter))
            a -= _position_alpha
            a += 1
            if a > 82: a -= 82
            elif a < 1: a += 82

            b = number_to_letter(source=_alpha_rotor_external, number=a)
            
            c = int(letter_to_number(source=_alpha_rotor_internal, letter=b))
            c += _position_alpha
            c -= _position_beta
            if c > 82: c -= 82
            elif c < 1: c += 82

            d = number_to_letter(source=_beta_rotor_external, number=c)

            e = int(letter_to_number(source=_beta_rotor_internal, letter=d))
            e += _position_beta
            e -= _position_reflector
            if e > 82: e -= 82
            elif e < 1: e += 82

            f = number_to_letter(source=_reflector_rotor_external, number=e)

            g = int(letter_to_number(source=_reflector_rotor_internal, letter=f))
            g -= _position_beta
            g += _position_reflector
            if g > 82: g -= 82
            elif g < 1: g += 82

            h = number_to_letter(source=_beta_rotor_internal, number=g)

            i = int(letter_to_number(source=_beta_rotor_external, letter=h))
            i -= _position_alpha
            i += _position_beta
            if i > 82: i -= 82
            elif i < 1: i += 82

            j = number_to_letter(source=_alpha_rotor_internal, number=i)

            k = int(letter_to_number(source=_alpha_rotor_external, letter=j))
            k -= 1
            k += _position_alpha
            if k > 82: k -= 82
            elif k < 1: k += 82

            _out += number_to_letter(source=alphabet, number=k)
            out.set(value = (_out))

            if print_all_variables:
                print("\n")

                print("number_of_letter_rotor_1: " + str(number_of_letter_rotor_1))
                print("number_of_letter_rotor_2: " + str(number_of_letter_rotor_2))
                print("number_of_lette_rotor_3: " + str(number_of_letter_rotor_3))

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

                print("3: " + str(number_of_letter_rotor_3))
                print("2: " + str(number_of_letter_rotor_2))
                print("1: " + str(number_of_letter_rotor_1))

            number_of_letter_rotor_3_memory = number_of_letter_rotor_3
            number_of_letter_rotor_2_memory = number_of_letter_rotor_2
            number_of_letter_rotor_1_memory = number_of_letter_rotor_1

            # Add one position to rotor 3.
            letter_up(rotor=3)
            
            # If rotor 3 turns one turn it adds one position to rotor 2.
            if number_of_letter_rotor_3_memory > 26:
                letter_up(rotor=2)
            
            # If rotor 2 turns one turn it adds one position to rotor 3.
            if number_of_letter_rotor_2_memory > 26: letter_up(rotor=1)
            
            # If rotor 3 turns one turn it set all rotor to 1.
            if number_of_letter_rotor_1_memory > 26:
                number_of_letter_rotor_1 = 1
                number_of_letter_rotor_2 = 1
                number_of_letter_rotor_3 = 1

        else: 
            counter_invalid_letter += 1
            error_text = '"' + str(letter) + '"' + " is not in alphabet."
            _position_entry_error += 1
            listbox.insert(_position_entry_error, error_text)

        print(str(counter) + "/" + str(_len_input))
        counter +=1

frm_1 = Frame(window, bg="white", height=244, width=73)
frm_1.place(x=13, y=65)
set_mousewheel(widget=frm_1, command=lambda e: letter_up(rotor=1))

frm_2 = Frame(window, bg="white", height=244, width=73)
frm_2.place(x=112, y=65)
set_mousewheel(frm_2, lambda e: letter_up(rotor=2))

frm_2 = Frame(window, bg="white", height=244, width=73)
frm_2.place(x=211, y=65)
set_mousewheel(frm_2, lambda e: letter_up(rotor=3))

button_up_1 = Button(window, text="UP", bg=color_button, fg=cn,activebackground=actb, width=width_button, height=high_button, command=lambda:letter_up(rotor=1), cursor="hand2").grid(row=1, column=0, padx=13, pady=10)
button_down_1 = Button(window, text="DOWN", bg=color_button, fg=cn, activebackground=actb, width=width_button, height=high_button, command=lambda:letter_down(rotor=1), cursor="hand2").grid(row=5, column=0, padx=13, pady=10)

button_up_2 = Button(window, text="UP", bg=color_button, fg=cn, activebackground=actb, width=width_button, height=high_button, command=lambda:letter_up(rotor=2), cursor="hand2").grid(row=1, column=1, padx=13, pady=10)
button_down_2 = Button(window, text="DOWN", bg=color_button, fg=cn, activebackground=actb, width=width_button, height=high_button, command=lambda:letter_down(rotor=2), cursor="hand2").grid(row=5, column=1, padx=13, pady=10)

button_up_3 = Button(window, text="UP", bg=color_button, fg=cn, activebackground=actb, width=width_button, height=high_button, command=lambda:letter_up(rotor=3), cursor="hand2").grid(row=1, column=2, padx=13, pady=10)
button_down_3 = Button(window, text="DOWN", bg=color_button, fg=cn, activebackground=actb, width=width_button, height=high_button, command=lambda:letter_down(rotor=3), cursor="hand2").grid(row=5, column=2 , padx=13, pady=10)

screen_1_1 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_1_1, borderwidth=0, background="white", justify="right").grid(row=2, column=0, padx=20, pady=20)
screen_1_2 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_1_2, borderwidth=0, background="white", justify="right").grid(row=3, column=0, padx=20, pady=20)
screen_1_3 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_1_3, borderwidth=0, background="white", justify="right").grid(row=4, column=0, padx=20, pady=20)

screen_2_1 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_2_1, borderwidth=0, background="white", justify="right").grid(row=2, column=1, padx=20, pady=20)
screen_2_2 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_2_2, borderwidth=0, background="white", justify="right").grid(row=3, column=1, padx=20, pady=20)
screen_2_3 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_2_3, borderwidth=0, background="white", justify="right").grid(row=4, column=1, padx=20, pady=20)

screen_3_1 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_3_1, borderwidth=0, background="white", justify="right").grid(row=2, column=2, padx=20, pady=20)
screen_3_2 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_3_2, borderwidth=0, background="white", justify="right").grid(row=3, column=2, padx=20, pady=20)
screen_3_3 = Entry(window, font=("arial", 20, "bold"), width=2, textvariable=rotor_letter_3_3, borderwidth=0, background="white", justify="right").grid(row=4, column=2, padx=20, pady=20)

_input_text = Entry(window, font=("arial",15), width=50, textvariable="", borderwidth=3, background="white")
_input_text.place(x=30, y=400)

_output_text = Entry(window, font=("arial",15), width=50, textvariable=out, borderwidth=3, background="white").place(x=30, y=500)

button_encript = Button(window, text="Encript", bg=color_button, fg=cn, activebackground=actb, width=width_button, height=high_button, command=lambda:encript(), cursor="hand2").place(x=30, y=435)

button_reset = Button(window, text="Reset", bg=color_button, fg=cn, activebackground=actb, width=width_button, height=high_button, command=lambda:reset(), cursor="hand2").place(x=350, y=160)

listbox.place(x=450, y=40, width=150, height=300)

window.mainloop()
