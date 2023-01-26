print_all_variables = False

_alpha_rotor_external =     ("q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p")
_alpha_rotor_internal =     ('a','o','K','P','/','3','U','l','w','c','D','u','H','V','8','ú','Ñ','Y','n','p','4','F','k','*','2','-','O','q','B','C','d','R','I','Z',',','h','L','r','Ú','A','.','9','S','x','é','É','Q','i','W','f','6','g','t',' ','7','s','Á','T','Ó','v','G','á','Í','M','ó','m','e','N','+','X','ñ','1','E','b','y','j','J','5','í','z')

_beta_rotor_external =      ("S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R")
_beta_rotor_internal =      ('k','n','j','*','T','O',',','z','5','L','N','F','B','o','g','P','Ñ','3','d',' ','i','Á','J','í','Z','G','.','4','r','q','C','K','-','v','s','1','t','c','U','á','l','h','E','m','e','x','R','W','H','y','9','Y','ú','7','S','2','6','w','8','é','ñ','ó','b','I','X','u','Í','Q','Ú','D','É','M','+','V','f','a','p','/','A','Ó')

_reflector_rotor_external = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/")
_reflector_rotor_internal = ("y","+","u","a","P","M","í","*","É","v","1","T","F","Q","q","8","E","N"," ","k","L","3","n","X","W","c","h","D","x","Y","-","Ú",",","m","Z","Í","w","S","4","g","V","é","Ó","7","Ñ","6","t","s","C","J","j","b","A",".","/","I","i","o","e","ó","ñ","G","á","9","K","5","U","l","2","r","p","O","ú","z","f","R","d","B","H","Á")

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

alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/")
alphabet_for_position_rotor = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")

def number_to_letter(number):
    number -=1
    out = alphabet[number]
    return out

def letter_to_number(letter):
    counter = 0 
    for k in alphabet:
        if k == letter:
            out = counter 
            out += 1
        counter += 1
    return out

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
        
    _position_alpha =  int(letter_to_number(letter=_position_alpha_input))
    _position_beta =  int(letter_to_number(letter=_position_beta_input))
    _position_reflector =  int(letter_to_number(letter=_position_reflector_input))


    _input = input("Enter phrase: ")
    
    out = ""
    for letter in _input:
        if print_all_variables: print("\n")

        _letter = int(letter_to_number(letter=letter))
        _letter -= _position_alpha
        _letter += 1
        if _letter > 80: _letter -= 80
        elif _letter < 1: _letter += 80

        a = alpha_external.number_to_letter(number=_letter)
        if print_all_variables: print(a)
        
        b = int(alpha_internal.letter_to_number(letter=a))
        if print_all_variables: print(b)

        b += _position_alpha
        b -= _position_beta
        if b > 80: b -= 80
        elif b < 1: b += 80

        c = beta_external.number_to_letter(number=b)
        if print_all_variables: print(c)

        d = int(beta_internal.letter_to_number(letter=c))
        if print_all_variables: print("d: " + str(d))

        d += _position_beta
        d -= _position_reflector
        if d > 80: d -= 80
        elif d < 1: d += 80

        e = reflector_external.number_to_letter(number=d)
        if print_all_variables: print("e: " + e)

        f = int(reflector_internal.letter_to_number(letter=e))
        if print_all_variables: print("f: " + str(f))        

        f-=_position_beta
        f+=_position_reflector
        if f > 80: f -= 80
        elif f < 1: f += 80

        g = beta_internal.number_to_letter(number=f)
        if print_all_variables: print(g)

        h = int(beta_external.letter_to_number(letter=g))
        if print_all_variables: print(h)

        h -=_position_alpha
        h +=_position_beta
        if h > 80: h -= 80
        elif h < 1: h += 80

        i = alpha_internal.number_to_letter(number=h)
        if print_all_variables: print(i)

        j = int(alpha_external.letter_to_number(letter=i))
        if print_all_variables: print(j)

        j -= 1
        j += _position_alpha
        if j > 80: j -= 80
        elif j < 1: j += 80

        _position_alpha += 1
        if _position_alpha > 27:
            _position_alpha -= 27
            _position_beta += 1

        if _position_beta > 27:
            _position_beta -= 27
            _position_reflector += 1

        if _position_reflector > 27:
            _position_reflector -= 27

        out += number_to_letter(number=j)
        
    print(out)
