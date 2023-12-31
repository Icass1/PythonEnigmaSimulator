from random import randrange, shuffle
import os

simple_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú", "0", "1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?", "=", "_", ":", "(", ")", "[", "]", "{", "}", "#", '"', "<", ">", "!", "\n"]

long_alphabet = ['•', '¶', '§', 'A', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '€', 'ƒ', '„', '…', '†', '‡', '‰', 'Š', 'Œ', 'Ž', '‘', '’', '“', '”', '—', '™', 'š', 'œ', 'ž', 'Ÿ', '¡', '!', '¢', '£', '¤', '¥', '¦', '¨',
'©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', 'µ', '·', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô',
'Õ', 'Ö', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü',
'ý', 'þ', 'ÿ', 'Å', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '\n']

def clean_alphabet(alphabet):
    
    out = []
    file = open("fileasdf.txt", "w")
    for k in alphabet:
        try: 
            file.write(k)
            out.append(k)
        except: 
            print(f"Deleting {k}")
    file.close()
    os.remove("fileasdf.txt")
    return out

def _pop(index, list):
    _out = []
    for element in list:
        if list.index(element) == index:
            pass
        else: _out.append(element)
    return _out

def check(list):
    values = list
    repeated = []
    single = []
    for x in values:
        if x not in single:
            single.append(x)
        else:
            if x not in repeated:
                repeated.append(x)
    print("Repeated: {}".format(repeated))

def generate_pairs(alphabet):
    global list_pairs
    _list = alphabet

    list_pairs = []
    while len(_list) != 0:
        random_number = randrange(len(_list))
        random_leter = _list[random_number]



        list_to_append = [_list[0], random_leter]
        list_pairs.append(list_to_append)
        _list = _pop(index=0, list=_list)

        try: _list = _pop(index=_list.index(random_leter), list=_list)
        except: pass

    # print(len(list_pairs)) 

    list_1 = []
    list_2 = []
    for pair in list_pairs:
        if pair[0] == pair[1]:
            list_1.append(pair[0])
            list_2.append(pair[1])
        else:
            list_1.append(pair[0])
            list_1.append(pair[1])

            list_2.append(pair[1])
            list_2.append(pair[0])
    return list_1, list_2

def create_lists(alphabet, rotors):

    list_1, list_2 = generate_pairs(alphabet=alphabet)
    
    print("alphabet =                  {}".format(str(alphabet)))
    print("")
    shuffle(alphabet)

    for k in range(1, rotors):
        print("_rotor_{}_external =         {}".format(k, str(alphabet)))
        shuffle(alphabet)
        print("_rotor_{}_internal =         {}".format(k, str(alphabet)))
        print("")
        shuffle(alphabet)

    print("_rotor_reflector_external = {}".format(str(list_1)))
    print("_rotor_reflector_internal = {}".format(str(list_2)))

    print("")

    print("sources.append(alphabet)")

    for k in range(1, rotors):
        print(f"sources.append(_rotor_{k}_external)")
        print(f"sources.append(_rotor_{k}_internal)")

    print("sources.append(_rotor_reflector_external)")
    print("sources.append(_rotor_reflector_internal)")
    
    write = True

    if write:
        
        file = open(file = "rotors.py", mode="w", encoding="utf-8")
        
        file.write("sources = []\n")

        file.write("\n")

        file.write("def get_sources():\n")
        file.write("    return sources\n")

        file.write("\n\n")

        file.write("alphabet =                  {}\n".format(str(alphabet)))
        file.write("\n")
        shuffle(alphabet)

        for k in range(1, rotors):
            file.write("_rotor_{}_external =         {}\n".format(k, str(alphabet)))
            shuffle(alphabet)
            file.write("_rotor_{}_internal =         {}\n".format(k, str(alphabet)))
            file.write("\n")
            shuffle(alphabet)

        file.write("_rotor_reflector_external = {}\n".format(str(list_1)))
        file.write("_rotor_reflector_internal = {}\n".format(str(list_2)))

        file.write("\n")

        file.write("sources.append(alphabet)\n")

        for k in range(1, rotors):
            file.write(f"sources.append(_rotor_{k}_external)\n")
            file.write(f"sources.append(_rotor_{k}_internal)\n")

        file.write("sources.append(_rotor_reflector_external)\n")
        file.write("sources.append(_rotor_reflector_internal)\n")
        file.close()
        
# create_lists(alphabet=long_alphabet, rotors=30)
# print(clean_alphabet(new_long_alphabet))


out = []
for k in range(10000):
    out.append(chr(k))

print(out)
print(ord("\n"))