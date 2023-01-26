print_all_variables = False
error_text = ""

alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/")
alphabet_for_position_rotor = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")

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

while True:
    _position_alpha_pass = True
    while _position_alpha_pass:
        _position_alpha_input = input("Position alpha: ")
        if _position_alpha_input in alphabet_for_position_rotor:
            _position_alpha_pass =  False
        else: print("Invalid input.")

    _position_beta_pass = True
    while _position_beta_pass:
        _position_beta_input = input("Position beta: ")
        if _position_beta_input in alphabet_for_position_rotor:
            _position_beta_pass = False
        else: print("Invalid input.")

    _position_reflector_pass = True
    while _position_reflector_pass:
        _position_reflector_input = input("Position reflector: ")
        if _position_reflector_input in alphabet_for_position_rotor:
            _position_reflector_pass = False
        else: print("Invalid input.")
        
    _position_alpha =  int(letter_to_number(source=alphabet, letter=_position_alpha_input))
    _position_beta =  int(letter_to_number(source=alphabet, letter=_position_beta_input))
    _position_reflector =  int(letter_to_number(source=alphabet, letter=_position_reflector_input))

    _input = input("Enter phrase: ")
    
    out = ""
    for letter in _input:
        if letter in alphabet:

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

            _position_alpha += 1

            if _position_alpha > 26: _position_beta += 1
                
            if _position_beta > 26: _position_reflector += 1
            if _position_reflector > 26:
                _position_alpha = 1
                _position_beta = 1
                _position_reflector = 1

            out += number_to_letter(source=alphabet, number=j)

        else: 
            error_text = '"' + str(letter) + '"' + " is not in the alphabet."
            print(error_text)
    print(out)
