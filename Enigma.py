from time import sleep
import threading
from random import randrange

print_all_variables = False

# Set rotors position.
number_of_letter_rotor_1 = 1
number_of_letter_rotor_2 = 1
number_of_letter_rotor_3 = 1

counter_invalid_letter = 0

encripted_letters = []

start_encript = []

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
   return source[number]

# Returns the number of the position of letter in source.
def letter_to_number(source, letter):
    return source.index(letter)

def encript(message):
    

    # If the input has the initial letters of the rotors, remove them from the input and set them as the position of the rotors.
    if message[0] in alphabet and message[1] == " " and message[2] in alphabet and message[3] == " " and message[4] in alphabet and message[5] == " ":
        number_of_letter_rotor_1 = letter_to_number(letter=message[0], source=alphabet)
        number_of_letter_rotor_2 = letter_to_number(letter=message[2], source=alphabet)
        number_of_letter_rotor_3 = letter_to_number(letter=message[4], source=alphabet)
        message = message[6:len(message)]
    else:
        number_of_letter_rotor_1 = randrange(81)
        number_of_letter_rotor_2 = randrange(81)
        number_of_letter_rotor_3 = randrange(81)

    # Write the initial position of the rotors in _out.
    _out = ""
    _out += number_to_letter(source=alphabet, number=number_of_letter_rotor_1) + " " + number_to_letter(source=alphabet, number=number_of_letter_rotor_2) + " " + number_to_letter(source=alphabet, number=number_of_letter_rotor_3) + " "
    
    _max = len(alphabet) - 1
    _min = 0
    _add_substract = len(alphabet)
    # Encript each letter of the input one by one.
    for letter in message:
        if letter in alphabet:
            _position_alpha = number_of_letter_rotor_3
            _position_beta = number_of_letter_rotor_2
            _position_reflector = number_of_letter_rotor_1

            a = int(letter_to_number(source=alphabet, letter=letter))
            a -= _position_alpha
            a += 1

            if a > _max: a -= _add_substract
            elif a < _min: a += _add_substract

            b = number_to_letter(source=_alpha_rotor_external, number=a)
            
            c = int(letter_to_number(source=_alpha_rotor_internal, letter=b))
            c += _position_alpha
            c -= _position_beta

            if c > _max: c -= _add_substract
            elif c < _min: c += _add_substract

            d = number_to_letter(source=_beta_rotor_external, number=c)

            e = int(letter_to_number(source=_beta_rotor_internal, letter=d))
            e += _position_beta
            e -= _position_reflector

            if e > _max: e -= _add_substract
            elif e < _min: e += _add_substract

            f = number_to_letter(source=_reflector_rotor_external, number=e)

            g = int(letter_to_number(source=_reflector_rotor_internal, letter=f))
            g -= _position_beta
            g += _position_reflector

            if g > _max: g -= _add_substract
            elif g < _min: g += _add_substract

            h = number_to_letter(source=_beta_rotor_internal, number=g)

            i = int(letter_to_number(source=_beta_rotor_external, letter=h))
            i -= _position_alpha
            i += _position_beta

            if i > _max: i -= _add_substract
            elif i < _min: i += _add_substract

            j = number_to_letter(source=_alpha_rotor_internal, number=i)

            k = int(letter_to_number(source=_alpha_rotor_external, letter=j))
            k -= 1
            k += _position_alpha

            print("k before: " + str(k))

            if k > _max: k -= _add_substract
            elif k < _min: k += _add_substract

            print("k after: " + str(k))
            _out += number_to_letter(source=alphabet, number=k)

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

        else: 
            print(letter + "is not in the alphabet")
    print(_out)

while True:
    _input = input("Enter message: ")
    message_encripted = encript(message=_input)
